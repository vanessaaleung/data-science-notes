# Implementing Airflow DAGS

## Airflow operators
_Represents a sigle task in a workflow_
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
