# RTGL

[![PyPI](https://img.shields.io/pypi/v/rtgl)](https://pypi.org/project/rtgl/)
[![Python](https://img.shields.io/badge/python-3.12%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)

**RTGL (Relational Task Generation Language)** is a Python framework for writing compact, expressive
predictive queries over relational data, with a focus on **Relational Deep Learning**, and inspired by the proprietary **PQL** from [**KumoAI**](https://docs.nvidia.com/sdgm/rfm/overview).

Defining a prediction task over relational databases usually means hand-writing SQL or pandas pipelines for entity selection, temporal joins, and label aggregation: code that is verbose, easy to get subtly wrong, and rarely reusable across tasks. 
RTGL replaces that boilerplate: declare *what* to predict and *for whom*, and RTGL compiles the query to SQL, optionally executes it, and returns the result.

## 🧠 Features

- 🔀 **Two converters**: `SConverter` for static prediction queries, `TConverter` for temporal
  queries evaluated at a set of prediction timestamps.
- 🔍 **Automatic validation**: built-in *syntactic* and *semantic* checks reject malformed queries and schema mismatches before any SQL is executed.
- 🔗 **Multi-hop relationships**: resolves the shortest foreign-key path between two tables automatically, *not just direct relations*.
- 🧵 **Common Path Expressions (CPEs)**: name an explicit join path and reference it like a regular table, including cases where several equally short paths make automatic resolution ambiguous.
- 💉 **SQL Injections**: drop a raw SQL query in as a *virtual table*, declare its keys, and use it anywhere a table is expected.
- ⚙️ **Dual output mode**: `execute=False` returns the generated SQL; `execute=True` runs it on DuckDB and returns a `Table` object.

## 📦 Installation

```bash
pip install rtgl
```

## 🚀 Quickstart

### 1. Describe Your `Database`

**RTGL** operates over a `Database` of `Table` objects. 
Wrap each pandas `DataFrame` with its primary key, its foreign keys, and an optional time column.

A database can be supplied either as a [RelBench](https://relbench.stanford.edu/) `Database` object or through RTGL's own simplified equivalent, shown below.

```python
import pandas as pd
from rtgl.base import Database, Table

users = pd.DataFrame({
    "user_id": [1, 2, 3],
    "registration_date": pd.to_datetime(["2024-01-01", "2025-07-23", "2026-08-08"]),
    # ... other columns
})
orders = pd.DataFrame({
    "user_id": [1, 1, 1, 3],
    "order_date": pd.to_datetime(["2026-07-05", "2026-07-20", "2026-08-10", "2026-08-15"]),
    # ... other columns
})
# ... other dataframes

db = Database(table_dict={
    "users": Table(
        df=users,
        pkey_col="user_id",
        time_col="registration_date",
    ),
    "orders": Table(
        df=orders,
        fkey_col_to_pkey_table={"user_id": "users"},
        time_col="order_date",
    ),
    # ... other tables
})
```

### 2. Static Query with `SConverter`

A static query produces exactly one label per entity, independent of time.

```python
from rtgl.converter import SConverter

converter = SConverter(db)

# how many orders has each user placed, over all time?
rtgl_query = """
    PREDICT COUNT(orders.*)
    FOR EACH users.*;
"""

# returns the generated SQL query
sql_query = converter.convert(rtgl_query, execute=False)

# returns a Table object with (fk, label) columns
table = converter.convert(rtgl_query, execute=True)

print(table.df)
#    fk  label
# 0   1      3
# 1   2      0
# 2   3      1

# db can be replaced later without rebuilding the converter
new_db = ...
converter.set_db(new_db)
```

### 3. Temporal Query with `TConverter`

A temporal query is evaluated at a set of prediction timestamps, and every aggregation is computed over a time window relative to each one.

```python
import pandas as pd
from rtgl.converter import TConverter

timestamps = pd.Series(pd.to_datetime(["2026-07-01", "2026-08-09"]))
converter = TConverter(db, timestamps)

# how much will each user place orders in the 30 days following each timestamp?
rtgl_query = """
    PREDICT COUNT(orders.*, 0, 30, DAYS)
    FOR EACH users.*;
"""

# returns the generated SQL query
sql_query = converter.convert(rtgl_query, execute=False) 

# returns a Table object with (fk, timestamp, label) columns
table = converter.convert(rtgl_query, execute=True) 

print(table.df)
#    fk   timestamp  label
# 0   1  2026-07-01      2  
# 1   2  2026-07-01      0
# 2   1  2026-08-09      1
# 3   2  2026-08-09      0
# 4   3  2026-08-09      1

# db and timestamps can be replaced later without rebuilding the converter
new_db = ...
converter.set_db(new_db)
new_timestamps = ...
converter.set_timestamps(new_timestamps)
```

Note: User 3 has no row at `2026-07-01`: their `registration_date` (`2026-08-08`) falls after that timestamp, so RTGL excludes them automatically. 
By `2026-08-09` they exist, and a row appears. 
See [RTGL Fundamentals](./docs/01-rtgl-fundamentals.md) for why this behaviour matters.

## 📚 Guides & Examples

Three guides cover the language in depth, each paired with a runnable notebook:

| Guide | Notebook | Covers |
| :--- | :--- | :--- |
| [RTGL Fundamentals](./docs/01-rtgl-fundamentals.md) | [`01-standard-tasks.ipynb`](./experiments/01-standard-tasks.ipynb) | Query anatomy, conditions, aggregations, automatic multi-hop, temporal windows |
| [Common Path Expressions](./docs/02-common-path-expressions.md) | [`02-common-path-expressions.ipynb`](./experiments/02-common-path-expressions.ipynb) | Explicit join paths and ambiguity resolution |
| [SQL Injections](./docs/03-sql-injections.md) | [`03-sql-injections.ipynb`](./experiments/03-sql-injections.ipynb) | Raw SQL as a virtual table |

The [`rtgl-tasks`](https://github.com/kolesole/rtgl-tasks) repository collects full prediction tasks built with **RTGL** on real datasets.

## 🏗️ Architecture

<p align="center">
  <img src="./docs/assets/architecture.svg" alt="Architecture" width="100%">
</p>


## 🔧 Development

### Install uv

macOS and Linux:

```bash
wget -qO- https://astral.sh/uv/install.sh | sh
```

Windows:

```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Install Dependencies

```bash
uv sync --all-extras
```

### Regenerate Parser Files

After modifying the lexer or parser grammar files (`*.g4`), regenerate the ANTLR outputs from the repository root:

```bash
./regenerate_parser.sh
```

### Run Tests

```bash
pytest
```

### Run Linter

```bash
ruff check .
```

## 📄 License

**RTGL** is released under the [MIT License](./LICENSE).
