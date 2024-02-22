#!/usr/bin/python3

"""
This is a python script that uses REST API for
a given employee ID, returns information about
his/her TODO list progress.

The script must display the following;
1) EMPLOYEE_NAME: name of the employee
2) NUMBER_OF_DONE_TASKS: number of completed tasks
3) TOTAL_NUMBER_OF_TASKS: total number of tasks [completed + non-completed]
4) Second and N next lines display the title of completed tasks.
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: python script.py <employee_id>")
        exit(1)

    session = requests.Session()

    # u_id is the employee ID
    u_id = argv[1]
    idURL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(u_id)
    nameURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(u_id)

    employee = session.get(idURL)
    employeeName = session.get(nameURL)

    json_requests = employee.json()
    name = employeeName.json()['name']

    total_tasks = 0

    for completed_tasks in json_requests:
        if completed_tasks['completed']:
            total_tasks += 1

    print("Employee {} is done with tasks({}/{}):".
          format(name, total_tasks, len(json_requests)))

    for completed_tasks in json_requests:
        if completed_tasks['completed']:
            print("\t " + completed_tasks.get('title'))
