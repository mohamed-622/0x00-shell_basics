#!/usr/bin/python3
""" Python script to export data in the CSV format """
import csv
import requests
from sys import argv


if __name__ == "__main":
    user_id = argv[1]
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    # Get the user's username
    user_data = requests.get(url).json()
    username = user_data.get("username")

    # Get the user's todos
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    todos = requests.get(todos_url).json()

    # Write the data to a CSV file
    with open(f"{user_id}.csv", mode="w", newline="") as f:
        csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for todo in todos:
            csv_writer.writerow([user_id, username,
                                 todo.get("completed"), todo.get("title")])
