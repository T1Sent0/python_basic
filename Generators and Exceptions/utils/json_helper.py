import json
import os.path
from utils.os_util import create_directory


def create_json_file(data, file_name):
    """
    Создаёт JSON файл и заполняет его данными
    :param data:
    :return:
    """
    if '/' in file_name:
        index_slash_char = file_name.find('/')
        directory_name = file_name[0:index_slash_char]
        create_directory(directory_name)

    with open(file_name, 'w') as file:
        json.dump(data, file)


def get_json_data(path_to_file):
    """
    Получает файл
    :param path_to_file:
    :return:
    """
    if os.path.isfile(path_to_file):
        with open(path_to_file, 'r') as file:
            content = file.read()
            return json.loads(content)
