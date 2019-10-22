import requests
import vk
from helpers import get_object_from_file_txt

def make_vk_request(METHOD_NAME, PARAMETERS):
    ACCESS_TOKEN = get_object_from_file_txt("access_token.txt")
    V = get_object_from_file_txt("version_API.txt")

    response = requests.get('https://api.vk.com/method/%s?%s&access_token=%s&v=%s' %(METHOD_NAME, PARAMETERS, ACCESS_TOKEN, V))
    if (response.status_code == requests.codes.ok):
        return response.json()
    else:
        return("Error" + response.status_code)

if __name__ == '__main__':
    print(make_vk_request('users.get', 'fields'))
