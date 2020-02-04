#!/usr/bin/python3
"""Script to fetch all employee's TODO list progress info
from the JSONPlaceholder API and save it on a JSON formatted file.
"""
from json import dump
from requests import get

if __name__ == '__main__':
    url_user_info = 'https://jsonplaceholder.typicode.com/users'
    url_todos_info = 'https://jsonplaceholder.typicode.com/todos'
    user_data = get(url_user_info).json()
    todo_data = get(url_todos_info).json()
    with open('todo_all_employees.json', 'w') as output_file:
        data = dict()
        for user in user_data:
            user_id = user.get('id')
            username = user.get('username')
            user_tasks = list(
                filter(
                    lambda task:
                    task.get('userId') == user_id,
                    todo_data
                )
            )
            tasks_data = [
                {'username': username,
                 'task': task.get('title'),
                 'completed': task.get('completed')
                 }
                for task in user_tasks
            ]
            data[user_id] = tasks_data
        dump(data, output_file)
