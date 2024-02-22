#!/usr/bin/python3
"""
Export the api data to CSV format
"""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) < 2:
        print("Missing <employee_id>")
        exit(1)

    session = requests.Session()

    # u_id is the Employee ID.
    u_id = argv[1]
    idURL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(u_id)
    nameURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(u_id)

    employee = session.get(idURL)
    employeeName = session.get(nameURL)

    json_requests = employee.json()

    with open(f"{u_id}.csv", "w", newline='') as csvfile:

        csvwriter = csv.writer(csvfile, delimiter=',',
                               quotechar='"', quoting=csv.QUOTE_ALL)

        for todo in json_requests:
            csvwriter.writerow([u_id, employeeName.json()['username'],
                               todo.get("completed"), todo.get("title")])
