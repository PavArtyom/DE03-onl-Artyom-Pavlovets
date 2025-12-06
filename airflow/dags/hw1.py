from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import BranchPythonOperator
from airflow.sensors.time_delta import TimeDeltaSensor
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

name = "Artyom"

def positive_numbers():
    list_of_numbers = [1, -2, 5, 0, 3]
    positive_list = []
    for number in list_of_numbers:
        if number > 0:
            positive_list.append(number)
    total = 0
    for p in positive_list:
        total += p
    print(f"Сумма положительных: {total}")

default_args = {
    "owner" : "user",
    "start_date": datetime(2025, 6, 1),
}

with DAG (
    dag_id = f"{name.lower()}_homework_dag",
    default_args = default_args,
    schedule = None,
    catchup = False,
    tags = ["Homework"],
):
    start = EmptyOperator(task_id="start")

    download_data = BashOperator(
        task_id="download_data",
        bash_command='echo "Downloading data..."'
)

    positive_numbers = PythonOperator(
        task_id = "positive_numbers",
        python_callable = positive_numbers,
    )

    sensor_task = TimeDeltaSensor(
        task_id="sensor_wait_3_seconds",
        delta=timedelta(seconds=3),
        poke_interval=1,
        mode="reschedule",
    )

    end = EmptyOperator(task_id="end")

    start >> download_data >> positive_numbers >> sensor_task >> end