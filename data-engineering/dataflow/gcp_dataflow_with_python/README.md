# GCP Dataflow with Python

A word-counting workflow

1. Set up virtual environment
2. Get Apache Beam SDK

```pip install apache-beam[gcp]```

3. Run WordCount locally

Sample input: <a href="https://github.com/cs109/2015/blob/master/Lectures/Lecture15b/sparklect/shakes/kinglear.txt">here</a>

```
python -m apache_beam.examples.wordcount \
  --output outputs
```

To view the outputs

```more outputs*```

To exit, press the q key.

4. Run WordCount on the Dataflow service

First, define the PROJECT, BUCKET, and REGION variables:

```
PROJECT=PROJECT_ID
BUCKET=GCS_BUCKET
REGION=DATAFLOW_REGION
```
Run the pipeline:

```
python -m apache_beam.examples.wordcount \
  --region $REGION \
  --input gs://dataflow-samples/shakespeare/kinglear.txt \
  --output gs://$BUCKET/wordcount/outputs \
  --runner DataflowRunner \
  --project $PROJECT \
  --temp_location gs://$BUCKET/tmp/
```

5. View the results on GCP

6. Modifying pipeline code

so that the WordCount pipeline is not case sensitive

The original pipeline code: <a href="https://github.com/apache/beam/blob/master/sdks/python/apache_beam/examples/wordcount.py">here</a>

```
python wordcount.py --output outputs
```

7. Delete the Cloud Storage Bucket

