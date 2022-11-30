import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weatherapi.settings')
django.setup()

import requests
from api.models import Users 

def get_data(user_url): 
    response = requests.get(user_url)

    for repo in response.json():
        user = Users.objects.get_or_create(id = repo['id'], name = repo['name'], username = repo['username'], email=repo['email'], phone=repo['phone'])[0]

if __name__ == '__main__':
    user_url = "https://jsonplaceholder.typicode.com/users"
    get_data(user_url)