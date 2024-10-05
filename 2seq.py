list_values = ''
spliterator = ','
has_semicolon = False
has_slash_symbol = False

def check_value():
    if list_values.find(';') >= 0:
        global spliterator
        spliterator = ';'
        global has_semicolon
        has_semicolon = True

    if list_values.find('/') >= 0:
        spliterator = '/'
        global has_slash_symbol
        has_slash_symbol = True


def ask_user():
    global list_values
    list_values = input('Введите любые цифры через запятую - ')

    while list_values == '':
        global spliterator
        list_values = input('Введите любые цифры через запятую - ')
        spliterator = ','

    check_value()


ask_user()


if spliterator != ',' and (has_semicolon and has_slash_symbol):
    ask_user()

uq_result = set(list_values.split(spliterator))
list_result = list(uq_result)

print('Ваш список')
print(list_result)
