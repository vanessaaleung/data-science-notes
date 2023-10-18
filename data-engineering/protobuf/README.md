# Protobuf

## Protobuf VS Avro
- Avro:
  - Compresses data, efficient with large files
  - Read fields without knowing the whole schema
- Protobuf
  - Efficient with smaller batches of data
  - Backwards schema compatibility
  - All fields optional

## Why not Avro
- Avro: Not schema attached to the message. When rolling out a new schema version on the producer end, it doesn't also get updated on the consumer end, which confuses the consumer/consumer failing to map the message to the old schema.
- Protobuf: includes field position
