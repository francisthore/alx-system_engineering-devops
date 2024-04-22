#!/usr/bin/python3
"""Collects data from an api"""

if __name__ == "__main__":
    import requests
    from sys import argv
    user_url = 'https://jsonplaceholder.typicode.com/users/{}/'.format(argv[1])
    todo_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        argv[1])
    user_request = requests.get(user_url)
    todo_request = requests.get(todo_url)
    try:
        user_response = user_request.json()
        todo_response = todo_request.json()
        i = 0
        for task in todo_response:
            if task['completed'] is True:
                i = i + 1
        name = user_response['name']
        print('Employee {} is done with tasks({}/{}):'.format(
            name,
            i, len(todo_response)
        ))
        for task in todo_response:
            if task['completed'] is True:
                print('\t{}'.format(task['title']))
    except Exception as e:
        print(e)
