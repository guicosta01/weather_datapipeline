from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.macros import ds_add
from datetime import datetime, timedelta
from os.path import join
import pandas as pd


date_today1 = datetime.today().isocalendar().week

bash_path = 'mkdir -p "/home/guilherme/Documents/weather_planning/week_{}"'.format(date_today1)

with DAG(
    'weather_dag_v4', 
    start_date = days_ago(1),
    schedule_interval = '@daily'

) as dag:
        
        task_mkdir = BashOperator(
            task_id = 'mkdir',
            bash_command = bash_path
        )


        def extract_data():
            delta_time = 7 
            date_today = datetime.today()
            date_end = date_today + timedelta(days = delta_time)

            date_today = date_today.strftime('%Y-%m-%d')
            date_end = date_end.strftime('%Y-%m-%d')

            city = 'Sao%20Paulo'
            key = YOUR_API_KEY
            url_api = join('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/' +
                        f'{city}/{date_today}/{date_end}?unitGroup=metric&include=days&key={key}&contentType=csv')
            df = pd.read_csv(url_api)

            file_path = r'/home/guilherme/Documents/weather_planning/week_{}/'.format(date_today1)
            df.to_csv(file_path + 'data_weather.csv')
            


        task_2 = PythonOperator(
                task_id = 'extract_weather_data',
                python_callable = extract_data
        )


        task_mkdir >> task_2

       
    

