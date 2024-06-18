#!/usr/bin/python3
"""
Retrieves a TODO list progress for a
given employee ID
Usage: ./module <id>
"""

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
        total_tasks = len(todos)
        tasks_completed = [task for task in todos if task['completed'] is True]
        emp_name = emp.get('name')
        print('Employee {} is done with tasks({}/{}):'.format(
            emp_name, len(tasks_completed), total_tasks
        ))
        for task in tasks_completed:
            print('\t {}'.format(task.get('title')))
