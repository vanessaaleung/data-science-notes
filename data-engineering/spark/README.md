# Spark
_A fast and general engine for large-scale data processing_

<p align="center">
  <img src="https://open-dse.github.io/assets/images/ekhtiar/spark.png" width="300px">
</p>

1. Basic Intro
2. Data Cleaning
3. Transforming Data
4. Packaging Application
5. Testing

## Basic Intro
- 4 libraries built on top of Spark core
  - Spark SQL
  - Spark Streaming
  - MLlib
  - GraphX
- Used for
  - Process data at scale by parallelizing execution over multiple machines
  - Interactive analytics in notebook format
  - Machine Learning
- Starting Spark
  ```python
  from pyspark.sql import SparkSession

  spark = SparkSession.builder.getOrCreate()
  ```
- Read CSV Files
  - Actual execution is postponed until performing an action on the dataframe like `.show()`
  ```python
  prices = spark.read.options(header="true").csv('file_path')
  prices.show()
  ```
- Enforcing a Schema
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
  - default mode is `"PERMISSIVE"`
- Fill missing data
  ```python
  prices.fillna(25, subset=[col])
  ```
- Conditionally Replacing Values with `when`
  ```python
  employees.withColumn('end_date', when(col('end_date') > one_year_from_now, None)
           .otherwice(col('end_date'))
  ```

## Transforming Data
- Filtering rows
  - Function `col` creates Column objects
  ```python
  prices.filter(col('country') == 'BE')
  ```
- Selecting and renaming columns with `select` and `alias`
  ```python
  prices.select(col("store"), 
                col("brand").alia("brandname"))
        .distinct())
  ```
- Grouping and aggregation with `groupBy`
  ```python
  prices.groupBy(col('brand')).mean('price')
  ```
  ```python
  prices.groupBy(col('brand'))
        .agg(avg('price'), count('brand'))
  ```
- Joining with `join`
  ```python
  ratings.join(prices, ['brand', 'model'])
  ```
- Ordering with `orderBy`
  ```python
  prices.orderBy(col('date'))
  ```
## Packaging Application
- run with python
```shell
python script.py
```
- use spark-submit to launch a job
  - sets up launch environment for use with the cluster manager and the selected deploy mode
  ```shell
  spark-submit \
    --master "local[*]" \ # tells Spark where it can get resources from 
    --py-files PY_FILES \ # copy Python modules to all nodes
    --MAIN_PYTHON_FILE \ # tells Spark the entry point of the application (the main file)
    app_arguments  # optional arguments parsed by the main script
  ```
- Collecting all dependencies in one archive
  ```shell
  zip \
    --recurse-paths \    # recursively add all files in all subfolders
    dependencies.zip \   # name of the resulting archive
    pydiaper
  ```
  ```shell
  spark-submit \
    --py-files dependencies.zip \
    --pydiaper/cleaning/clean_prices.py
  ```
  
## Testing
### Test Pyramid
- Unit Testing: test pieces of code that don't rely on external dependencies
- Integration/Service Test
  - interaction with file systems and databases, slower
  - tests the interaction between a few services
- UI test
  - Closest to end-user experiences
  - Most difficult to debug
  - Combine the services of many systems
  
### Write a Unit Test
- Inputs are clear, create in-memory DataFrames makes testing easier
- Data is close to where it is being used ("code-proximity")
- Create small, resuable and well-named functions
- `assertDataFrameEqual()`

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
