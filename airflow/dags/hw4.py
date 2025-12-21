from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"[START] выполняю функцию {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[END] функция {func.__name__} завершена")
        return result

    return wrapper

def prepare_task(numbers, multiplier, **kwargs):
    ti = kwargs['ti']
    task_id = kwargs['task'].task_id
    logical_date = kwargs["logical_date"]
    print(f"Task ID: {task_id}, Logical date: {logical_date}")

    result = [n * multiplier for n in numbers]

    ti.xcom_push(key="numbers_scaled", value=result)

@my_decorator
def calculate_task(username, **kwargs):
    ti = kwargs['ti']
    value = ti.xcom_pull(key="numbers_scaled", task_ids='prepare_task')
    calc_value = sum(value)
    message = f"User {username}, total sum is {calc_value}"
    print(message)
    ti.xcom_push(key="summary", value=message)

def report_task(**kwargs):
    ti = kwargs['ti']
    summary = ti.xcom_pull(key="summary", task_ids='calculate_task')
    print(f"Финальный результат: {summary}")

default_args = {
    "owner" : "user",
    "start_date": datetime(2024, 1, 1),
}

with DAG (
    dag_id = "hw4_dag",
    default_args = default_args,
    schedule = None,
    catchup = False,
    tags = ["hw4"],
):

    prepare = PythonOperator(
        task_id = 'prepare_task',
        python_callable = prepare_task,
        op_args = [[20,40,60]],
        op_kwargs = {
            'multiplier': 2
        },
    )

    calculate = PythonOperator(
        task_id = 'calculate_task',
        python_callable = calculate_task,
        op_kwargs = {
            'username': 'Artyom'
        },
    )

    report = PythonOperator(
        task_id="report",
        python_callable=report_task,
    )

    prepare >> calculate >> report







