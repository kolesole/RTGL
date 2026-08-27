"""Database explorer module which provides functionality to explore a database and its tables."""

from rtgl.base.database import Database
from rtgl.base.table import Table


class DatabaseExplorer:
    r"""Database explorer class that provides functionality to explore a database and its tables.

    Has methods to normalize databases, find tables, columns, etc. in a case-insensitive manner.
    """

    def __init__(self, db: Database, cte_dict: dict):
        r"""Initialize the explorer with a database and its CTE/SQL-injection table declarations.

        Args:
            db (Database): *`Database`* instance containing the schema and data tables to explore.
            cte_dict (dict): Mapping of CTE/SQL-injection table name to its *`Table`* and
                foreign-key info, as built by the converter.

        Returns:
            out (None):
        """
        self.db = db
        self.norm_db = self.normalize_db()
        self.cte_dict = cte_dict

    def normalize_table(self, table_obj: Table) -> Table:
        r"""Normalize a *`Table`* object by converting all column names to lowercase.
    
        Args:
            table_obj (Table): *`Table`* object to be normalized.
    
        Returns:
            out (Table): Normalized *`Table`* object with lowercase column names.
        """
        return Table(
            df=table_obj.df.head(0).rename(columns=str.lower) if table_obj.df is not None else None,
            fkey_col_to_pkey_table={
                fk.lower(): ptable for fk, ptable in (table_obj.fkey_col_to_pkey_table or {}).items()
            },
            pkey_col=table_obj.pkey_col.lower() if table_obj.pkey_col else None,
            time_col=table_obj.time_col.lower() if table_obj.time_col else None,
        )
    
    def normalize_db(self) -> Database:
        r"""Normalize a *`Database`* instance by converting all table and column names to lowercase.
    
        Returns:
            out (Database): Normalized *`Database`* instance with lowercase table and column names.
        """
        return Database(
            table_dict={name.lower(): self.normalize_table(table)
                for name, table in self.db.table_dict.items()} if self.db.table_dict else {}
        )

    def find_table(self, table: str) -> tuple[str, str, Table, dict[str, str] | None] | None:
        r"""Find a *`Table`* object in the *`Database`* by its name (case-insensitive).

        Args:
            table (str): Name of the table to find.

        Returns:
            out (tuple[str, Table] | None): Tuple of the form (original_table_name, Table)
                Returns None if no table with the given name was found.
        """
        table = table.lower()

        if cte_inf := self.cte_dict.get(table):
            return "cte", table, *cte_inf

        if table_obj := self.norm_db.table_dict.get(table):
            return "db", table, table_obj, None

        return None

    def find_column(self, table: str, column: str) -> str | None:
        r"""Find a column name in a table (case-insensitive).

        Args:
            table (str): Name of the table.
            column (str): Name of the column to find.

        Returns:
            out (str | None): Original name of the column if found, None otherwise.
        """
        column = column.lower()

        if not (table_inf := self.find_table(table)):
            return None

        loc, _, table_obj, _ = table_inf

        if column == "*":
            return table_obj.pkey_col if table_obj.pkey_col else "*"

        if loc == "cte":
            return column
        elif loc == "db":
            return column if column in table_obj.df else None

        return None

    def find_ptable(self, table: str, fk: str) -> str | None:
        r"""Find the parent table name that a given table references through a given foreign key (case-insensitive).

        Args:
            table (str): Name of the child table.
            fk (str): Name of the foreign key column in the child table.

        Returns:
            out (str | None): Name of the parent table that the child table references through the foreign key column
                if found, None otherwise.
        """
        table, fk = table.lower(), fk.lower()

        if not (table_inf := self.find_table(table)):
            return None

        for cte_name, (_, fkey_table_to_fkey_col) in self.cte_dict.items():
            if (fk_col := fkey_table_to_fkey_col.get(table)) and (fk_col == fk):
                return cte_name

        _, _, table_obj, _ = table_inf

        return (table_obj.fkey_col_to_pkey_table or {}).get(fk) if table_obj else None

    def find_pkey(self, table: str) -> str | None:
        r"""Find the primary key column of a table (case-insensitive).

        Args:
            table (str): Name of the table.

        Returns:
            out (str | None): Name of the primary key column of the table if found, None otherwise.
        """
        if not (table_inf := self.find_table(table)):
            return None
        
        _, _, table_obj, _ = table_inf
        return table_obj.pkey_col

    def find_orig_name(self, table: str) -> str | None:
        r"""Find the original name of a table (case-insensitive).

        Args:
            table (str): Name of the table.

        Returns:
            out (str | None): Original name of the table if found, None otherwise.
        """
        table = table.lower()
            
        for orig_name in self.db.table_dict:
            if orig_name.lower() == table:
                return orig_name
            
        return None

    def find_time_column(self, table: str) -> str | None:
        r"""Find the name of the time column for a given table (case-insensitive).

        Args:
            table (str): Name of the table whose time column is to be found.

        Returns:
            out (str | None): The name of the time column associated with the specified table,
                or None if the table has no time column.
        """
        if not (table_inf := self.find_table(table)):
            return None
        
        _, _, table_obj, _ = table_inf

        return table_obj.time_col
