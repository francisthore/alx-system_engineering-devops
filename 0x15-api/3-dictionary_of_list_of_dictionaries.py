#!/usr/bin/python3
"""Collects data from an api"""

if __name__ == "__main__":
    import requests
    import json

    users_url = 'https://jsonplaceholder.typicode.com/users/'
    user_response = requests.get(users_url).json()
    file_path = 'todo_all_employees.json'
    url_prefix = 'https://jsonplaceholder.typicode.com/users/'
    try:
        all_users_todo = {}
        for user in user_response:
            user_tasks = []
            user_id = user.get('id')
            user_name = user.get('username')
            todos_url = '{}{}/todos'.format(url_prefix, user_id)
            todos_response = requests.get(todos_url).json()
            for task in todos_response:
                row = {}
                row['username'] = user_name
                row['task'] = task['title']
                row['completed'] = task['completed']
                user_tasks.append(row)
            all_users_todo[user_id] = user_tasks
            with open(file_path, 'w') as file:
                json.dump(all_users_todo, file)
    except Exception as e:
        print(e)
