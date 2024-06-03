#!/usr/bin/python3
"""
Retrieves data from an API and exports
it to json
"""
import json
import requests
from sys import argv

if __name__ == '__main__':
    emp_id = argv[1]
    task_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        emp_id)
    emp_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(emp_id)

    with requests.get(task_url) as request:
        todos = request.json()
    with requests.get(emp_url) as request:
        emp = request.json()

    if todos and emp:
        username = emp.get('username')
        tasks_list = []
        data = {}
        for task in todos:
            task_dict = {}
            task_dict['task'] = task.get('title')
            task_dict['completed'] = task.get('completed')
            task_dict['username'] = username
            tasks_list.append(task_dict)
        data[emp_id] = tasks_list
        with open('{}.json'.format(emp_id), 'w') as file:
            json.dump(data, file)
