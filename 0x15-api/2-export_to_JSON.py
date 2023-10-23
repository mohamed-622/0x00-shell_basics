#!/usr/bin/python3
""" Python script to export data in the JSON format """
import json
import requests
from sys import argv


if __name__ == "__main__":
    """Prevent execution of this code when imported"""
    url = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]
    user = requests.get(url + "users/" + user_id).json()
    todos = requests.get(url + "todos?userId=" + user_id).json()
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")} for task in todos]}, jsonfile)
