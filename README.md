
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

