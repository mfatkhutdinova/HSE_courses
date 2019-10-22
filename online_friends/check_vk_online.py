from VK_api import make_vk_request

def check_vk_online(method_name, parametres):
    online_fiends = []
    info_about_friend = {}
    all_friends = make_vk_request(method_name, parametres)

    for friend in all_friends['response']['items']:
        info_about_friend = {}
        if friend['online'] == 1:
            info_about_friend['first_name'] = friend['first_name']
            info_about_friend['last_name'] = friend['last_name']
            info_about_friend['url'] = 'https://vk.com/id' + str(friend['id'])
            online_fiends.append(info_about_friend)
    return online_fiends

def main(user_id):
    method_name = 'friends.get'
    parametres = 'user_id=' + user_id + '&order=name&fields=domain,online&name_case=nom'
    return (check_vk_online(method_name, parametres))






