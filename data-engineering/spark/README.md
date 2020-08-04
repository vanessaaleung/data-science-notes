# Spark

1. [Performance Tuning]()

## Performance Tuning
- Caching Data In Memory
- Other Configuration Options
- Join Strategy Hints for SQL Queries
- Coalesce Hints for SQL Queries
- Adaptive Query Execution
  - Coalescing Post Shuffle Partitions
  - Converting sort-merge join to broadcast join
  - Optimizing Skew Join

### Caching Data In Memory
Spark SQL can cache tables using an in-memory columnar format by calling `spark.catalog.cacheTable("tableName")` or `dataFrame.cache()`. Then Spark SQL will scan only required columns and will automatically tune compression to minimize memory usage and GC pressure (garbage collector pressure). You can call `spark.catalog.uncacheTable("tableName")` to remove the table from memory.

### Other Configuration Options
### Join Strategy Hints for SQL Queries
### Coalesce Hints for SQL Queries
### Adaptive Query Execution
### Coalescing Post Shuffle Partitions
### Converting sort-merge join to broadcast join
### Optimizing Skew Join
