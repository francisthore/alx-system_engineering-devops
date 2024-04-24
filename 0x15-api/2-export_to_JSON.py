#!/usr/bin/python3
"""Collects data from an api"""

if __name__ == "__main__":
    import requests
    from sys import argv
    import json

    user_id = argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}/'.format(user_id)
    todo_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        argv[1])
    user_response = requests.get(user_url).json()
    todo_response = requests.get(todo_url).json()
    file_path = '{}.json'.format(user_id)
    try:
        user_name = user_response.get('username')
        json_arr = []
        user_id_json = {}
        for task in todo_response:
            row = {}
            row['task'] = task['title']
            row['completed'] = task['completed']
            row['username'] = user_name
            json_arr.append(row)
        user_id_json[user_id] = json_arr
        with open(file_path, 'w') as file:
            json.dump(user_id_json, file)
    except Exception as e:
        print(e)
