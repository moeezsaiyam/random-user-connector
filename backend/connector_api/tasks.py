from __future__ import absolute_import, unicode_literals

import requests
from celery import shared_task
from .models import User

@shared_task
def randomuser_connector():
    """
    A Random User Connector that fetch user from the given endpoint perodically,
    and insert that in database
    """
    try:
        # fetch a random user from the given endpoint
        r = requests.get('https://randomuser.me/api')
        users = r.json()['results']

        for user in users:
        
            name = user['name']
            name = f"{name['title']} {name['first']} {name['last']}"
            email = user['email']
            gender = user['gender']
            country = user['location']['country']
            nationality = user['nat']

            # Add a user in the User Table
            User.objects.create(
                name = name,
                gender = gender,
                email = email,
                country = country,
                nationality = nationality
            )

        print("Success!")
    except Exception as e:
        print(e)

