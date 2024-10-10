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
    if not is_folder:
        os.remove(name)
    else:
        shutil.rmtree(name)

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


def show_current_directory(path):
    """
    Функция выводит наполнение указанной директории
    :param path:
    :return:
    """
    if os.path.isdir(path):
        print()
        for dir_item in os.listdir(path):
            print(dir_item)
    else:
        print("Не возможно применить к файлу")


def show_only_directory(path):
    """
    Функция выводит на экран только директории
    :param path:
    :return:
    """
    for dir_item in os.listdir(path):
        if os.path.isdir(dir_item):
            print(dir_item)


def show_only_files(path):
    """
    Функция выводит на экран только файлы
    :param path:
    :return:
    """
    for dir_item in os.listdir(path):
        if not os.path.isdir(dir_item):
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