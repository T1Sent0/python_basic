user_balance = 0
user_purchase_history = []

def pay_balance():
    global user_balance
    new_balance = input('Введите сумму пополнения: ')

    try:
        new_balance = int(new_balance)
        user_balance += int(new_balance)
    except ValueError:
        print(f"Невозможно преобразовать '{new_balance}' в число.")

    show_menu()

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
        else: print("На балансе недостаточно средств")
    except ValueError:
        print(f"Невозможно преобразовать '{sum_purchase}' в число.")

    show_menu()

def show_purchase_history():
    for purchase in user_purchase_history:
        print(purchase)

    show_menu()


def show_menu():
    while True:
        print()
        print(f"На вашем счету {user_balance}")
        print()
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        print()
        choise = input('Выберите пункт меню: ')
        if choise == '1':
            pay_balance()
        elif choise == '2':
            purchase()
        elif choise == '3':
            show_purchase_history()
        elif choise == '4':
            return
        else: print('Не верный пункт меню: ')


show_menu()