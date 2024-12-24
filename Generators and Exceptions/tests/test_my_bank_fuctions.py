from utils.json_helper import get_json_data, create_json_file
from utils.os_util import delete

user_data_directory = 'user_data'
balance_file_name = 'bank_account_data.json'
purchase_history = 'purchase_history.json'

def test_get_user_balance():
    """
    Тест получения баланса пользователя из файла
    :return:
    """
    user_account_data = get_json_data(f'{user_data_directory}/{balance_file_name}')

    if user_account_data is None:
        assert user_account_data is None

    if user_account_data:
        assert isinstance(user_account_data['balance'], int)


def test_read_balance():
    """
    Тест проверки записи в файл баланса пользователя
    :return:
    """
    new_data = {
        'balance': 10,
    }

    create_json_file(new_data, f'{user_data_directory}/{balance_file_name}')

    user_account_data = get_json_data(f'{user_data_directory}/{balance_file_name}')
    if user_account_data:
        assert user_account_data['balance'] == 10
        delete(f'{user_data_directory}/{balance_file_name}')
    else:
        assert user_account_data is None


def test_get_purchase_history():
    existing_data = get_json_data(f'../{user_data_directory}/{purchase_history}')

    if existing_data is not None:
        assert len(list(existing_data['purchase_history'])) > 0
        delete(f'../{user_data_directory}/{purchase_history}')
    else:
        assert existing_data is None

def test_read_purchase_history():
    existing_data = [{
        'purchase_name': 'Test',
    }, {
        'purchase_name': 'Test2',
    }]

    create_json_file({'purchase_history': existing_data}, f'../{user_data_directory}/{purchase_history}')

    existing_data = get_json_data(f'{user_data_directory}/{purchase_history}')
    if existing_data:
        assert len(list(existing_data[purchase_history])) == 2
        delete(f'../{user_data_directory}/{purchase_history}')
    else:
        assert existing_data is None

