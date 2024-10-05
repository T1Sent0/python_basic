year = input('В каком году родился А.С. Пушкин ? ')
day = ''

def check_birth_year():
    global year
    global day
    while (year != '1799'):
        print()
        year = input('Вы ошиблись. Попробуйте ещё раз ')

    day = input('В какой день он родится ? ')
    check_birth_day()

def check_birth_day():
    global day
    while (day != '6'):
        print()
        day = input('Вы ошиблись. Попробуйте ещё раз ')

    print('Верно')

check_birth_year()