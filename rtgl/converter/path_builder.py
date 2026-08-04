import warnings
from collections import deque

from rtgl.base import Database

type Path = list[tuple[str, str, str]]  # foreign key, table name, edge type ("f" ... forward, "r" ... reversed)
type Relations = dict[str, dict[str, list[tuple[str, str]]]]  # src table name -> dst table name -> (foreign key, edge type)


class PathBuilder:

    def __init__(self, db: Database, cte_dict: dict):
        self.db = db
        self.cte_dict = cte_dict

        self.relations, self.extended_relations = self._build_relations()

    def build_path(self, src_table: str, dst_table: str) -> Path:
        if src_table == dst_table:
            return []

        def _bfs(relations: Relations) -> list[Path]:
            queue = deque([(src_table, [], {src_table})])
            found_paths = []

            while queue:
                cur_table, path, visited = queue.popleft()
                if cur_table == dst_table:
                    found_paths.append(path)
                    continue

                # print(relations.get(cur_table))
                for next_table, rels_list in relations.get(cur_table, {}).items():
                    if next_table in visited:
                        continue

                    for next_fk, edge_type in rels_list:
                        # print(next_table, next_fk, edge_type)

                        queue.append((
                            next_table,
                            path + [(next_fk, next_table, edge_type)],
                            visited | {next_table})
                        )

            return found_paths

        paths = _bfs(self.extended_relations)

        # if len(paths) > 1:
        #     warnings.warn((
        #         f"Multiple paths found between {src_table!r} and {dst_table!r}!\n"
        #         f"Using the first shortest path: {paths[0]}."
        #         ), stacklevel=2
        #     )
        # print(paths)
        # print(paths)
        return paths[0]

    def _build_relations(self) -> tuple[Relations, Relations]:
        relations = {}
        extended_relations = {}

        def _add_relation(src_table: str, dst_table: str, fk: str):
            relations.setdefault(src_table, {}).setdefault(dst_table, [])
            extended_relations.setdefault(src_table, {}).setdefault(dst_table, [])
            extended_relations.setdefault(dst_table, {}).setdefault(src_table, [])
            
            forward_edge = (fk, "f")
            reversed_edge = (fk, "r")

            if forward_edge not in relations[src_table][dst_table]:
                relations[src_table][dst_table].append(forward_edge)

            if forward_edge not in extended_relations[src_table][dst_table]:
                extended_relations[src_table][dst_table].append(forward_edge)
                extended_relations[dst_table][src_table].append(reversed_edge)

        for table_name, table_obj in self.db.table_dict.items():
            for fk, ptable in (table_obj.fkey_col_to_pkey_table or {}).items():
                _add_relation(table_name, ptable, fk)

        for cte_name, (cte_obj, fk_table_fk_col) in self.cte_dict.items():
            for fk, ptable in (cte_obj.fkey_col_to_pkey_table or {}).items():
               _add_relation(cte_name, ptable, fk)
            
            for ctable, fk in fk_table_fk_col.items():
                _add_relation(ctable, cte_name, fk)                                                                   
        
        return relations, extended_relations
