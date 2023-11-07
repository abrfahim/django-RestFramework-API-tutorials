import requests
import json

URL = 'http://127.0.0.1:8000/netcreate/'

data={
    'id':3,
}

json_data = json.dumps(data)
response = requests.delete(url=URL, data=json_data)

data = response.json()
print(data)
