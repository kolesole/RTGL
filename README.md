# PredQL

**PredQL** (Predictive Query Language) is a Python framework for writing compact, expressive predictive queries over relational data, especially for Relational Deep Learning.

It lets you write shorter, more expressive queries by abstracting temporal joins and complex aggregations.

## 🧠 Features

- 🎯 **ANTLR-based Parser** 
  - Lexer and parser for PredQL syntax

- 🌳 **Structured parse-tree visitor**
  - Converts parsed queries into normalized dictionaries with source positions.

- 🔍 **Semantic validation**
  - Schema-aware query validation with error reporting.

- 🔀 **Two converters**
  - 📌 `SConverter` for static prediction queries.
  - ⏰ `TConverter` for temporal prediction queries with timestamp windows.

- ⚙️ **Dual output mode**
  - `execute=False` returns generated SQL.
  - `execute=True` executes SQL and returns a `Table` object.

## ⚙️ Installation

Install PredQL via pip:

```bash
pip install predql
```

## 🚀 Quickstart

### 1. Build your database as [RelBench](https://github.com/snap-stanford/relbench) `Database` object or use simplified PredQL version 

```python
# path to classes
from predql.base import Database, Table
```

### 2. Static query with `SConverter`

```python
from predql.converter import SConverter

converter = SConverter(db)

predql_query = """
    PREDICT COUNT_DISTINCT(votes.* 
        WHERE votes.votetypeid == 2)
    FOR EACH posts.* WHERE posts.PostTypeId == 1
                       AND posts.OwnerUserId IS NOT NULL
                       AND posts.OwnerUserId != -1;
"""

# SQL only
sql_query = converter.convert(predql_query, execute=False)

# execute and get Table(fk, label)
table = converter.convert(predql_query, execute=True)
```

### 3. Temporal query with `TConverter`

```python
import pandas as pd
from predql.converter import TConverter

timestamps = pd.Series(...) # define timestamps for which prediction must be made
converter = TConverter(db, timestamps)

# also, it is possible to update prediction timestamps later without recreating converter
converter.set_timestamps(new_timestamps)

predql_query = """
    PREDICT COUNT_DISTINCT(votes.* 
        WHERE votes.votetypeid == 2, 0, 91, DAYS)
    FOR EACH posts.* WHERE posts.PostTypeId == 1
                       AND posts.OwnerUserId IS NOT NULL
                       AND posts.OwnerUserId != -1;
"""

# SQL only
sql_query = converter.convert(predql_query, execute=False)

# execute and get Table(fk, timestamp, label)
table = converter.convert(predql_query, execute=True)
```

### 4. Examples

For more comprehensive examples and use cases, check out the [`relbench_exp.ipynb`](./experiments/relbench_exp.ipynb) notebook.  
You can also check the [`predql-tasks`](https://github.com/kolesole/predql-tasks) repository for more tasks.

## 📐 Query Language

### 📌 Static query design

```sql
PREDICT <aggregation | expression | table.column> [RANK TOP K | CLASSIFY]
FOR EACH <entity_table>.<primary_key>
[WHERE <static_condition | static_nested_expression>];
```

### ⏰ Temporal query shape

```sql
PREDICT <aggregation | temporal_expression> [RANK TOP K | CLASSIFY]
FOR EACH <entity_table>.<primary_key> [WHERE <static_condition | static_nested_expression>]
[ASSUMING <temporal_condition | temporal_nested_expression>]
[WHERE <temporal_condition | temporal_nested_expression>];
```

### 🧮 Aggregations

| Function | Meaning | Condition-Compatible |
| :--- | :--- | :--- |
| `AVG` | average | ✅ |
| `MAX` | maximum | ✅ |
| `MIN` | minimum | ✅ |
| `SUM` | sum | ✅ |
| `COUNT` | non-null count | ✅ |
| `COUNT_DISTINCT` | distinct count | ✅ |
| `FIRST` | earliest value by time | ✅ |
| `LAST` | latest value by time | ✅ |
| `LIST_DISTINCT` | list of distinct values | ❌ |

### 🧭 Temporal window rules

- Window format: `<start>, <end>, <measure_unit>`.
- Supported units: `YEARS`, `MONTHS`, `WEEKS`, `DAYS`, `HOURS`, `MINUTES`, `SECONDS`.
- Window semantics are half-open: `(start, end]`.
- `PREDICT`/`WHERE`: `start` and `end` must be non-negative.
- `ASSUMING`: `start` and `end` must be non-positive.
- `start` must be strictly less than `end`.

## 🏗️ Architecture

```text
PredQL Query String
    ↓
[Lexer] -> Tokens
    ↓
[Parser] -> Parse Tree
    ↓
[Visitor] -> Structured Dictionary
    ↓
[Validator] -> Semantic Checks
    ↓
[Converter] -> SQL Query
    ↓ (optional execute=True)
[DuckDB] -> Result Table
```

## 🔧 Development

### Install uv

- macOS & Linux

```bash
wget -qO- https://astral.sh/uv/install.sh | sh
```

- Windows

```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Install dependencies

```bash
uv sync --all-extras
```

### Regenerate parser files

If you modify lexer or parser grammar files (`*.g4`), regenerate ANTLR outputs from the repo root:

```bash
./regenerate_parser.sh
```

### Run tests

```bash
pytest
```

### Run linter

```bash
ruff check .
```
