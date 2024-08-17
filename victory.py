hollywood_actor_names = dict([('Джонни Депп', 61), ('Роберт Дауни-младший', 59),
                              ('Кристиан Бэйл', 50), ('Уиллард Кэрролл Смит Второй', 55),
                              ('Дуэйн Джонсон', 52), ('Сэмюэл Л. Джексон', 74)])
length_hollywood_actor_names = len(hollywood_actor_names)
can_restart = False

def victorina():
    count_correct_answer = 0
    count_incorrect_answer = 0

    print('Приветствуем тебя в нашей викторине.');
    print('Сейчас мы зададим тебе несколько вопросов о знаменитосях постарайся отвечать правильно  удачи !!')

    for actor in hollywood_actor_names.items():
        age = input('Актёр ' + actor[0] + ' сколько ему лет ? ')
        if (age != str(actor[1])):
            count_incorrect_answer += 1
            print('Не верно')
            continue

        count_correct_answer += 1
        print('Верно')

    print()
    print('Вот и подошла к концу наша викторина. \n')

    print('Всего было вопросов - ' + str(length_hollywood_actor_names))
    print('Количество правильных ответов - ' + str(count_correct_answer))
    print('Процент правильных ответов - ' + str(round(count_correct_answer * 100 / length_hollywood_actor_names, 2)))
    print('Количество не правильных ответов - ' + str(count_incorrect_answer))
    print(
        'Процент не правильных ответов - ' + str(round(count_incorrect_answer * 100 / length_hollywood_actor_names, 2)))

    print()
    can_restart_answer = input('Хотите попробовать ещё раз ? (Да\Нет) ')

    if (can_restart_answer == 'Да'):
        victorina()
    else:
        return

victorina()
