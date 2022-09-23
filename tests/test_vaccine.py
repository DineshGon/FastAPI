from fastapi.testclient import TestClient
import json

from src.main import app

# Ref https://fastapi.tiangolo.com/tutorial/testing/


client = TestClient(app)


def test_retrieve_appointments_byid():
    data = {"startTime": '3:30', 'endTime': '5:40'}
    response = client.post('/devsecops/vaccine', json.dumps(data))
    # response.raw
    response = client.get('/devsecops/vaccine/1')
    assert response.status_code == 200
    assert response.json()['startTime'] == '3:30'
    assert response.json()['endTime'] == '5:40'


def test_create_vaccine():
    data = {"startTime": '3:30', 'endTime': '5:40'}
    response = client.post('/devsecops/vaccine', json.dumps(data))
    assert response.status_code == 201
    assert response.json()['startTime'] == '3:30'
    assert response.json()['endTime'] == '5:40'


def test_retrieve_all_appointments():
    response = client.get('/devsecops/vaccine/all')
    assert response.status_code == 200


def test_update_appointment():
    data = {"startTime": '1:10', 'endTime': '2:20'}
    response = client.put('devsecops/vaccine/1', json.dumps(data))
    print(response.json(), "****************")
    print(response, "****************")
    assert response.status_code == 202
    assert response.json() == 'updated'


def test_delete_appointment():
    response = client.delete('/devsecops/vaccine/1')
    assert response.status_code == 204


## second test of tc

data1 = {
    'startTime': '10:50',
    'endTime': '11:50'
}


def test_create_vaccine_1():
    response = client.post('/devsecops/vaccine', json=data1)
    assert response.status_code == 201
    assert response.json()['startTime'] == '10:50'

# print(os.path.abspath(__file__))
# print(__file__)
# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# from vaccine.routers.vaccineRouter import router
