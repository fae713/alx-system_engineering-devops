#!/usr/bin/python3
"""
Exporting the data to JSON format
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: python script.py <employee_id>")
        exit(1)

    session = requests.Session()

    # u_id is the Employee ID.
    u_id = argv[1]
    idURL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(u_id)
    nameURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(u_id)

    employee = session.get(idURL)
    employeeName = session.get(nameURL)

    json_requests = employee.json()

    totalTasks = []

    userData = {}

    for todo in json_requests:
        totalTasks.append(
                {
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                    "username": employeeName.json()['username'],
                })
    userData[u_id] = totalTasks

    with open(f"{u_id}.json", "w") as USER_ID:
        json.dump(userData, USER_ID)
