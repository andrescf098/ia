import requests

def get_categories():
    response = requests.get('https://api.escuelajs.co/api/v1/categories')
    return response.json()