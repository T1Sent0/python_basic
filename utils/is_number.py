def is_number(input):
    """
    Функция проверки на число
    :param input: any
    :return: bool
    """
    try:
        int(input)
        return True
    except:
        return False