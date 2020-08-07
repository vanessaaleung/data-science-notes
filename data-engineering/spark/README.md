# Spark
_A fast and general engine for large-scale data processing_

<p align="center">
  <img src="https://open-dse.github.io/assets/images/ekhtiar/spark.png" width="300px">
</p>

## What is Spark?
- 4 libraries built on top of Spark core
  - Spark SQL
  - Spark Streaming
  - MLlib
  - GraphX
- Used for
  - Process data at scale by parallelizing execution over multiple machines
  - Interactive analytics in notebook format
  - Machine Learning
  
## Starting Spark
```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
```

## Read CSV Files
- Actual execution is postponed until performing an action on the dataframe like `.show()`
```python
prices = spark.read.options(header="true").csv('file_path')
prices.show()
```
## Enforcing a Schema
- `ByteType()`: can hold values between -128 and 127
- `ShortType()`: good for numbers within the range of [-32,768, 32,767]
- `DateType()`, `BooleanType()`, etc.

```python
schema = StructType([StructField("store", StringType(), nullable=False),
                      ...
                      ])
prices = spark.read.options(header="true").schema(schema).csv('file_path')
```

## Data Cleaning
- Implicit standards
  - Regional datetimes vs. UTC
  - Column naming conventions
- Handle Invalid Rows - remove them authomatically
  ```python
  prices = spark.read.options(mode="DROPMALFORMED").csv(...)
  ```
- Fill missing data
  ```python
  prices.fillna(25, subset=[col])
  ```
- Conditionally replace values with `when`
  ```python
  employees.withColumn('end_date', when(col('end_date') > one_year_from_now, None).otherwice(col('end_date'))
  ```
  
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
