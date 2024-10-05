import random

hollywood_actor_names = dict([('Джонни Депп', '09.06.1963'), ('Роберт Дауни-младший', '04.04.1965'),
                              ('Кристиан Бэйл', '30.01.1974'), ('Уиллард Кэрролл Смит Второй', '25.09.1968'),
                              ('Дуэйн Джонсон', '02.05.1972'), ('Сэмюэл Л. Джексон', '21.12.1948'),
                              ('Крис Хемсворт', '11.08.1983'), ('Том Хиддлстон', '09.02.1981'),
                              ('Райан Гослинг', '12.11.1980'), ('Кларк Грегг', '02.04.1962')])

hollywood_actor_birthday_map = dict([('09.06.1963', 'Девятое Июня 1963'), ('04.04.1965', 'Четвёртое Апреля 1965'),
                                    ('30.01.1974', 'Тридцатое января 1974'), ('25.09.1968', 'Двадцатьпятое сентября 1968'),
                                    ('02.05.1972', 'Второе мая 1972'), ('21.12.1948', 'Двадцатьпервое декабря 1948'),
                                    ('11.08.1983', 'Одиннадцатое августа 1983'), ('09.02.1981', 'Девятое февраля 1981'),
                                    ('12.11.1980', 'Двенадцатое ноября 1980'), ('02.04.1962', 'Второе апреля 1962')])

random_hollywood_actors = random.sample(list(hollywood_actor_names.items()), 5)

can_restart = False

def victorina():
    count_correct_answer = 0
    count_incorrect_answer = 0

    print('Приветствую в нашей викторине ! Сейчас, выберет 5 из 10 знаменитостей абсолютно случайно.')
    print('Вам необходимо угадать полную дату рождения этих людей. ')
    print('Желаем вам удачи !')

    for actor in random_hollywood_actors:
        age = input('Актёр ' + actor[0] + ' сколько ему лет ? ')
        if (age != str(actor[1])):
            count_incorrect_answer += 1
            print('Не верно. ')
            print('Правильный ответ - ' + hollywood_actor_birthday_map.get(actor[1]))
            continue

        count_correct_answer += 1
        print('Верно')

    print()
    print('Вот и подошла к концу наша викторина. \n')

    print('Всего было вопросов - ' + str(len(random_hollywood_actors)))
    print('Количество правильных ответов - ' + str(count_correct_answer))
    print('Процент правильных ответов - ' + str(round(count_correct_answer * 100 / len(random_hollywood_actors), 2)))
    print('Количество не правильных ответов - ' + str(count_incorrect_answer))
    print(
        'Процент не правильных ответов - ' + str(round(count_incorrect_answer * 100 / len(random_hollywood_actors), 2)))

    print()
    can_restart_answer = input('Хотите попробовать ещё раз ? (Да\Нет) ')

    if (can_restart_answer == 'Да'):
        victorina()
    else:
        return

victorina()

