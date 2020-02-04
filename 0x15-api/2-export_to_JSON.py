#!/usr/bin/python3
"""Script to fetch employee's TODO list progress info
from the JSONPlaceholder API and save it on an JSON formatted file.
"""
from requests import get
from sys import argv
from json import dump

if __name__ == '__main__':
    employee_id = argv[1]
    url_user_info = 'https://jsonplaceholder.typicode.com/users/{}'
    url_todos_info = 'https://jsonplaceholder.typicode.com/todos'
    query_todos = {'userId': employee_id}
    user_data = get(url_user_info.format(employee_id)).json()
    todo_data = get(url_todos_info, params=query_todos).json()
    username = user_data.get('username')
    filename = '{}.json'.format(employee_id)
    with open(filename, 'w') as output_file:
        tasks_data = [{'task': task.get('title'), "completed": task.get('completed'), 'username': username} for task in todo_data]
        data = {employee_id: tasks_data}
        dump(data, output_file)
