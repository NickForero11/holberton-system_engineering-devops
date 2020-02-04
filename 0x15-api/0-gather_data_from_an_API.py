#!/usr/bin/python3
"""Script to fetch employee's TODO list progress info
from the JSONPlaceholder API.
"""
from requests import get
from sys import argv


if __name__ == '__main__':
    employee_id = int(argv[1])
    url_user_info = 'https://jsonplaceholder.typicode.com/users/{}'
    url_todos_info = 'https://jsonplaceholder.typicode.com/todos'
    query_todos = {'userId': employee_id}
    user_data = get(url_user_info.format(employee_id)).json()
    todo_data = get(url_todos_info, params=query_todos).json()
    username = user_data.get('name')
    number_of_tasks = len(todo_data)
    tasks_done = list(filter(lambda task: task.get('completed'), todo_data))
    number_of_done_tasks = len(tasks_done)
    first_line = 'Employee {} is done with tasks({}/{}):'
    print(first_line.format(username, number_of_done_tasks, number_of_tasks))
    for task in tasks_done:
        print('\t {}'.format(task.get('title')))
