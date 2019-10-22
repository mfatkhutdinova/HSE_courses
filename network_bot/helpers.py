import json
import os
import re
from getpass import getpass


def delete_punctuations(text):
    if not isinstance(text, str):
        return ''
    return re.sub(r"([^\w\d\s]|_)", '', text)


def save_json_data(data, path, method="write"):
    if os.path.exists(path):
        return
    with open(path, method[0], encoding="utf-8",
              errors="xmlcharrefreplace") as writer:
        json.dump(data, writer, ensure_ascii=False, indent=True)


def load_json_data(path):
    if os.path.exists(path):
        return
    with open(path, encoding="utf-8", errors="xmlcharrefreplace") as reader:
        return json.load(reader)


def load_txt_data(file_name):
    with open(file_name, 'r', encoding='utf-8')as reader:
        return str(reader.read())


def get_api_key(env_var_name, source_name):
    api_key = os.environ.get(env_var_name)
    if not api_key:
        api_key = getpass(f"Please, enter your api-key from {source_name}: ")
        os.environ[env_var_name] = api_key
    return api_key


def get_data_and_save(object_to_save, file_name):
    user_old_data = load_json_data(file_name)
    new_user_data = []
    if not user_old_data:
        new_user_data.append(object_to_save)
        save_json_data(new_user_data, file_name)

    for old_data in user_old_data:
        new_user_data.append(old_data)
    new_user_data.append(object_to_save)

    save_json_data(new_user_data, file_name)
