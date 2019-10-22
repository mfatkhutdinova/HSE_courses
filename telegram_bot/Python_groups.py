from VK_api import make_vk_request
from helpers import save_object_to_file

def search_Python_groups_from_vk(method, parameters):
    try:
        python_news = make_vk_request(method, parameters)
    except:
        return('Error!')
    id_python_group = []

    print(python_news)
    for group in python_news['response']['items']:
        python_groups = {}
        python_groups['id'] = group['id']
        python_groups['screen_name'] = group['screen_name']
        id_python_group.append(python_groups)

    save_object_to_file(id_python_group, "id_python_groups.json")
    return("Done!")

if __name__ == '__main__':
    method, parameters = 'groups.search', 'q=Python&type=group'
    print(search_Python_groups_from_vk(method, parameters))