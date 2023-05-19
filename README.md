
# Weather datapipeline


Weather datapipeline: Develop a datapipeline that extract weather information from an API based on the user's location or a specified city.

Using Apache Airflow to scheduling the current weather conditions along with a forecast for the upcoming days.

The output of this workflow will be saved in a specific folder that contains the week number in format 'csv', and it going to be used for the stakeholders for planning your actions.

## API Reference

```
  https://www.visualcrossing.com/weather-api
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `YOUR_API_KEY` | `string` | **Required**. Your API key |


## Environment Variables

To run this project, you will need to change the following variables

`YOUR_API_KEY`


## Tech

**Python** 

**Apache Airflow** 

**Bash** 


## Bash commands

sudo apt update
sudo apt upgrade
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.10

apt install python3.10-venv
python3.10 -m venv venv
source venv/bin/activate

pip install 'apache-airflow==2.3.2' --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.3.2/constraints-3.10.txt"

export AIRFLOW_HOME=~/Documents/weather_datapipeline/airflow_weather (change by your dir)

airflow standalone (just for tests)


## Task (in development)
Put some Imagens 





