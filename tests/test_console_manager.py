import os.path
import shutil

from utils.os_util import create_directory, delete, copy

"""
    Тест функции создания директории
"""


def test_create_directory():
    directory_name = "Test"
    create_directory(directory_name)
    assert os.path.exists(directory_name) is True
    shutil.rmtree(directory_name)


"""
    Тест удаления директории
"""


def test_delete():
    directory_name = "Test"
    file_name = 'test.txt'
    create_directory(directory_name)
    assert os.path.exists(directory_name) is True
    delete(directory_name)
    assert os.path.exists(directory_name) is False
    with open(file_name, 'w') as file:
        file.write('Hello')
    assert os.path.isfile(file_name) is True
    delete(file_name)
    assert os.path.isfile(file_name) is False


"""
    Тест копирования директории
"""


def test_copy():
    source_directory = 'Test'
    dest_directory = 'Test2'
    file_name = 'test.txt'

    create_directory(source_directory)
    create_directory(dest_directory)
    assert os.path.exists(source_directory) is True
    assert os.path.exists(dest_directory) is True
    copy(source_directory, f'{dest_directory}/{source_directory}')
    assert os.path.exists(f'{dest_directory}/{source_directory}') is True

    with open(file_name, 'w') as file:
        file.write('Hello')

    copy(file_name, f'{dest_directory}/{source_directory}')

    assert os.path.exists(f'{dest_directory}/{source_directory}/{file_name}') is True
    delete(source_directory)
    delete(dest_directory)
    delete(file_name)

