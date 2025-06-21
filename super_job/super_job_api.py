import requests
import json
from helpers import get_api_key_from_file

def make_superjob_request(relative_url, url_params = None):
    api_key = get_api_key_from_file("superJob_api_key.txt")
    headers = {'X-Api-App-Id' : api_key}
    response = requests.get('https://api.superjob.ru/2.0/%s' % relative_url,
                            params=url_params, headers=headers)
    return response.json()



