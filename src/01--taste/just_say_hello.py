from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

dag_id = "just_say_hello"

with DAG(dag_id=dag_id, start_date=datetime(2018, 11, 14),
         schedule_interval=None) as dag:

    def say_hello():
        print("Hello Airflow!")

    PythonOperator(task_id="say_hello", python_callable=say_hello)
