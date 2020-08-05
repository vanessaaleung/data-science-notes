# Building Production Pipelines in Airflow
1. [Templates](#templates)
2. [More Templates](#more-templates)
3. [Branching](#branching)
4. [Creating a Production Pipeline](#creating-a-production-pipeline)

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

- However, when using a single task instead of a loop, all entries would succeed or fail as a single task. Separate operators allow for better monitoring and scheduling of these tasks.
  
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

## Branching
_Provides conditional logic_

<img src="https://user-images.githubusercontent.com/6249654/48800846-3a19e980-ed0b-11e8-89d0-29ceba2ce2fb.png" height="200px">

- Tasks can be selectively executed / skipped
- `BranchPythonOperator`
- Takes a `python_callable` to return the next task id to follow
```python
def branch_test(**kwargs):
  if int(kwargs['ds_nodash']) % 2 == 0:
    return 'even_day_task'
  else:
    return 'odd_day_task'

branch_task = BranchPythonOperator(
  provide_context=True,   # provide access to the runtime variables and macros to the function
  python_callable=branch_text
)

branch_task >> even_day_task
branch_task >> odd_day_task
```
## Creating a Production Pipeline
### Running DAGs & Tasks
- Run a specific task
```shell
airflow run <dag_id> <task_id> <date>
```
- Run a full DAG
```shell
airflow trigger_dag -e <date> <dag_id>
```
### Operators Reminder
- BashOperator: expects `bash_command`
- PythonOperator: expects `python_callable`
- BrachPythonOperator: requires `python_callable` and `provide_context=True`, the callable must accept `**kwargs`
- FileSensor: requires `filepath`, might need `mode` or `poke_interval`

### Template Reminder
- Check which fields can use templated strings
  - run `help(<Airflow object>)`, i.e., `help(BashOperator)`
  - look for a line that referencing `templated_fields`, e.g. `('bash_command', 'env')`
