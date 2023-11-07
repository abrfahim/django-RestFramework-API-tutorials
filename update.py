import requests
import json

URL = 'http://127.0.0.1:8000/netcreate/'

data ={
    'id':1,
    'duration': 6,
    
}

json_data = json.dumps(data)
response = requests.put(url=URL, data=json_data)

data = response.json()
print(data)