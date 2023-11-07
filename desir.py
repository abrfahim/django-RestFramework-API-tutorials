import requests
import json

URL = 'http://127.0.0.1:8000/netcreate/'

data ={
    'teacher_name': 'Rashed Abrar',
    'course_name': 'Data Science',
    'duration':6,
    'seat': 20,
}

json_data = json.dumps(data)
r = requests.post(url=URL, data=json_data)
data = r.json()
print(data)