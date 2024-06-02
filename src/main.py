from api_utils import get_users, get_todos

def is_user_in_fancode_city(user):
    lat = float(user['address']['geo']['lat'])
    lng = float(user['address']['geo']['lng'])
    return -40 < lat < 5 and 5 < lng < 100

def get_fancode_users(users):
    return [user for user in users if is_user_in_fancode_city(user)]

def calculate_completion_percentage(user, todos):
    user_todos = [todo for todo in todos if todo['userId'] == user['id']]
    completed_todos = [todo for todo in user_todos if todo['completed']]
    if not user_todos:
        return 0
    return len(completed_todos) / len(user_todos) * 100

def check_fancode_users_task_completion():
    users = get_users()
    todos = get_todos()
    fancode_users = get_fancode_users(users)

    for user in fancode_users:
        print(f"User {user['id']} {user['name']} does  meet the fancode city criteria.")

        completion_percentage = calculate_completion_percentage(user, todos)
        if completion_percentage <= 50:
            print(f"User {user['id']} {user['name']} does not meet the task completion criteria.")
        else:
            print(f"User {user['id']} {user['name']} meets the task completion criteria.")

if __name__ == "__main__":
    check_fancode_users_task_completion()
