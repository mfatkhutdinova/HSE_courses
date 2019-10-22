from helpers import get_object_from_file, save_object_to_file
from datetime import datetime
from VK_api import make_vk_request
import time
import os

def todays_date():
    return (str(datetime.today().date()))

def collects_useful_information_in_posts_in_VK(id_python_groups_list, date_today):
    useful_info_about_post_list = []

    for group in id_python_groups_list:
        posts_of_group = make_vk_request('wall.get', 'owner_id=-' + str(group['id']))
        try:
            for post in posts_of_group['response']['items']:
                if (time.strftime("%Y-%m-%d", time.localtime(post['date'])) == date_today):
                    useful_info_about_post = {}
                    useful_info_about_post['text'] = post['text']
                    useful_info_about_post['url'] = 'https://vk.com/' + str(group['screen_name']) + '?w=wall' + str(post['owner_id']) + '_' + str(post['id'])
                    useful_info_about_post['date'] = str(date_today)
                    useful_info_about_post_list.append(useful_info_about_post)
        except:
            continue
    return useful_info_about_post_list

def append_posts_in_file(useful_new_info, useful_old_info):
    new_posts = []
    for new_info in useful_new_info:
        is_info = False
        for old_info in useful_old_info:
            if old_info == new_info:
                is_info = True
                break
        if is_info == False:
            new_posts.append(new_info)

    if len(new_posts) != 0:
        for post in new_posts:
            useful_old_info.append(post)
        save_object_to_file(useful_old_info, 'Python_posts.json')

def search_todays_news_from_VK(name_file):
    id_python_groups_list = get_object_from_file(name_file)
    date_today = todays_date()

    useful_new_info = collects_useful_information_in_posts_in_VK(id_python_groups_list, date_today)

    if os.path.exists('Python_posts.json'):
        useful_old_info = get_object_from_file('Python_posts.json')
    else:
        save_object_to_file(useful_new_info, 'Python_posts.json')
        return('Done!')

    append_posts_in_file(useful_new_info, useful_old_info)
    return ('Done!')

if __name__ == '__main__':
    name_file = 'id_python_groups.json'
    print(search_todays_news_from_VK(name_file))