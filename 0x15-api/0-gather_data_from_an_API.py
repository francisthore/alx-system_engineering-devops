#!/usr/bin/python3
"""Collects data from an api"""

if __name__ == "__main__":
    import requests
    from sys import argv
    user_url = 'https://jsonplaceholder.typicode.com/users/{}/'.format(argv[1])
    todo_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        argv[1])
    user_response = requests.get(user_url).json()
    todo_response = requests.get(todo_url).json()
    try:
        name = user_response['name']
        completed = [task for task in todo_response if task['completed']]
        print('Employee {} is done with tasks({}/{}):'.format(
            name, len(completed), len(todo_response)
        ))
        for task in completed:
            print('\t{}'.format(task['title']))
    except Exception as e:
        print(e)
