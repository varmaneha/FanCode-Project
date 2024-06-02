import requests

def get_users():
    response = requests.get("http://jsonplaceholder.typicode.com/users")
    response.raise_for_status()
    return response.json()

def get_todos():
    response = requests.get("http://jsonplaceholder.typicode.com/todos")
    response.raise_for_status()
    return response.json()
