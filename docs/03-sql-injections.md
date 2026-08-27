# SQL Injections

An **SQL injection** is **RTGL**'s escape hatch: you drop a raw SQL query in anywhere a table is expected, declare its keys by hand, and RTGL treats the result as a **virtual table** — joinable, filterable, and aggregatable exactly like a real one.
It is the tool you reach for when neither the schema nor the grammar can express what the task needs.

This guide covers the syntax, how an injection is referenced from the rest of a query, the situations that call for one, and the case where a **CPE** is the better answer.
It pairs with [`experiments/03-sql-injections.ipynb`](../experiments/03-sql-injections.ipynb), where every query is executed against a real dataset and checked, label for label, against its **RelBench** reference task.

See [RTGL Fundamentals](./01-rtgl-fundamentals.md) for the base query grammar.

## Table of Contents

- [What an SQL Injection Is](#what-an-sql-injection-is)
- [Syntax](#syntax)
- [Referencing an Injection](#referencing-an-injection)
- [Use Cases](#use-cases)
- [When a CPE Is the Better Tool](#when-a-cpe-is-the-better-tool)

## What an SQL Injection Is

RTGL's grammar and its [automatic multi-hop resolution](./01-rtgl-fundamentals.md#automatic-multi-hop) cover the large majority of predictive workflows, and while they do, an injection would add nothing.

Real relational data, however, is rarely as tidy as the schema suggests.
Sometimes the relationship you need to traverse was never declared as a foreign key, even though it exists in the data.
Sometimes the label calls for a statistical function RTGL does not expose, or for logic that simply does not fit the shape of a single `PREDICT` clause.
An **SQL injection** answers all three by letting you write that fragment yourself.

The declaration has two halves, and the split is the whole idea:

- The **body** - a raw SQL query - produces the rows.
- The **metadata** - a fixed sequence of brace-delimited slots - tells RTGL how those rows relate to the rest of the database.

Under the hood, each injection is compiled into a **CTE (Common Table Expression)** in the generated SQL, and its declared metadata is attached to an internal `Table` descriptor.
From that point on, path resolution, temporal windowing, and temporal masking treat the injection exactly as they treat a table read from the `Database`.

Note: The raw SQL inside the **injection body** is not validated during RTGL's conversion phase. 
Any syntax errors will only be caught by the underlying database engine at execution time.

## Syntax

An injection is a raw SQL query enclosed in square brackets, followed by the metadata RTGL needs in order to treat its result as a table:

```sql
[<sql_body>] -- required
{<table_name>} -- required
{<pkey_col>} -- required slot, may be left empty
{<fkey_col> -> <parent_table>, ...} -- required slot, may be left empty
{<other_table>.<fkey_col>, ...} -- required slot, may be left empty
{<time_col>} -- temporal queries only; required slot, may be left empty
```

Each brace fills one fixed slot, and the slots always appear in this order:

| Slot | Meaning |
| :--- | :--- |
| *\<sql_body>* | Your raw SQL query. |
| *\<table_name>* | The name this result is exposed under, usable as *\<table_name>.\<column>* anywhere else in the query. |
| *\<pkey_col>* | This result's primary key column. Required only if some *other* table declares a foreign key pointing *into* this injection, or if the injection is itself the `FOR EACH` source. |
| *\<fkey_col> -> \<parent_table>*, ... | Columns in the `SELECT` that are foreign keys, and the table each one references. |
| *\<other_table>.\<fkey_col>*, ... | Columns in *other* tables that reference this injection's primary key. |
| *\<time_col>* | This result's time column. Required whenever the injection is aggregated over in a temporal query. |

Two rules govern how the braces are written.

First, every brace is a **positional** slot and must be present even when its contents are empty - `{}` is how you say "no primary key" or "no incoming foreign keys".

Second, the *\<time_col>* slot is the one exception to that rule: in a **static** query it is dropped entirely.
A static injection therefore carries **four** braces and a temporal one carries **five**.

## Referencing an Injection

Because an injection is a table as far as the rest of the query is concerned, the column reference attaches directly to the closing brace, exactly where *\<table>.\<column>* would otherwise appear:

```sql
PREDICT COUNT(
    [SELECT 
        * 
     FROM 
        reviews 
     WHERE 
        rating >= 4
    ]{high_rated_reviews}
    {}
    {productId->products}
    {}.reviewId)
FOR EACH products.productId;
```
Since this is a static query, only four braces appear.

The temporal form adds the *\<time_col>* slot, after which the usual window arguments follow the column:

```sql
PREDICT COUNT(
    [SELECT 
        * 
     FROM 
        reviews 
     WHERE 
        rating >= 4
    ]{high_rated_reviews}
    {}
    {productId->products}
    {}
    {date}.reviewId, 0, 91, DAYS)
FOR EACH products.productId;
```

Note: Declare only the foreign keys the query actually needs.

## Use Cases

The sections below cover the situations where injections are useful.
They share a pattern worth noticing: in each one, the obstacle is not that RTGL computes the wrong thing, but that the query cannot be *stated* at all.

### An Undeclared Foreign Key

Every hop in a **CPE** is checked against the schema's declared foreign keys and rejected if the relationship was never declared - no sequence of hops can express a join RTGL does not know exists.
An injection sidesteps this by declaring the missing edge itself.

### SQL Functions RTGL Does Not Support

RTGL offers `AVG`, `COUNT`, `COUNT_DISTINCT`, `FIRST`, `LAST`, `LIST_DISTINCT`, `MAX`, `MIN`, and `SUM` - but nothing for the most frequent value in the window or to use simple scalar function (e.g., `LENGTH`).
Where SQL provides such a function, the injection body can compute it and expose the result as an ordinary column.

### Only One Aggregation per Clause

RTGL computes exactly one aggregation per `PREDICT` clause or condition.
Consequently, there is no way to compute a per-child aggregation and then aggregate that again at the parent level without an SQL Injection.

### Multi-Hop Paths Over-Constrained by Time

This last case is subtler than the others, because nothing about the query looks wrong.
A path can be entirely unambiguous - no competing routes, no missing foreign keys - and still compute an unintended label in a temporal query, if more than one table along the way carries its own time column.

The reason is that RTGL applies the requested window to **every** time-columned table on the path, not only to the one you had in mind.
Each additional time column narrows the result further, and the label quietly reflects the intersection of all of them.

## When a CPE Is the Better Tool

An injection is not automatically the stronger option just because it is the lower-level one.
When the relationship you need *is* already declared and the difficulty is only *which* declared edges to follow, a **CPE** states the answer directly, while an injection has to encode it twice - once in the join, once in the metadata.

The [`post-post-related`](../experiments/03-sql-injections.ipynb#post-post-related) task is the clearest illustration.
It asks which existing posts users will link a given post to, which means relating `posts` to itself through the `postLinks` bridge table:

```mermaid
flowchart LR
    P1(["📝 posts (source)"])
    P2(["📝 posts (target)"])

    L("🔗 postLinks")

    P1 -->|PostId| L
    L -->|RelatedPostId| P2

    classDef highlightTable fill:#ecfdf5,stroke:#10b981,stroke-width:2px,color:#047857,font-weight:bold

    class P1,P2,L highlightTable

    linkStyle 0,1 stroke:#10b981,stroke-width:3px
```

*Both foreign keys of `postLinks` point at the same table, so the route has to be named rather than searched for.*

The task hinges on disambiguating the two foreign keys `postLinks` declares into `posts` - `PostId` and `RelatedPostId` - which a CPE does cleanly by naming the exact hops; see [`02-common-path-expressions.ipynb`](../experiments/02-common-path-expressions.ipynb#post-post-related).

An injection attempting the same disambiguation runs into a circular problem:

- To let RTGL join the injection to `posts` at all, you must declare the edge you traverse, `PostId->posts`.

- The collected column, `RelatedPostId`, also points at `posts`, and declaring that relationship is what tells a `LIST_DISTINCT` label it is a reference into `posts`.

- Declaring both, however, recreates the exact pair of equally short paths that made the task ambiguous.

Declaring only the edge you join on does avoid the error and computes the right values - but the returned `Table` then loses the label's foreign-key annotation, so the result is no longer self-describing as a link-prediction task.
