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

import sys
import json
import requests


if __name__ == "__main__":
    session = requests.Session()

    url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]
    employee_id_param = {'userid': employee_id}
    employee_res = session.get(url + "user/{}".format(employee_id))
    employee = employee_res.json()
    todos_res = session.get(url + "todos", params=employee_id_param)
    todos = todos_res.json()

    completed = []

    for todo in todos:
        if todo.get("completed") is True:
            completed.append(todo.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(
        employee.get("name"), len(completed), len(todos)))

    [print("\t {}".format(complete)) for complete in completed]
