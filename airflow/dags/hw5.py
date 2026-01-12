from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.exceptions import AirflowException
import random
import logging
from datetime import datetime,timedelta

def my_dec(func):
    def wrapper(*args, **kwargs):
         ti = kwargs["ti"]
         run_id = kwargs["run_id"]
         ds = kwargs["ds"]
         task_id = ti.task_id

         result = func(*args, **kwargs)

         logging.info(f"run_id={run_id}, ds={ds}, task_id={task_id}")
         return result
    return wrapper

@my_dec
def generate_usd_rate(**kwargs):
    ti = kwargs['ti']

    rate = random.randint(1, 8)

    logging.info(f"Сгенерированный курс = {rate}")
    return rate

@my_dec
def check_usd_rate(**kwargs):
    ti = kwargs['ti']
    rate = ti.xcom_pull(task_ids='generate_usd_rate')
    logging.info(f"Полученное значение {rate}")
    if rate < 3 or rate > 6:
        raise AirflowException("Входит в диапазон меньше 3 или больше 6")
    else:
        logging.info(f"После проверки: {rate}")
    ti.xcom_push(key='checked_rate', value=rate)

@my_dec
def print_report(**kwargs):
    ti = kwargs['ti']
    rate = ti.xcom_pull(task_ids='check_usd_rate', key ='checked_rate')
    logging.info(f"Финальный отчет:{rate}")




default_args = {
    "owner" : "user",
    "start_date": datetime(2025, 12, 19),
    "retries": 3,
    "retry_delay": timedelta(seconds=10),
}

with DAG (
    dag_id = "student_fx_tiny_dag_Artyom",
    default_args = default_args,
    schedule = '*/2 * * * *',
    catchup = False,
    tags = ["hw5"],
):

    start = EmptyOperator(task_id = "start")

    end = EmptyOperator(task_id = "end")

    generate_usd_rate = PythonOperator(
        task_id = 'generate_usd_rate',
        python_callable = generate_usd_rate,
    )

    check_usd_rate= PythonOperator(
        task_id = 'check_usd_rate',
        python_callable = check_usd_rate,
    )

    print_report = PythonOperator(
        task_id='print_report',
        python_callable=print_report,
    )

    start >> generate_usd_rate >> check_usd_rate >> print_report >> end