#!/usr/bin/python3
"""Script to fetch employee's TODO list progress info
from the JSONPlaceholder API and save it on an CSV formatted file.
"""
from requests import get
from sys import argv
from csv import (writer, QUOTE_ALL)

if __name__ == '__main__':
    employee_id = argv[1]
    url_user_info = 'https://jsonplaceholder.typicode.com/users/{}'
    url_todos_info = 'https://jsonplaceholder.typicode.com/todos'
    query_todos = {'userId': employee_id}
    user_data = get(url_user_info.format(employee_id)).json()
    todo_data = get(url_todos_info, params=query_todos).json()
    username = user_data.get('name')
    filename = '{}.csv'.format(employee_id)
    with open(filename, 'w') as output_file:
        csv_writer = writer(output_file, delimiter=',', quoting=QUOTE_ALL)
        for task in todo_data:
            csv_writer.writerow([employee_id, username, task.get(
                'completed'), task.get('title')])
