import requests
from config.config import BASE_URL

def get(endpoint, params=None, headers=None):
    url = BASE_URL + endpoint
    response = requests.get(url, params=params, headers=headers)
    return response

def post(endpoint, data=None, json=None, headers=None):
    url = BASE_URL + endpoint
    response = requests.post(url, data=data, json=json, headers=headers)
    return response

def put(endpoint, data=None, json=None, headers=None):
    url = BASE_URL + endpoint
    response = requests.put(url, data=data, json=json, headers=headers)
    return response

def delete(endpoint, data=None, json=None, headers=None):
    url = BASE_URL + endpoint
    response = requests.delete(url, data=data, json=json, headers=headers)
    return response


