from collections import deque

from rtgl.base import Database

type Path = list[tuple[str, str, str]]  # foreign key, table name, edge type ("f" ... forward, "r" ... reversed)
type Relations = dict[str, dict[str, list[tuple[str, str]]]]  # src table name -> dst table name -> (foreign key, edge type)


class PathBuilder:

    def __init__(self, db: Database, cte_dict: dict, predefined_paths: dict):
        self.db = db
        self.cte_dict = cte_dict
        self.predefined_paths = predefined_paths

        self.paths = {}
        self.norm_predefined_paths = self._normalize_predefined_paths()
        self.relations = self._build_relations()

    def find_shortest_path(self, src_table: str, dst_table: str) -> tuple[Path | None, str]:
        if src_table in self.norm_predefined_paths:
            return self.find_orig_src_table(src_table), self.norm_predefined_paths[src_table]

        self.paths.setdefault(src_table, {}).setdefault(dst_table, [])
        if path := self.paths[src_table][dst_table]:
            return src_table, path

        paths = self.build_paths(src_table, dst_table)

        return src_table, (paths[0] if paths else [])
        
    def build_paths(self, src_table: str, dst_table: str) -> list[Path]:
        if src_table == dst_table:
            return []

        self.paths.setdefault(src_table, {}).setdefault(dst_table, [])    

        paths = []
        queue = deque([(src_table, [], {src_table})])

        while queue:
            cur_table, path, visited = queue.popleft()
            if cur_table == dst_table:
                paths.append(path)

                if len(paths) == 1:
                    self.paths[src_table][dst_table] = path
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
                
        return paths

    def find_orig_src_table(self, path_name: str) -> str | None:
        if predefined_path := self.predefined_paths.get(path_name):
            return predefined_path[0][1]
        
        return path_name

    def _build_relations(self) -> Relations:
        relations = {}

        def _add_relation(src_table: str, dst_table: str, fk: str):
            relations.setdefault(src_table, {}).setdefault(dst_table, [])
            relations.setdefault(dst_table, {}).setdefault(src_table, [])
            
            forward_edge = (fk, "f")
            reversed_edge = (fk, "r")

            if forward_edge not in relations[src_table][dst_table]:
                relations[src_table][dst_table].append(forward_edge)
                relations[dst_table][src_table].append(reversed_edge)

        for table_name, table_obj in self.db.table_dict.items():
            for fk, ptable in (table_obj.fkey_col_to_pkey_table or {}).items():
                _add_relation(table_name, ptable, fk)

        for cte_name, (cte_obj, fk_table_fk_col) in self.cte_dict.items():
            for fk, ptable in (cte_obj.fkey_col_to_pkey_table or {}).items():
               _add_relation(cte_name, ptable, fk)
            
            for ctable, fk in fk_table_fk_col.items():
                _add_relation(ctable, cte_name, fk)                                                                   
        
        return relations

    def _normalize_predefined_paths(self) -> dict[str, Path] | None:
        processed_paths = {}
        for path_alias, path in self.predefined_paths.items():
            processed_path = []
            prev_fk = path[0][0]
            for fk, table in path[1:]:
                if table_inf := self.cte_dict.get(table):
                    table_obj, _ = table_inf
                    if table_obj.pkey_col and table_obj.pkey_col == fk:
                        processed_path.append((prev_fk, table, "f"))
                    else:
                        processed_path.append((prev_fk, table, "r"))

                if table_obj := self.db.table_dict.get(table):
                    if table_obj.pkey_col and table_obj.pkey_col == fk:
                        processed_path.append((prev_fk, table, "f"))
                    else:
                        processed_path.append((prev_fk, table, "r"))
                prev_fk = fk

            processed_paths[path_alias] = processed_path

        return processed_paths
