"""Foreign-key path resolution for joining tables in RTGL queries."""

from collections import deque

from rtgl.base.database_explorer import DatabaseExplorer

# foreign key, table name, edge type ("f" ... forward, "r" ... reversed)
type Path = list[tuple[str, str, str]]
# src table name -> dst table name -> (foreign key, edge type)
type Relations = dict[str, dict[str, list[tuple[str, str]]]]


class PathBuilder:
    r"""Resolves how two tables should be joined in the generated SQL.

    Given a *`DatabaseExplorer`* and predefined paths, builds a graph of
    foreign-key relations between tables and finds the shortest join path between any two of
    them. Also validates and resolves Common Path Expressions (CPEs): named, user-declared
    join paths that let a query reach a table through an explicit multi-hop route instead of
    the automatically discovered shortest one.
    """

    def __init__(self, db_explorer: DatabaseExplorer, predefined_paths: dict):
        r"""Initialize the path builder and precompute its relation graph.

        Args:
            db_explorer (DatabaseExplorer): *`DatabaseExplorer`* used to resolve table/column
                names and look up CTE/SQL-injection relations.
            predefined_paths (dict): Mapping of CPE alias (*`ParsedValue`*) to its list of
                (table, left_key, right_key) hops, as parsed from `WITH ... AS (...)` clauses.

        Returns:
            out (None):
        """
        self.db_explorer = db_explorer

        self.paths = {}
        # relations must exist before predefined paths can be matched against them
        self.relations = self._build_relations()
        self.predefined_paths = self._normalize_predefined_paths(predefined_paths)

    def find_shortest_path(self, src_table: str, dst_table: str) -> tuple[Path | None, str]:
        r"""Find the join path from a source table to a destination table.

        If `src_table` is a CPE alias, resolves it to its declared path and origin table
        instead of searching the relation graph.

        Args:
            src_table (str): Name of the source table, or a CPE alias.
            dst_table (str): Name of the destination table to reach.

        Returns:
            out (tuple[Path | None, str]): Tuple of (actual source table name, join path).
                The path is empty if `src_table` and `dst_table` are the same table.
        """
        src_table, dst_table = src_table.lower(), dst_table.lower()

        if src_table in self.predefined_paths:
            return self.find_orig_src_table(src_table), self.predefined_paths[src_table][0]

        paths = self.build_paths(src_table, dst_table)

        return src_table, (paths[0] if paths else [])

    def find_orig_src_table(self, path_name: str) -> str | None:
        r"""Resolve a name to the real table it refers to.

        Args:
            path_name (str): A table name, or a CPE alias declared via `WITH ... AS (...)`.

        Returns:
            out (str | None): The origin table of the CPE if `path_name` is a CPE alias,
                otherwise `path_name` unchanged (it is already a real table name).
        """
        path_name = path_name.lower()

        if predefined_path := self.predefined_paths.get(path_name):
            return predefined_path[1]

        return path_name

    def is_path_correct(self, path_name: str) -> bool:
        r"""Check whether a CPE's declared hops match real foreign-key relations.

        Args:
            path_name (str): A CPE alias declared via `WITH ... AS (...)`.

        Returns:
            out (bool): True if every hop in the CPE corresponds to an actual foreign-key
                relation in the schema, False if `path_name` is not a known CPE alias or
                any of its hops is invalid.
        """
        path_name = path_name.lower()

        if predefined_path := self.predefined_paths.get(path_name):
            return predefined_path[2]

        return False

    def is_path_temporal(self, path: Path, src_table: str) -> bool:
        r"""Check whether any table along a join path has a time column.

        Used to decide whether temporal join constraints (matching each hop's timestamp to
        the prediction window) are needed when joining through this path.

        Args:
            path (Path): Join path, as returned by `find_shortest_path`/`build_paths`.
            src_table (str): Name of the table the path starts from.

        Returns:
            out (bool): True if `src_table` or any intermediate table on the path (excluding
                the final destination table) has a time column.
        """
        src_table = src_table.lower()

        # walk the source table plus every intermediate table (the destination is excluded,
        # since its time column is handled by the caller separately)
        path = [(None, src_table, None)] + path[:-1]

        return any(self.db_explorer.find_time_column(table) for _, table, _ in path)

    def build_paths(self, src_table: str, dst_table: str, only_temporal: bool=False) -> list[Path]:
        r"""Find the shortest path(s) between two tables via breadth-first search.

        Results are cached per (src_table, dst_table, only_temporal) combination. Stops after
        finding up to two shortest paths: a second path of the same length means the shortest
        path is ambiguous, which is all the caller needs to know without exploring further.

        Args:
            src_table (str): Name of the source table, or a CPE alias.
            dst_table (str): Name of the destination table to reach.
            only_temporal (bool): If True, only return paths that pass through at least one
                table with a time column (excluding the destination table). Applies to a CPE's
                own declared path too: if it isn't temporal, no path is returned for it.

        Returns:
            out (list[Path]): List of shortest paths found (0, 1, or 2 paths).
        """
        src_table, dst_table = src_table.lower(), dst_table.lower()

        if src_table in self.predefined_paths:
            path, src_table, _ = self.predefined_paths[src_table]
            if only_temporal and not self.is_path_temporal(path, src_table):
                return []
            return [path]

        if src_table == dst_table:
            return []

        # only_temporal is part of the cache key: the same (src, dst) pair can have a
        # different shortest path depending on whether it must pass through a time column
        cache_key = (dst_table, only_temporal)
        self.paths.setdefault(src_table, {}).setdefault(cache_key, [])
        if paths := self.paths[src_table][cache_key]:
            return paths

        paths = []
        queue = deque([(src_table, [], {src_table})])

        while queue:
            cur_table, path, visited = queue.popleft()
            if cur_table == dst_table:
                if only_temporal and not self.is_path_temporal(path, src_table):
                    continue

                paths.append(path)

                if len(paths) == 1:
                    self.paths[src_table][cache_key] = [path]
                    continue
                else:
                    break

            for next_table, rels_list in self.relations.get(cur_table, {}).items():
                if next_table in visited:
                    continue

                for next_fk, edge_type in rels_list:
                    queue.append((
                        next_table,
                        path + [(next_fk, next_table, edge_type)],
                        visited | {next_table})
                    )

        self.paths[src_table][cache_key] = paths

        return paths

    def _build_relations(self) -> Relations:
        r"""Build the undirected graph of foreign-key relations between all tables.

        Combines relations from the schema's tables with relations declared by SQL
        injections/CTEs: both the injected table's own outgoing foreign keys and the
        foreign keys other tables declare pointing into it.

        Returns:
            out (Relations): Adjacency map from each table to its directly related tables,
                with the connecting foreign-key column and edge direction for each relation.
        """
        relations = {}

        def _add_relation(src_table: str, dst_table: str, fk: str):
            relations.setdefault(src_table, {}).setdefault(dst_table, [])
            relations.setdefault(dst_table, {}).setdefault(src_table, [])

            forward_edge = (fk, "f")
            reversed_edge = (fk, "r")

            if forward_edge not in relations[src_table][dst_table]:
                relations[src_table][dst_table].append(forward_edge)
                relations[dst_table][src_table].append(reversed_edge)

        for table_name, table_obj in self.db_explorer.norm_db.table_dict.items():
            for fk, ptable in (table_obj.fkey_col_to_pkey_table or {}).items():
                _add_relation(table_name, ptable, fk)

        for cte_name, (cte_obj, fkey_table_to_fkey_col) in self.db_explorer.cte_dict.items():
            for fk, ptable in (cte_obj.fkey_col_to_pkey_table or {}).items():
               _add_relation(cte_name, ptable, fk)

            for ctable, fk in fkey_table_to_fkey_col.items():
                _add_relation(ctable, cte_name, fk)

        return relations

    def _normalize_predefined_paths(self, predefined_paths) -> dict[str, Path] | None:
        r"""Validate and convert declared CPE hops into ready-to-use join paths.

        For each CPE, walks its declared `table.key -> table.key` hops and matches each one
        against the actual relation graph to determine whether it is a forward or reversed
        foreign-key edge. A CPE is marked incorrect as soon as a hop doesn't correspond to
        any real relation (e.g. a typo'd table/column, or a completely made-up join).

        Args:
            predefined_paths (dict): Mapping of CPE alias (*`ParsedValue`*) to its list of
                (table, left_key, right_key) hops, as parsed from `WITH ... AS (...)` clauses.

        Returns:
            out (dict[str, Path] | None): Mapping of CPE alias to
                (resolved path, origin table name, whether every hop was valid).
        """
        processed_paths = {}
        for path_alias, path in predefined_paths.items():
            path_alias = path_alias.value
            processed_path = []

            src_table = path[0][0]
            is_correct = True

            for i in range(len(path) - 1):
                table, left_key, right_key = path[i]
                next_table, next_left_key, _ = path[i + 1]

                # the key used to join out of table is its right_key if given
                current_key = right_key if right_key else left_key

                if not (table_inf := self.db_explorer.find_table(table)):
                    is_correct = False
                    break

                _, _, table_obj, _ = table_inf

                if table_obj.pkey_col and table_obj.pkey_col == current_key:
                    relation = (next_left_key, "r")
                else:
                    relation = (current_key, "f")

                if relation not in self.relations.get(table, {}).get(next_table, []):
                    is_correct = False
                    break

                processed_path.append((relation[0], next_table, relation[1]))

            processed_paths[path_alias] = (processed_path, src_table, is_correct)

        return processed_paths
