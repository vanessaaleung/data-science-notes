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
