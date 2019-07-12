from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from nonexist import astral

dag_id = "hello_dag_bag_wrong"

with DAG(dag_id=dag_id, start_date=datetime(2018, 11, 14),
         schedule_interval=None) as dag:

    def say_hello_wrong():
        print("Hello, wrong DAG!")

    PythonOperator(task_id="say_hello_wrong", python_callable=say_hello_wrong)
