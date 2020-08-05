# Building Production Pipelines in Airflow
1. [Templates](#templates)
2. [More Templates](#more-templates)

## Templates
_Allow substituting information during a DAG run_
- Created using the `Jinja` templating language
```python
templated_command="""
  echo "Reading {{ params.filename }}"
"""

t1 = BashOperator(
  ...
  bash_command=templated_command,
  params={'filename': 'file1.txt'}
)
```

## More Templates
### More Advanced Template
```python
templated_command="""
  {% for filename in params.filenames %}
    echo "Reading {{ filename }}"
  {% endfor %}
"""

t1 = BashOperator(
  ...
  params={'filenams': ['file1.txt', 'file2.txt']}
)
```
### Variables
_Provides assorted information about DAG runs, tasks, and system configuration_
- Execution Date: `{{ ds }}`
- Execution Date, no dashes: `{{ ds_nodash }}`
- Previous Execution Date: `{{ prev_ds }}`
- Previous Execution Date, no dashes: `{{ prev_ds_nodash }}`
- DAG Object: `{{ dag }}`
- Airflow Config Object: `{{ conf }}`

### Macros
_Reference to the Airflow macros package which provides various objects/methods for Airflow templates_
- `{{ macros }}`
- `{{ macros.datetime }}`: `datetime.datetime` object
- `{{ macros.timedelta }}`: `timedelta` object
- `{{ macros.uuid }}`: Python's `uuid` object
- `{[ macros.ds_add('2020-04-15, 5) }}`: modify days from a date, this returns `2020-04-20`


