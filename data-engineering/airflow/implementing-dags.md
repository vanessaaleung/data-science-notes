# Implementing Airflow DAGS

## Airflow operators
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

## Airflow tasks
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
