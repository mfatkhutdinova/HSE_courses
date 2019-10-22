import requests
import os

def make_vk_request(METHOD_NAME, PARAMETERS):
    ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
    V = '5.62'

    try:
        response = requests.get('https://api.vk.com/method/%s?%s&access_token=%s&v=%s' %(METHOD_NAME, PARAMETERS, ACCESS_TOKEN, V))
        if (response.status_code == requests.codes.ok):
            return response.json()
    except:
        return("Error" + response.status_code)

