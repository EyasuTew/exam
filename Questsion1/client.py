import json
import flask
import requests

while True:
    #headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    response = requests.post('http://localhost:5009/getObjloc')
    print(response.content)
    print("----")
