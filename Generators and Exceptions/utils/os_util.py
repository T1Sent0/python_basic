import os
import shutil
import platform


def create_directory(name):
    """
    Функция создаёт директорию
    :param name:
    :return:
    """
    if not os.path.exists(name):
        os.mkdir(name, 0o777)


def delete(name):
    """
    Удаляет файл или директорию по названию
    :param name:
    :return:
    """
    is_folder = os.path.isdir(name)
    # переписано на тернарный оператор
    os.remove(name) if not is_folder else shutil.rmtree(name)

def copy(source, dest):
    """
    Функция копирует файлы или директории
    :param source:
    :param dest:
    :return:
    """
    is_folder = os.path.isdir(source)
    if not is_folder:
        shutil.copy(source, dest)
    else:
        if '.' in dest:
            print("нельзя копировать директорию в файл")
            return

        shutil.copytree(source, dest)


def get_current_directory_list(path, can_sort = False):
    list_item_directory = []
    if os.path.isdir(path):
        if can_sort:
            list_item_directory.append(get_files_on_directory(path))
            list_item_directory.append(get_directory_by_path(path))

        for dir_item in os.listdir(path):
            list_item_directory.append(dir_item)

    return list_item_directory


def show_current_directory(path):
    """
    Функция выводит наполнение указанной директории
    :param path:
    :return:
    """
    if os.path.isdir(path):
        print()
        # переписано на генератор списка
        print_dir_items = [dir_item for dir_item in get_current_directory_list(path)]
        print(print_dir_items)
    else:
        print("Не возможно применить к файлу")


def get_directory_by_path(path):
    """
    Получает только директории по пути
    :param path:
    :return:
    """
    directory_list = []
    for dir_item in os.listdir(path):
        if os.path.isdir(dir_item):
            directory_list.append(dir_item)

    return directory_list

def show_only_directory(path):
    """
    Функция выводит на экран только директории
    :param path:
    :return:
    """
    for dir_item in get_directory_by_path(path):
            print(dir_item)


def get_files_on_directory(path):
    """
    Возвращает только файлы из директории
    :param path:
    :return:
    """
    list_files = []
    for dir_item in os.listdir(path):
        if not os.path.isdir(dir_item):
            list_files.append(dir_item)

    return list_files

def show_only_files(path):
    """
    Функция выводит на экран только файлы
    :param path:
    :return:
    """
    for dir_item in get_files_on_directory(path):
        print(dir_item)

def show_operation_system_info():
    """
    Функция выводит информацию о системе
    :return:
    """
    print()
    print("Информация о системе: ")
    print("Имя OS: ", platform.system())
    print("Версия ОС:", platform.version())
    print("Архитектура ОС:", platform.architecture())
    print("Полная информация о системе:", platform.platform())
    print("Имя компьютера:", platform.node())
    print("Версия Python:", platform.python_version())


def change_work_directory(path):
    """
    Изменяет рабочую директорию
    :param path:
    :return:
    """
    if '.' in path:
        print("Нельзя изменить директорию на файл")
        return
    else:
        os.chdir(path)


def save_current_directory_to_file(content):
    """
    Сохраняет в файл наполнение текущей директории
    :param content:
    :return:
    """
    with open('current_directory_data.txt', 'w') as file:
        file.write(content)