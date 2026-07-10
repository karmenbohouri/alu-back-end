#!/usr/bin/python3
"""Export to JSON.

This module fetches an employee's TODO list from the JSONPlaceholder
REST API and exports all of their tasks to a JSON file named
USER_ID.json.
"""
import json
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

    tasks = []
    for task in todos:
        tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    json_data = {str(user_id): tasks}

    filename = "{}.json".format(user_id)
    with open(filename, "w") as json_file:
        json.dump(json_data, json_file)
