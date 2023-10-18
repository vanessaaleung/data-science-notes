# Apache Flink
- Mostly for batch processing

- [Timely streaming processing](#timely-streaming-processing)
- [Stateful streaming processing](#stateful-streaming-processing)
- [Fault tolerance](#fault-tolerance)

## Timely streaming processing
- Event time: the time that each individual event occurred on its producing device.
- Processing time: the system time of the machine that is executing the respective operation.
- Watermarks: flow as part of the data stream and carry a timestamp t.
- ![image](https://github.com/vanessaaleung/data-science-notes/assets/24954551/4979ee45-b19d-46c6-b7b2-ce646372cedc)

## Stateful streaming processing
- When an application searches for certain event patterns, the state will store the sequence of events encountered so far.
- When aggregating events per minute/hour/day, the state holds the pending aggregates.
- When training a machine learning model over a stream of data points, the state holds the current version of the model parameters.
- When historic data needs to be managed, the state allows efficient access to events that occurred in the past.

## Fault tolerance
- Stream replay
- State snapshotting

## Flink Cluster
- one JobManager + one or more Task Manager
