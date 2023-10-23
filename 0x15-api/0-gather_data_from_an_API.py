#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
argument -- an integer representing the employee ID
Return: The employee name and the tasks completed per total tasks.
"""
import requests
from sys import argv


if __name__ == "__main__":
    """Prevent execution of this code when imported"""
    url = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]
    user = requests.get(url + "users/" + user_id).json()
    todos = requests.get(url + "todos?userId=" + user_id).json()
    completed_tasks = []
    for task in todos:
        if task.get("completed") is True:
            completed_tasks.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed_tasks), len(todos)))
    for task in completed_tasks:
        print("\t {}".format(task))
