# Maintaining and Monitoring Airflow Workflows

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
