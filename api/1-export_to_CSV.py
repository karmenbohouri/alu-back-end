#!/usr/bin/python3
"""Export to CSV.

This module fetches an employee's TODO list from the JSONPlaceholder
REST API and exports all of their tasks to a CSV file named
USER_ID.csv.
"""
import csv
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    base_url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(base_url, employee_id)
    todos_url = "{}/todos".format(user_url)

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    user_id = user.get("id")
    username = user.get("username")

    filename = "{}.csv".format(user_id)
    with open(filename, "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                user_id,
                username,
                task.get("completed"),
                task.get("title")
            ])
            