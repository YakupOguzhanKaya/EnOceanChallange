# EnOcean QA Engineer Challenge

## Requirements

- Python 3.8+

## Getting Started

Install requirements for scripts,

```
pip install -r requirement.txt
```

### Challenge 1

Please write a script to retrieve JSON data from a REST API and validate the response.
Please use the following API https://jsonplaceholder.typicode.com/

On the `tests/test_api.py` file your script should:

1.	Do a GET request to the /users endpoint
2.	Validate the response code to be 200
3.	Validate the response is an array of json objects
4.  Write a file named "target_companies.txt" which contains the company names ends with " Group" from the response

### Challenge 2

Please write a robot script to fetch data using a swagger schema (https://petstore3.swagger.io/) and submit to another web service (https://postman-echo.com). 

Using the given swagger schema,
On the `e2e/api.robot` file your script implementation should:

1.	Fetch all available pets 
2.	Iterate through available pets
3.	For each pet, 
    - Transform pet name to uppercase
    - Post a json object`https://postman-echo.com/post` with schema below
    - Validate the response code to be 200
    - Validate the response data contains sent uppercase name. 
```json
{
    "name": NAME_OF_THE_PET_IN_UPPERCASE,
}
```

### Challenge 3

Please write an unit test to assert that log_to_stdout() method in tests/log_function.py logs the sentence below every 1 minute.
"This line should be logged every 1 minute"

Use tests/test_log_function.py file to implement your unit test.

1.  After test execution there shouldn't be any warnings/errors regarding async tasks. 
2.  Seeing the log two times in two minutes is enough for assertion.