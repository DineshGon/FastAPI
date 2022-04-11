from fastapi.testclient import TestClient
import json

import os
# print(os.path.abspath(__file__))
# print(__file__)
import sys
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ..main import app

# from vaccine.routers.vaccineRouter import router

client = TestClient(app)

def test_create_vaccine():
    data = {"startTime": '3:30', 'endTime':'5:40'}
    response = client.post('/vaccine',json.dumps(data))
    assert response.status_code == 201
    assert response.json()['startTime'] == '3:30'
