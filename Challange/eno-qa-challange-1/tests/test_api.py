import json
import requests


def test_challenge_1():
    url = "https://jsonplaceholder.typicode.com"
    response = requests.get(f"{url}/users")
    assert response.ok
    try:
        json_object = json.loads(response.text)
        print("Response is json object")
        assert True
    except ValueError as e:
        print("Response is not json object")
        assert False

    output_file = open("target_companies.txt", "w")
    for one_array in json_object:
        output_file.write(one_array['company']['name'] + " Group \n")
    output_file.close()


test_challenge_1()
