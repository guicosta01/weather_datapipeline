
# Weather datapipeline

A brief description of what this project does and who it's for:

Weather datapipeline: Develop a datapipeline that extract weather information from an API based on the user's location or a specified city.

Using Apache Airflow to scheduling the current weather conditions along with a forecast for the upcoming days.

The output of this workflow will be used for the stakeholders for planning your actions.
## API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`

`ANOTHER_API_KEY`


## Tech

**Python** 

**Apache Airflow** 


## Bash commands
get commands in doc 

sudo apt update
sudo apt upgrade
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.10

apt install python3.10-venv
python3.10 -m venv venv
source venv/bin/activate

pip install 'apache-airflow==2.3.2' --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.3.2/constraints-3.10.txt"

export AIRFLOW_HOME=~/Documents/weather_datapipeline/airflow_weather
airflow standalone


