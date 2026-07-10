#!/usr/bin/python3
"""Export to JSON - all employees.

This module fetches the TODO list of all employees from the
JSONPlaceholder REST API and exports every task to a single JSON
file named todo_all_employees.json.
"""
import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    users_url = "{}/users".format(base_url)
    users = requests.get(users_url).json()

    all_tasks = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")

        todos_url = "{}/users/{}/todos".format(base_url, user_id)
        todos = requests.get(todos_url).json()

        tasks = []
        for task in todos:
            tasks.append({
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            })

        all_tasks[str(user_id)] = tasks

    filename = "todo_all_employees.json"
    with open(filename, "w") as json_file:
        json.dump(all_tasks, json_file)
