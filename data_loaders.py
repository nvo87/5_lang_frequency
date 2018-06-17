import json


def load_from_json(filepath):
    with open(filepath, encoding='utf-8') as file_object:
        try:
            return json.load(file_object)
        except json.decoder.JSONDecodeError:
            return None


def load_from_txt(filepath):
    try:
        with open(filepath, encoding='utf-8') as file_object:
            return file_object.read()
    except UnicodeDecodeError:
        with open(filepath, encoding='cp1251') as file_object:
            return file_object.read()
    except UnicodeDecodeError:
        return None