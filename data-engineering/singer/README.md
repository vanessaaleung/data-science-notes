# Singer
_Open-source standard/specification for writing scripts that move data_

<p align="center">
  <img src="https://images.ctfassets.net/fi0zmnwlsnja/34ci8cjJN1evEENDyxD5hT/2cc4bc14208d7916f14b8c0ab959d6df/singer_logo.png?w=636&h=272&q=50&fit=fill" height="200px">
</p>

1. [Introduction](#introduction)
2. [Running An Ingestion Pipeline with Singer](#running-an-ingestion-pipeline-with-singer)

## Introduction
Singer describes how data extraction scripts(**taps**) and data loading scripts(**targets**) should communicate, allowing them to be used in any combination to move data from any source to any destination like databases, web APIs, files, queues, etc..

- need to install tap and target in two different envs
```Shell
› pip install target-csv tap-exchangeratesapi
› tap-exchangeratesapi | target-csv
INFO Replicating the latest exchange rate data from exchangeratesapi.io
INFO Tap exiting normally
› cat exchange_rate.csv
AUD,BGN,BRL,CAD,CHF,CNY,CZK,DKK,GBP,HKD,HRK,HUF,IDR,ILS,INR,JPY,KRW,MXN,MYR,NOK,NZD,PHP,PLN,RON,RUB,SEK,SGD,THB,TRY,ZAR,EUR,USD,date
1.3023,1.8435,3.0889,1.3109,1.0038,6.869,25.47,7.0076,0.79652,7.7614,7.0011,290.88,13317.0,3.6988,66.608,112.21,1129.4,19.694,4.4405,8.3292,1.3867,50.198,4.0632,4.2577,58.105,8.9724,1.4037,34.882,3.581,12.915,0.9426,1.0,2017-02-24T00:00:00Z
```

- data exchange format: JSON
- extract with taps and load with targets
  - language independent
### Communicate over Streams
_A "named" virtual location to which you send messages that can be picked up at a downstream location_

<img src="https://assets.datacamp.com/production/repositories/4724/datasets/f8d3f4cb1e70bc022d9a592c5dcfafc44d29efdb/singer_tap_target_full.png" height="300px">
  
- schema (metadata): annotate and validate structured data by specifying data type or import constraints
  - Complete the JSON schema
  ```python
  json_schema = (
    "properties": {"age": {"maximum": 130,
                            "minimum": 1,
                            "type": "integer"}},
    "$id": "xxx",
    "$schema": "xxx"}
  )
  ```
  - Write the schema
    - `stream_name="xxx"`: data that belongs together should be sent to the same stream
    - `key_properties=["id"]`: a list of strings that make up the primary key for records from the stream
  ```python
  import singer
  singer.write_schema(schema=json_schema,
                      stream_name="xxx",   
                      key_properties=["id"])
  ```
- state (process metadata)
- record (data)

### Serializing JSON
- many configuration files in Singer hold JSON
- transforms the object to a stringg
```python
import json
json.dumps(json_schema["properties"]["age"])
```
- write the string to a file
```python
# Open the configuration file in writable mode
with open("foo.json", mode="w") as fh:
  # Serialize ``obj`` as a JSON formatted stream to ``fp``
  json.dump(obj=json_schema, fp=fh)
```

## Running An Ingestion Pipeline with Singer
### Streaming record messages
- with `write_record`
```python
columns = ("id", "name", "age", ...)
users = {"(1, "Adrian", 32, False),
            ...}
singer.write_record(stream_name="xxx",
                    record=dict(zip(columns, users.pop())))
```
```shell
{"type": "RECORD", "stream": "xxx", "record": {"id":1, "name": "Adrian", ...}}
```
- or
```python
fixed_dict = {"type": "RECORD", "stream": "xxx"}
record_msg = {**fixed_dict, "record": dict(zip(columns, users.pop()))}
```
### Chaining taps and targets
```python
import singer

singer.write_schema(stream_name="xxx", schema=...)
singer.write_records(stream_name="xxx", records=...)
```
- Ingestion pipelie: Pipe the tap's output into a Singer target, using the `|` symbol
  - `tap-marketing-api | target-csv`: pipe the output of the `tap-marketing-api` tap to `target-csv`
  - 
  ```shell
  tap-marketing-api | target-csv --config some_config_file
  ```
  
### Modular Ingestion Pipelines
- Each tap/target is designed to do one thing very well
```shell
my-packaged-tap | target-csv
my-packaged-tap | target-google-sheets
```

### Keeping Tracking with State Messages
- e.g. keeps track of the last record the tap reported on
|id|name|last_updated_on|
|---|---|---|
|1|Adrian|2019-06-14|
|2|Ruanne|2019-06-16|
|3|Hillary|2019-06-16|

```python
singer.write_state(value={"max-last-updated-on": some_variable}) 
```

