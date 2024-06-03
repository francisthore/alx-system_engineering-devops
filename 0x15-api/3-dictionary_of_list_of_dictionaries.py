#!/usr/bin/python3
"""
Retrieves data from an API and creates
a json of all the data
"""

import json
import requests

if __name__ == '__main__':
    emp_url = 'https://jsonplaceholder.typicode.com/users/'
    with requests.get(emp_url) as request:
        users = request.json()
    if users:
        data = {}
        for user in users:
            id = user.get('id')
            username = user.get('username')
            tasks_url = '{}{}/todos'.format(emp_url, id)
            with requests.get(tasks_url) as request:
                tasks = request.json()
            if tasks:
                tasks_list = []
                for task in tasks:
                    task_dict = {}
                    task_dict['username'] = username
                    task_dict['task'] = task.get('title')
                    task_dict['completed'] = task.get('completed')
                    tasks_list.append(task_dict)
            data[id] = tasks_list
        with open('todo_all_employees.json', 'w') as file:
            json.dump(data, file)
