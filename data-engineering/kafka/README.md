# Kafka
_A event streming platform, distributed system_

- [Official Intro](https://kafka.apache.org/intro)

## Event
_Recrods that something happened_
- key
- value
- timestamp
- optional metadata
- example
```text
Event key: "Alice"
Event value: "Made a payment of $200 to Bob"
Event timestamp: "Jun. 25, 2020 at 2:06 p.m."
```

## Event Streaming
_Ensures a continuous flow and interpretation of data so that right information is at the right place, right time_
- **Capturing** (write/read) data in real-time from event sources like databases, sensors, mobile devices
- **Storing** these event streams durably for later retrieval
- Manipulating, **processing**, and reacting to evernt streams in real-time/retrospectively
- **Routing** event streams to different destination technologies

## Servers and Clients
- Servers: Kafka is run as a cluster of one of more servers
  - some of these servers form the storage layer - brokers
  - Fault-tolerant: if any servers fails, others will take over the work
- Clients: allow to write distrubted applications that read/write/process event streams in parallel

## Producer and Consumer
- Producers: client applications that write events to Kafka
- Consumers: those subscribe (read/process) events
- two are fully decoupled

## Topic
_Events are organized and stored in topics, simliar to a folder_
- Multi-producer, multi-subscriber
- Can define how long Kafka should retain events through a per-topic configuration
- **Partitioned**: a topic is spread over a number of buckets located on different brokers
  - Scalability: allows to read and write data from/to many brokers at the same time
  - Events with the same key (e.g. customer ID) are written to the same partition
  - A new event is appened to one of the topic's partitions
  
  <img src="https://kafka.apache.org/images/streams-and-tables-p1_p4.png" height="300px">
- Can be **replicated** across regions/datacenters
  - Common production setting is a replication factor of 3: three copies of data
