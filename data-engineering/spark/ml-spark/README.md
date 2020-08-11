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








