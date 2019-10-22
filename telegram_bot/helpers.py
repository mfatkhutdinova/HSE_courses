import json

def save_object_to_file(object_to_save, file_name):
    with open(file_name, 'w', encoding='utf-8') as writter:
        writter.write(json.dumps(object_to_save, ensure_ascii=False, indent=True))

def get_object_from_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as reader:
        return json.load(reader)

def get_object_from_file_txt(file_name):
    with open(file_name, 'r', encoding='utf-8')as reader:
        return str(reader.read())