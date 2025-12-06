from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import BranchPythonOperator
from airflow.sensors.time_delta import TimeDeltaSensor
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

name = "Artyom"

def calculate_sum(N):
    result = sum(range(1, N+1))
    print(f"Сумма чисел от 1 до {N} = {result}")
    return result

default_args = {
    "owner" : "user",
    "start_date": datetime(2024, 1, 1),
}

with DAG (
    dag_id = f"{name.lower()}_heavy_task_dag",
    default_args = default_args,
    schedule = None,
    catchup = False,
    tags = ["Calculate sum"],
):

    start = EmptyOperator(task_id = "start")

    sensor_task = TimeDeltaSensor(
        task_id="sensor_wait_5_seconds",
        delta=timedelta(seconds=5),
        poke_interval=1,
        mode="reschedule",
    )

    calculate_sum = PythonOperator(
        task_id = "calculate_sum",
        python_callable = calculate_sum,
        op_kwargs={'N': 9}
    )

    end = EmptyOperator(task_id = "end")

    start >> sensor_task >> calculate_sum >> end