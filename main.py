from utils.is_number import is_number
from utils.to_number import to_number
from utils.os_util import *
from my_bank import show_menu
from victory import victorina

while True:
    print()
    print('Меню')
    print('1. Создать директорию')
    print('2. Удалить')
    print('3. Копировать (файл/директорию)')
    print('4. Просмотр содержимого')
    print('5. Посмотреть только директории')
    print('6. Посмотреть только файлы')
    print('7. Посмотреть информацию об операционной системе')
    print('8. Создатель программы')
    print('9. Играть в викторину')
    print('10. Мой банковский счёт')
    print('11. Смена рабочей директории')
    print('12. Cохранить содержимое рабочей директории в файл')
    print('13. Выход')

    choice = input("Выберите пункт меню: ")
    input_choice = to_number(choice)

    while not is_number(input_choice):
        input_choice = input("Введите число от 1 до 13: ")
        input_choice = to_number(input_choice)

    if input_choice < 1 or input_choice > 12:
        print('Выход. Вы должны ввести число от 1 до 13')
        break

    if input_choice == 1:
        directory_name = input("Введите име директории: ")
        create_directory(directory_name)
    elif input_choice == 2:
        directory_name = input("Введите име директории: ")
        delete(directory_name)

    elif input_choice == 3:
        source_directory = input("Введите имя директории или файла для копирования: ")
        dest_directory = input("Введите имя директории куда копировать или новое имя файла: ")
        copy(source_directory, dest_directory)

    elif input_choice == 4:
        directory_name = input("Введите име директории: ")
        show_current_directory(directory_name)

    elif input_choice == 5:
        directory_name = input("Введите имя директории: ")
        show_only_directory(directory_name)

    elif input_choice == 6:
        directory_name = input("Введите имя директории: ")
        show_only_files(directory_name)

    elif input_choice == 7:
        show_operation_system_info()

    elif input_choice == 8:
        print("Создатель программы: Гайдаш Алексей.")
        print("E-mail для связи - foregestore@gmail.com")

    elif input_choice == 9:
        victorina()

    elif input_choice == 10:
        show_menu()

    elif input_choice == 11:
        directory_name = input("Введите имя директории: ")
        change_work_directory(directory_name)

    elif input_choice == 12:
        directory_name = input("Введите име директории: ")
        file_names = 'files - ' + ' '.join(get_files_on_directory(directory_name))
        directory_names = 'dirs - ' + ' '.join(get_directory_by_path(directory_name))
        result = f'{file_names} \n{directory_names}'
        save_current_directory_to_file(result)

    elif input_choice == 13:
        break
    else:
        print('Не верный пункт меню')