#!/usr/bin/python3
"""Python script to export data in the CSV format"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    """Prevent execution of this code when imported"""
    url = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]
    user = requests.get(url + "users/" + user_id).json()
    todos = requests.get(url + "todos?userId=" + user_id).json()
    with open("{}.csv".format(user_id), "w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([user_id,user.get("username"),
                             task.get("completed"),task.get("title")])
