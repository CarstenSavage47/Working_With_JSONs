# Pulling data from Star Wars API Example
import pandas
import requests
import json
import ijson
from pandas.io.json import json_normalize

response = requests.get("https://swapi.dev/api/people")
response.json()
print(response.text)
response.json().keys()
response.json()['results']
People_JSON = response.json()['results']
People = pandas.json_normalize(People_JSON)




