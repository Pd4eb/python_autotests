import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '1e5405868450408e5d1a9d137b3340b8'
HEADER = {'Content-Type': 'application/json','trainer_token':TOKEN}
TRAINER_ID = 33176

def test_status_code():
    response =requests.get(url=f'{URL}/trainers',params={'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_part_of_respons():
    response_get=requests.get(url=f'{URL}/trainers',params={'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0]["id"] == '33176'