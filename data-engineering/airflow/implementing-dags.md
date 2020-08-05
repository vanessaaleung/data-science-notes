# Implementing Airflow DAGS
1. [Airflow Operators](#airflow-operators)
2. [Airflow Tasks](#airflow-tasks)
3. [Additional Operators](#additional-operators)
4. [Airflow Scheduling](#airflow-scheduling)

## Airflow Operators
_Represents a single task in a workflow_
- Run independently ususally
- Generally don't share information

### BashOperator
- Executes a give Bash command or script
```python
# Import the BashOperator
from airflow.operators.bash_operator import BashOperator

# Define the BashOperator
example_task = BashOperator(
  task_id='bash_example',
  # Define the bash_command
  bash_command='echo "Example!"',
  # Add the task to the dag
  dag=ml_dag)
```
- Runs the command in a temporary directory
- Can specify environment variables for the command
- Not guaranteed to run in the same location/environment

## Airflow Tasks
_Instances of operators_
- Assigned to a variable in Python
```python
task_id='bash_example'
```
### Task Dependencies
_Define a given order of task completion_
- Upstream: `>>`, means before
- Downstream: `<<`, means after
```python
task1 >> task2 >> task3
```
- Mixed dependencies
```python
task1 >> task2 << task3
```
or
```python
task1 >> task2 
task3 >> task2 
```
Either task 1 or 3 can run first

## Additional Operators
### Python Operator
- Executes a Python function/callable
```python
from airflow.operators.python_operator import PythonOperator

def printme():
  print("This goes in the logs!")
python_task = PythonOperator(
  ...
  python_callable=printme,
)
```
- Can pass in arguments using the `op_kwargs` dictionary
```python
def sleep(length_of_time):
  time.sleep(length_of_time)
sleep_task = PythonOperator(
  ...
  op_kwargs={'length_of_time': 5}
}
```
### EmailOperator
- Sends an email
- Can contain
  - HTML content
  - Attachments
```python
from airflow.operators.email_operator import EmailOperator
email_task = EmailOperator(
  ...
  to='abc@def.gh',
  subject='Test Subject',
  html_content='Test HTML',
  files='latest_sales.xlsx'
)
```
## Airflow Scheduling
### DAG Runs
_A specific instance of a workflow at a point in time_
- Can be run manually or via `schedule_interval`
- Maintain state for each workflow and the tasks within
  - running
  - failed
  - success
  
### Schedule Details
- `start_date`: initially schedule the DAG run
- `end_date`: when to stop running new DAG instances
- `max_tries`: how many attempts to make before fully failing the diagram
- `schedule_interval`: how often to schedule the DAG
    - between the `start_date` and `end_date`
    - can be defined in `cron` syntax
      - consists of 5 fields separated by a space
      - `*` represnets running for every interval
      - can be comma separated values in fields for a list of values
      <img src="https://ostechnix.com/wp-content/uploads/2018/05/cron-job-format-1.png">
      
      ```python
      0 12 * * *                # run daily at noon
      * * 25 2 *                # run once per minute on Feb 25
      0,15,30,45 * * * *        # run every 15 minutes
      ```
- use the `start_date` as the earliest possible value
- schedule the task at `start_date` + `schedule_interval`
```
'start_date': datetime(2020, 2, 25),
'schedule_interval': @daily
```
means the earliest starting time to run the DAG is on Feb 26th, 2020

### Airflow Scheduler Presets
- `@hourly`
- `@daily`
- `@weekly`
- Special presets for `schedule_interval`
  - `None`: Don't schedule ever, used for manually triggered DAGs
  - `@once`: schedule only once

