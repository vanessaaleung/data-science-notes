# Singer
_Open-source standard/specification for writing scripts that move data_

<p align="center">
  <img src="https://images.ctfassets.net/fi0zmnwlsnja/34ci8cjJN1evEENDyxD5hT/2cc4bc14208d7916f14b8c0ab959d6df/singer_logo.png?w=636&h=272&q=50&fit=fill" height="200px">
</p>

## Introduction
- data exchange format: JSON
- extract with taps and load with targets
  - language independent
### Communicate over Streams
_A "named" virtual location to which you send messages that can be picked up at a downstream location_

<img src="https://assets.datacamp.com/production/repositories/4724/datasets/f8d3f4cb1e70bc022d9a592c5dcfafc44d29efdb/singer_tap_target_full.png" height="300px">
  
- schema (metadata): annotate and validate structured data by specifying data type or import constraints
  ```python
  json_schema = (
    "properties": {"age": {"maximum": 130,
                            "minimum": 1,
                            "type": "integer"}},
    "$id": "xxx",
    "$schema": "xxx"}
  )
  ```
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
- transforms the object to a stringg
```python
import json
json.dumps(json_schema["properties"]["age"])
```
- write the string to a file
```python
with open("foo.json", mode="w") as fh:
  json.dump(obj=json_schema, fp=fh)
```
