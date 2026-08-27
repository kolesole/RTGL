# RTGL Fundamentals

This guide covers everything you need to write and understand standard **RTGL (Relationa Task Generation Language)** queries: query anatomy, conditions, aggregations, automatic multi-hop resolution, and temporal window rules.
It pairs with [`experiments/01-standard-tasks.ipynb`](../experiments/01-standard-tasks.ipynb), where every query is executed against a real dataset and checked, label for label, against its **RelBench** reference task.

## Table of Contents

- [What RTGL Is](#what-rtgl-is)
- [Query Anatomy](#query-anatomy)
- [Conditions & Operators](#conditions--operators)
- [Aggregation Functions](#aggregation-functions)
- [Temporal Window Rules](#temporal-window-rules)
- [Automatic Multi-Hop](#automatic-multi-hop)

## What RTGL Is

**Relational Deep Learning** tasks are usually defined by hand: pick an entity table, pick a prediction timestamp, join in the relevant related tables within some time window, aggregate a label - and then write that logic again, from scratch, for the next task.

**RTGL** is a declarative, SQL-like language that replaces that boilerplate.
You declare *what* to predict and *for whom*; RTGL compiles the query to SQL, optionally executes it, and returns the result.

```sql
-- for every user, count how many posts
-- they will place in the 30 days
-- after each prediction timestamp
PREDICT COUNT(posts.*, 0, 30, DAYS)
FOR EACH users.*;
```

Notice what the query does *not* say: nothing about how `posts` reaches `users`.
**RTGL** works that out from the schema itself - see [Automatic Multi-Hop](#automatic-multi-hop).

## Query Anatomy

Every RTGL query is either **static** or **temporal**.
A static query produces one label per entity, independent of time; a temporal query is evaluated at a set of prediction timestamps and produces one label per `(entity, timestamp)` pair.
The two share a skeleton but differ in which clauses they admit, as shown below.

<table>
  <tr>
    <th width="10%" align="center">Type</th>
    <th width="90%" align="center">Anatomy</th>
  </tr>
  <tr>
    <td align="center" valign="middle"><b>Static</b></td>
    <td valign="middle">

```sql
[WITH <common_path_expr> (, <common_path_expr>)*]
PREDICT <aggregation | expression | table.column> [RANK TOP K | CLASSIFY]
FOR EACH <entity_table>.<primary_key>
[WHERE <static_condition | static_nested_expression>];
```

  </td>
  </tr>
  <tr>
    <td align="center" valign="middle"><b>Temporal</b></td>
    <td valign="middle">

```sql
[WITH <common_path_expr> (, <common_path_expr>)*]
PREDICT <aggregation | temporal_expression> [RANK TOP K | CLASSIFY]
FOR EACH <entity_table>.<primary_key>
[WHERE <static_condition | static_nested_expression>] -- filters entities
[WHERE <temporal_condition | temporal_nested_expression>] -- filters (fk, timestamp) pairs
[ASSUMING <temporal_condition | temporal_nested_expression>];
```

  </td>
  </tr>
</table>

The sections below walk through those clauses in the order they appear.

### WITH

Optional, and available in both query types.
It declares one or more **CPEs (Common Path Expressions)**: named, explicit join paths that can afterwards be referenced like ordinary tables.
CPEs only become necessary once automatic path resolution runs out of road, so they have a guide of their own - see [Common Path Expressions](./02-common-path-expressions.md).

### PREDICT

Required in both query types.
This is where you declare *what* to predict; whatever it evaluates to becomes the `label` column of the result.

A **static** query offers three options: an *\<aggregation>*, an *\<expression>* (a condition, which yields a boolean label), or a bare *\<table>.\<column>*.
A **temporal** query offers two: an *\<aggregation>* or a *\<temporal_expression>*.
A bare *\<table>.\<column>* is not allowed in the temporal case, because a temporal label has to be tied to a time window, and a raw column value has no window to be evaluated over.

Both types accept a trailing `RANK TOP K` or `CLASSIFY` modifier, but only directly after an aggregation - and specifically only after `LIST_DISTINCT`, since it is the only function that produces a list to modify.
Attaching either modifier to any other aggregation is a validation error.

- `RANK TOP K` truncates the collected list to its first `K` elements (`K` must be a positive integer).
- `CLASSIFY` keeps the full list.

### FOR EACH

Required in both query types, and the counterpart to `PREDICT`: it defines *for whom* the label is computed.
It takes a *\<table>.\<column>* reference, where *\<column>* is either the table's primary key or `*` (equivalent in this context).

The entity table must declare a `pkey_col`, and its values become the `fk` column of the result.

In a temporal query the entity table's `time_col`, if it has one, additionally acts as a mask - **temporal masking**.
An entity appears only at timestamps at or after its own time value, so a user is never predicted for before they registered.
This is what keeps generated tasks free of label leakage without any extra work on your part.

### Static WHERE

Written directly after `FOR EACH` and available in both query types, the static `WHERE` filters *which entities* the query predicts for, before any label is computed.

Its subject can be a bare *\<table>.\<column>* or a static *\<aggregation>*:

```sql
FOR EACH posts.*
WHERE posts.OwnerUserId IS NOT NULL
  AND COUNT(references.*) > 5;
```

Note that each condition pairs one subject with exactly one operator.
To express several constraints, combine conditions with `AND`/`OR`.

### Temporal WHERE

Temporal queries only, and written after the static `WHERE`.
Rather than filtering entities, it filters `(fk, timestamp)` pairs, looking *backward* from each prediction timestamp - which is why its window must be non-positive.

Unlike the static form, its subject must be an *\<aggregation>*; a bare *\<table>.\<column>* is not allowed.

For example, to keep only posts that already had more than five references in the preceding three months:

```sql
WHERE COUNT(references.*, -91, 0, DAYS) > 5
```

### ASSUMING

Temporal queries only, and always the last clause.
Like the temporal `WHERE`, it filters `(fk, timestamp)` pairs and requires an *\<aggregation>* as its subject - but it looks *forward*, so its window must be non-negative.

The difference between the two is one of intent: the temporal `WHERE` conditions on what has already happened, while `ASSUMING` conditions on what is going to happen.
The latter is the usual way to restrict a task to entities that stay active across the label window.

For example, to keep only posts that will accumulate more than five references in the next three months:

```sql
ASSUMING COUNT(references.*, 0, 91, DAYS) > 5
```

### What Counts as a *\<table>*

Wherever the grammar expects a *\<table>*, three things are accepted: the name of a real table in the `Database`, a **CPE** alias, or an inline **SQL injection** (see [SQL Injections](./03-sql-injections.md)).

Note: A **CPE** alias cannot be used as the `FOR EACH` source - that clause requires a direct table reference, and RTGL rejects anything else during validation.

## Conditions & Operators

A condition compares a subject - an *\<aggregation>* or a *\<table>.\<column>* reference - against a literal value.
There are three kinds of condition, each with its own operator set and its own expected literal type:

| Kind | Operators | Notes |
| :--- | :--- | :--- |
| Numeric | `>` `>=` `<` `<=` `==` `!=` | Compares against an `INT`, `FLOAT`, or `DATETIME` literal (`YYYY-MM-DD HH:MM:SS`). |
| String | `CONTAINS` `NOT CONTAINS` `LIKE` `NOT LIKE` `STARTS WITH` `ENDS WITH` `=` | Compares against a quoted string. Equality uses a single `=`, not `==` - the latter is the numeric operator. |
| Null Check | `IS NULL` `IS NOT NULL` | Takes no right-hand side. |

Conditions combine with `AND`/`OR` and can be grouped with parentheses; `NOT` negates a single condition.
Precedence runs `OR` < `AND` < *\<condition>*, so parentheses are the way to override the default grouping:

```sql
WHERE COUNT(references.*) > 5
   OR (NOT posts.title CONTAINS "draft"
   AND posts.ownerId IS NOT NULL)
```

## Aggregation Functions

Nine aggregation functions are supported.
Each takes a *\<table>.\<column>* and, in a temporal query, a time window:

```sql
AVG(table.column [, start, end, UNIT])
COUNT(table.column [, start, end, UNIT])
COUNT_DISTINCT(table.column [, start, end, UNIT]) -- count distinct values
FIRST(table.column [, start, end, UNIT]) -- earliest by the table's time column
LAST(table.column [, start, end, UNIT]) -- latest by the table's time column
LIST_DISTINCT(table.column [, start, end, UNIT]) -- collect distinct values into a list
MAX(table.column [, start, end, UNIT])
MIN(table.column [, start, end, UNIT])
SUM(table.column [, start, end, UNIT])
```

The window is present only in temporal queries; a static aggregation covers every related row, with no notion of time.

Independently of the window, every aggregation can narrow the rows it consumes with a nested static `WHERE`, applied before the values are aggregated:

```sql
COUNT(references.* WHERE references.type == 1, 0, 91, DAYS)
```

If that nested `WHERE` references any table other than the aggregation's own or any aggregation, the aggregated table must declare a primary key - RTGL needs it to join the filtered rows back.

### Entities With Zero Related Rows

An entity may end up with no related rows in scope at all - either because none exist, or because none fall inside the window.
What happens next depends on the function, and holds for static and temporal queries alike:

| Function | Entity with zero related rows |
| :--- | :--- |
| `COUNT`, `COUNT_DISTINCT`, `SUM` | Label is `0`; the entity still appears in the result. |
| `AVG`, `MIN`, `MAX`, `FIRST`, `LAST`, `LIST_DISTINCT` | Label would be `NULL`, so the entity is dropped from the result entirely. |

## Temporal Window Rules

A temporal window `(start, end, UNIT)` covers the half-open interval **`(ts + start, ts + end]`** - exclusive of the start boundary, inclusive of the end - where `ts` is the prediction timestamp of the row being computed.
The `UNIT` is one of `SECONDS`, `MINUTES`, `HOURS`, `DAYS`, `WEEKS`, `MONTHS`, or `YEARS`.

The sign of `start` and `end` is constrained by the clause the aggregation appears in, which is simply the language enforcing the direction each clause is meant to look:

| Clause | Direction | Required sign |
| :--- | :--- | :--- |
| `PREDICT` | forward | `start >= 0`, `end >= 0` |
| `WHERE` (temporal) | backward | `start <= 0`, `end <= 0` |
| `ASSUMING` | forward | `start >= 0`, `end >= 0` |

Two further rules apply everywhere: `start` must be strictly less than `end`, and `-inf`/`+inf` are valid bounds for an unbounded window (useful, for example, to mean "at any point before now" in a backward-looking `WHERE`).

Finally, a temporal aggregation needs something for its window to apply to.
Either its own table, or some intermediate table on the path to the `FOR EACH` entity, must have a time column - if none does, RTGL rejects the query.

## Automatic Multi-Hop

As the opening example hinted, standard RTGL queries never say *how* two tables connect.
**RTGL** derives that from the foreign keys declared on `Table` objects, walking the schema to find the **shortest path of foreign keys** between the aggregated table and the entity table.
That chain can be of any length, and it may traverse foreign keys in either direction.

### Resolution Outcomes

What RTGL does next depends on how many shortest paths it finds:

| Paths found | Behaviour |
| :--- | :--- |
| Exactly one | Resolved - nothing to do. |
| Several, of **different** lengths | **Warning**: the shortest is used, and RTGL reports which route it picked. |
| Several, of the **same** length | **Error**: RTGL refuses to guess and rejects the query as ambiguous. |
| None | **Error**: the two tables are not connected. |

The warning case is usually benign, but it is worth reading rather than dismissing: if the route RTGL picked is not the one you had in mind, the query will run and quietly compute the wrong label.

### Temporal Queries Search Differently

In a temporal query, RTGL considers only paths that pass through **at least one table with a time column** (the entity table itself does not count), because the time window needs something to apply to.

This has a consequence worth internalising: **the same two tables can resolve to different paths in a static and a temporal query over the same schema.**
A short route through time-less lookup tables is valid statically, but is skipped in the temporal case in favour of a longer, time-aware one.

### When Automatic Resolution Is Not Enough

When the schema alone cannot settle the question, two escape hatches are available, and they address different problems.

**[Common Path Expressions](./02-common-path-expressions.md)** name the exact route explicitly and let you use it like a table.
This is the right tool when the problem is purely *which* declared foreign keys to follow - an ambiguous tie between equally short paths, or a deliberate preference for a route other than the shortest.

**[SQL Injections](./03-sql-injections.md)** drop raw SQL in as a virtual table.
These are needed when the relationship is not declared as a foreign key at all, or when the logic exceeds what the grammar can express.
