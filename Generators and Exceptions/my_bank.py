from utils.json_helper import create_json_file, get_json_data

user_data_directory = 'user_data'
balance_file_name = 'bank_account_data.json'
purchase_history = 'purchase_history.json'
user_balance = 0
user_purchase_history = []


def get_user_balance():
    user_account_data = get_json_data(f'{user_data_directory}/{balance_file_name}')
    if user_account_data is None:
        return 0

    return user_account_data['balance']


def read_balance(new_balance):
    new_data = {
        'balance': new_balance,
    }

    create_json_file(new_data, f'{user_data_directory}/{balance_file_name}')


def update_balance(new_balance):
    read_balance(new_balance)


def pay_balance():
    global user_balance
    new_balance = input('Введите сумму пополнения: ')

    try:
        new_balance = int(new_balance)
        user_balance += int(new_balance)

        read_balance(user_balance)

    except ValueError:
        print(f"Невозможно преобразовать '{new_balance}' в число.")


def save_purchase_history(purchase_name):
    existing_data = get_json_data(f'{user_data_directory}/{purchase_history}')
    if not existing_data:
        existing_data = [{'purchase_name': purchase_name }]
    else:
        existing_data = list(existing_data['purchase_history'])
        existing_data.append({
            'purchase_name': purchase_name,
        })

    create_json_file({'purchase_history': existing_data}, f'{user_data_directory}/{purchase_history}')


def get_purchase_history():
    existing_data = get_json_data(f'{user_data_directory}/{purchase_history}')

    if existing_data is None:
        return 0

    return list(existing_data['purchase_history'])


def purchase():
    global user_balance
    global user_purchase_history
    sum_purchase = input('Введите сумму покупки: ')

    try:
        sum_purchase = int(sum_purchase)
        if user_balance >= sum_purchase:
            purchase_name = input('Введите наименование покупки: ')
            user_purchase_history.append(purchase_name)
            user_balance = user_balance - sum_purchase
            save_purchase_history(purchase_name)
            update_balance(user_balance)
        else:
            print("На балансе недостаточно средств")
    except ValueError:
        print(f"Невозможно преобразовать '{sum_purchase}' в число.")


def show_purchase_history():
    global user_purchase_history

    if not user_purchase_history:
        user_purchase_history = get_purchase_history()

    # переписано на генератор списка
    print_result = [purchase for purchase in user_purchase_history]
    print(print_result)

def show_menu():
    global user_balance
    while True:
        print()
        user_balance = get_user_balance()
        print(f"На вашем счету {user_balance}")
        print()
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        print()
        choice = input('Выберите пункт меню: ')
        if choice == '1':

            pay_balance()
        elif choice == '2':
            purchase()
        elif choice == '3':
            show_purchase_history()
        elif choice == '4':
            break
        else:
            print('Не верный пункт меню: ')


if __name__ == "__main__":
    show_menu()
