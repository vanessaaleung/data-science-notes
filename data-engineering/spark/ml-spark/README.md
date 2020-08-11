# Machine Learning & Spark

## Data RAM
- The computer will start to use *virtual memory* and the data will be *paged* back and forth between RAM and disk.
- Retrieving data from disk is slow relative to RAM
- Solution: distribute data among clusters, each data partition can fit into RAM on a single computer in the cluster

## Spark Architecture
- Spark: does most processing in-memory
- Cluster: consists of one or more nodes
- Node: is a computer with CPU, RAM, and physical storage
- Executor: on each node, Spark launches an executor process and work is divided into tasks. The executors run tasks in multiple threads across the cores in a node
- Cluster Manager: allocates resources and coordinates activity across the cluster

## Connecting to Spark
```python
import pyspark
```
- sub-modules
  - Structured Data: `pyspark.sql`
  - Streaming Data: `pyspark.streaming`
  - Machine Learning: `pyspark.mllib` (unstructured representation of data in RDD, deprecated) and `pyspark.ml` (structured, tabular representation of data in DataFrames)
  
- Spark URL
  - Remote cluster: `spark://<IP address | DNS name>:<port>`
  - Local Cluster: 
    - `local` - only 1 core
    - `local[4]`: 4 cores
    - `local[*]`: all available cores

- Creating a SparkSession
```python
from pyspark.sql import SparkSession
# create a local cluster
spark = SparkSession.builder \
                    .master('local[*]`) \
                    .appName('first_spark_application') \
                    .getOrCreate()   # create or return an existing

# stop session
spark.stop()
```
## Loading Data
- Methods
  - `count()`: number of rows
  - `show()`: display rows
  - `printSchema()`
  - `dtypes`

- Read from csv
  ```python
  flights = spark.read.csv('flights.csv',
                         sep=',',
                         header=True,
                         inferSchema=True,
                         nullValue='NA')
  ```
  - sep: field seperator
  - schema: explicity column data types
  - inferSchema: deduce data types from data
  - nullValue: placeholder for missing data

## Data Preparation
- Dropping columns
  ```python
  cars = cars.drop('xxx')
  # or select those wanted
  cars = cars.select('xxx')
  ```
- Filter out missing values
  ```python
  cars.filter('cyl IS NULL')
  # or more aggressive
  cars = cars.dropna()
  ```
- Mutating columns
  ```python
  cars = cars.withColumn('newColumn', xxx)
  ```
- Indexing Categorical Data
  - index are assigned according to the descending relative frequency of each of the string values, i.e. most common one gets zero
  - `stringOrderType`: to change order
  ```python
  from pyspark.ml.feature import StringIndexer
  indexer = StringIndexer(inputCol='type', outputCol='type_idx')
  # Indexer identifies categories in the data
  indexer = indexer.fit(cars)
  # Indexer creates a new column with numeric index values
  cars = indexer.transform(cars)
  ```
- Assembling columns
  - ML algorithms in Spark operate on a single vector of operators
  ```python
  from pyspark.ml.feature import VectorAssembler
  
  assembler =VectorAssembler(inputCols=['col1', 'col2'], outputCol='features')
  assembler.transform(cars)
  ```
## Pipeline
### Leakage
- should only fit training data

### Pipelin
_Consists of a series of operations_

```python
from pyspark.ml import Pipeline
pipeline = Pipeline(stages=[indexer, onehot, assemble, regression])
pipeline = pipeline.fit(train)
predictions = pipeline.transform(test)
```
- Access stages in pipeline
```python
pipeline.stage[3]
```


