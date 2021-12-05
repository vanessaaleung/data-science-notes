# Data Engineering

<p align="center">
  <img src="https://miro.medium.com/max/3840/0*hmFg5WnkeqLcRLjA.jpg" height="300px">
</p>

- [Database](https://github.com/vanessaaleung/data-science-notes/tree/master/data-engineering/database)
- [Object Oriented Programming](https://github.com/vanessaaleung/data-science-notes/tree/master/data-engineering/object-oriented-programming)
- [Algorithms](https://github.com/vanessaaleung/data-science-notes/tree/master/data-engineering/algorithms)
- [Airflow](https://github.com/vanessaaleung/DS-notes/tree/master/data-engineering/airflow)
_A platform to program workflows_

- [Spark](https://github.com/vanessaaleung/DS-notes/tree/master/data-engineering/spark)
_A fast and general engine for large-scale data processing_

- [Singer](https://github.com/vanessaaleung/DS-notes/tree/master/data-engineering/singer)
_A open-source standard/specification for writing scripts that move data_

- [Dataflow](https://github.com/vanessaaleung/DS-notes/tree/master/data-engineering/dataflow)
_A Google Cloud Platform ETL tool_

- [MapReduce](#mapreduce)
- [Process vs Thread](#process-vs-thread)


## MapReduce
1. splits the input data-set into independent chunks which are processed by the map tasks in a completely **parallel** manner
2. **sorts** the outputs of the maps, which are then input to the reduce tasks

- Why:
  - for applications which process vast amounts of data (multi-terabyte data-sets) 
  - in-parallel on large clusters (thousands of nodes)
  - fault-tolerant
  
- The total number of partitions is the same as the number of reduce tasks for the job
- Users can control which keys (and hence records) go to which Reducer by implementing a custom Partitioner

## Process vs Thread
- Process: an executing program. An application consists of one or more processes
- Thread: One or more threads run in the context of the process. A thread is the basic unit to which the operating system allocates processor time
