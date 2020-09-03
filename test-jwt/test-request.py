import jwt_util
import requests
import json
import os

CREDENTIAL_FILE = '/home/brodseba/projects/.credential/app-v2-invoker.json'
RUN_SERVICE_URL = 'https://app-v2-3ezovjb7wq-nn.a.run.app/app/v2/places'

token = jwt_util.get_id_token(CREDENTIAL_FILE, RUN_SERVICE_URL)
request = requests.get(
    url = RUN_SERVICE_URL,
    headers = {
        'Authorization': f'Bearer {token}'
    }
)
results = {
    'status_code': request.status_code,
    'response': request.json()
}

print(json.dumps(results, indent=2))