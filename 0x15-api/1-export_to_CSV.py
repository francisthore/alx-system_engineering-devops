#!/usr/bin/python3
"""Collects data from an api and
exports it to csv"""

if __name__ == "__main__":
    import requests
    from sys import argv
    import csv

    user_id = argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}/'.format(user_id)
    todo_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        argv[1])
    user_response = requests.get(user_url).json()
    todo_response = requests.get(todo_url).json()
    try:
        with open('{}.csv'.format(user_id), 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            user_name = user_response.get('username')
            for task in todo_response:
                row = []
                row.append(task['userId'])
                row.append(user_name)
                row.append(task['completed'])
                row.append(task['title'])
                writer.writerow(row)
    except Exception as e:
        print(e)
