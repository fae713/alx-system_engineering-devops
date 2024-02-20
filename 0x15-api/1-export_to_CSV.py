#!/usr/bin/python3
"""
Extending my python script to CSV format
"""

from sys import argv
import requests
import csv

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

    with open(f"{u_id}.csv", "w", newline='') as USER_ID:

        csvwriter = csv.writer(USER_ID, delimiter=',',
                               quotechar='"', quoting=csv.QUOTE_ALL)

        #csvwriter.writerow(["USER_ID", "USERNAME",
         #                  "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for todo in json_requests:
            csvwriter.writerow([u_id, employeeName.json()['username'],
                               todo.get("completed"), todo.get("title")])
