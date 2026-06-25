# databases/neo4j

Neo4j database utilities.

## `Neo4jInterface`

A general-purpose Neo4j client wrapping the official [`neo4j`](https://neo4j.com/docs/python-manual/current/) Python driver.

### Constructor

```python
Neo4jInterface(
    password: str,
    database: str = 'neo4j',
    uri: str = 'neo4j://localhost:7687',
    username: str = 'neo4j',
)
```

### Methods

| Method | Description |
|---|---|
| `query_to_df(query)` | Runs a Cypher query and returns the results as a pandas DataFrame |
| `drop_everything()` | Deletes all nodes and relationships in the database |
| `drop_everything_by_node_type(the_type)` | Deletes all nodes of a given label and their relationships |
| `batch_it(function_to_use, list_batch)` | Executes a write transaction function over a batch; returns elapsed time in seconds |

### Example

```python
from python_tools_and_shortcuts.databases.neo4j.Neo4jInterface import Neo4jInterface

db = Neo4jInterface(password='secret')
df = db.query_to_df("MATCH (n) RETURN n.name AS name LIMIT 10")
print(df)
```

---

## `Neo4jGraphDataScienceInterface`

Extends `Neo4jInterface` with [Neo4j Graph Data Science (GDS)](https://neo4j.com/docs/graph-data-science/current/) library support, using the [`graphdatascience`](https://github.com/neo4j/graph-data-science-client) Python client.

### Constructor

Same parameters as `Neo4jInterface`.

### Methods

| Method | Description |
|---|---|
| `create_a_gds_graph_projection(graph_name, node_label, relationship_type)` | Creates (or recreates) a named in-memory GDS graph projection |
| `run_pagerank_on_gds_graph_projection(max_iterations, damping_factor)` | Runs PageRank on the current projection; results stored in `self.df_pagerank` |
| `run_label_propagation_on_gds_graph_projection()` | Runs Label Propagation on the current projection; results stored in `self.df_lpa_results` |

### Example

```python
from python_tools_and_shortcuts.databases.neo4j.Neo4jGraphDataScienceInterface import Neo4jGraphDataScienceInterface

db = Neo4jGraphDataScienceInterface(password='secret')
db.create_a_gds_graph_projection('my-graph', 'Person', 'KNOWS')
db.run_pagerank_on_gds_graph_projection()
print(db.df_pagerank)
```

### Dependencies

- `neo4j`
- `graphdatascience`
