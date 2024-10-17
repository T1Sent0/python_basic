"""
    Тесты для функции filter
"""


def is_positive(num):
    return num > 0


def is_negative(num):
    return num < 0


def is_even(num):
    return num % 2 == 0


def test_filter_is_positive():
    numbers = [-1, 2, -3, 4, 5]
    excepted_positive_result = [2, 4, 5]

    assert list(filter(is_positive, numbers)) == excepted_positive_result


def test_filter_is_negative():
    numbers = [-1, 2, -3, 4, 5]
    excepted_negative_result = [-1, -3]

    assert list(filter(is_negative, numbers)) == excepted_negative_result


def test_filter_is_even():
    numbers = [-1, 2, -3, 4, 5, 6]
    excepted_even_result = [2, 4, 6]

    assert list(filter(is_even, numbers)) == excepted_even_result


""""""

"""
    Тесы для функции map
"""


def square(x):
    return x * x


def test_map_square():
    input_data = [1, 2, 3, 4]
    expected_output = [1, 4, 9, 16]
    result = list(map(square, input_data))
    assert result == expected_output


def test_map_with_empty_list():
    input_data = []
    expected_output = []
    result = list(map(square, input_data))
    assert result == expected_output


def test_map_with_negative_numbers():
    input_data = [-1, -2, -3]
    expected_output = [1, 4, 9]
    result = list(map(square, input_data))
    assert result == expected_output


""""""
"""
    Тесты для функции sorted
"""


def test_sorted_basic():
    input_data = [4, 2, 3, 1]
    expected_output = [1, 2, 3, 4]
    result = sorted(input_data)
    assert result == expected_output


def test_sorted_empty_list():
    input_data = []
    expected_output = []
    result = sorted(input_data)
    assert result == expected_output


def test_sorted_with_strings():
    input_data = ["banana", "apple", "cherry"]
    expected_output = ["apple", "banana", "cherry"]
    result = sorted(input_data)
    assert result == expected_output


def test_sorted_with_reverse():
    input_data = [1, 2, 3, 4]
    expected_output = [4, 3, 2, 1]
    result = sorted(input_data, reverse=True)
    assert result == expected_output


def test_sorted_with_key():
    input_data = ["banana", "apple", "cherry"]
    expected_output = ["apple", "banana", "cherry"]
    result = sorted(input_data, key=len)
    assert result == expected_output
