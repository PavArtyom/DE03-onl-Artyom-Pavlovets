from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

name = "Artyom"

def count_positive_numbers():
    my_list = [-5, -2, 0, 3, 7, 10, -1, 4]
    positive_list = []
    for number in my_list:
        if number > 0:
            positive_list.append(number)
    print (f"Количество положительных чисел: {len(positive_list)}")

default_args = {
    "owner" : "user",
    "start_date": datetime(2024, 1, 1),
}

with DAG (
    dag_id = f"{name.lower()}_positive_count_dag",
    default_args = default_args,
    schedule = None,
    catchup = False,
    tags = ["Count positive numbers"],
):
    task_count_even = PythonOperator(
        task_id="count_positive_numbers",
        python_callable=count_positive_numbers,
    )


