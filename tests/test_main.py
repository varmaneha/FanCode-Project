import sys
sys.path.insert(0, './src') 
from main import is_user_in_fancode_city, calculate_completion_percentage

def test_is_user_in_fancode_city():
    user_in_fancode = {
        'address': {'geo': {'lat': '-20.0', 'lng': '50.0'}}
    }
    assert is_user_in_fancode_city(user_in_fancode) is True

    user_not_in_fancode = {
        'address': {'geo': {'lat': '10.0', 'lng': '50.0'}}
    }
    assert is_user_in_fancode_city(user_not_in_fancode) is False

def test_calculate_completion_percentage():
    user = {'id': 1}
    todos = [
        {'userId': 1, 'completed': True},
        {'userId': 1, 'completed': False},
        {'userId': 1, 'completed': True},
        {'userId': 2, 'completed': True}
    ]
    assert calculate_completion_percentage(user, todos) == 66.66666666666666

    user_with_no_todos = {'id': 3}
    assert calculate_completion_percentage(user_with_no_todos, todos) == 0
