# Maintaining and Monitoring Airflow Workflows
1. [Airflow Sensors](#airflow-sensors)
2. [Airflow Executors](#airflow-executors)
3. [Debugging and Troubleshooting](#debugging-and-troubleshooting)

## Airflow Sensors
_An operator that waits for a certain condition to be true_
- Creation of a file, upload of a database record, response from a web request, etc.
- Can define how often to check for the condition to be true
- Are assigned to tasks
- Arguments
  - `mode`: how to check for the condition
    - `poke`: default, continue checking until complete without giving up a workder slot
    - `reschedule`: give up task slot and try again later
  - `poke_interval`: how often to wait between checks
  - `timeout`: how long to wait before failing tasks

### File Sensor
_Checks for the existence of a file at a certain location_

```python
from airflow.contrib.sensors.file_sensor import FileSensor
file_sensor_task = FileSensor(
  ...
  filepath='salesdata.csv',
  poke_interval=300
)

init_sales_cleanup >> file_sensor_task >> generate_report
```

### Other Sensors
- `ExternalTaskSensor`: wait for a task in another DAG to complete
- `HttpSensor`: request a web URL and check for content
- `SqlSensor`: run a SQL query to check for content

### Why Sensors
- Uncertain when the condition will be true
- Repeatedly run a check without adding cycles/loops to the DAG

## Airflow Executors
### What is an Executor?
- Run tasks
- Different executors handle running the tasks differently
- `SequentialExecutor`, `LocalExecutor`, `CeleryExecutor`

### SequentialExecutor
_Default Airflow Executor_
- Runs one task at a time
- Useful for debugging
- Not recommended for production: limitations of task resources

### LocalExecutor
- Runs on a single system
- Treats tasks as processes
- **Parallelism** defined by the user: unlimited or limited to a number
- Utilize all resources

### CeleryExecutor
- Uses a Celery backend as task manager
- Multiple worker systems can be defined
- More difficult to setup & configure
- Powerful for organizations with extensive workflows

### Determine the Executor
- Via the `airflow.cfg` file, `executor= ...`
- Via the first line of `airflow list_dags`: `INFO-Using SequentialExecutor`

## Debugging and Troubleshooting
### DAG Won't Run on Schedule
- check if scheduler is running
- at least one`schedule_interval` hasn't passed
- Not enough tasks free within the executor to run
  - change executor type
  - add system resources
  - add more systems
  - change DAG scheduling

## DAG Won't Load
- DAG not in web UI
- DAG not in `airflow list_dags`
- Solutions
  - Verify DAG file is in the correct folder
  - Determine the DAGs folder via `airflow.cfg`

## Syntax Errors
- Most common reason
- Solutions
  - `airflow list_dags`
  - Run the Python interpreter
