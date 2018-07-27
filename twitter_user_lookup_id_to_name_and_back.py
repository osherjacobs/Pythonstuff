import requests
import json
import time
from twitcredentials import *

# FUNC NUMBER 1
api_url = 'https://api.twitter.com/1.1/users/lookup.json'


def lookup_users_id_to_name(user_id):
    query_url = api_url
    params = {'user_id': user_id}
    response = requests.get(query_url, params=params, auth=oauth)
    time.sleep(3)

    if response.status_code == 200:
        lst = json.loads(response.content)
        return lst[0]['screen_name']
    return None


hldr = lookup_users_id_to_name(UID)  # function call

print(hldr)

# FUNC NUMBER 2


def lookup_users_name_to_id(screen_name):
    query_url = api_url
    params = {'screen_name': screen_name}
    response = requests.get(query_url, params=params, auth=oauth)
    time.sleep(3)

    if response.status_code == 200:
        lst = json.loads(response.content)
        return lst[0]['id']
    return None


hldr1 = lookup_users_name_to_id(uname)  # function call

print(hldr1)
