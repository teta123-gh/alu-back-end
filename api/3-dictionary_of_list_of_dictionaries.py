#!/usr/bin/python3
"""
Exports all employees' TODO list data to a JSON file.
"""
import json
import requests


if __name__ == "__main__":
    # Fetch all users
    users_url = "https://jsonplaceholder.typicode.com/users"
    users_response = requests.get(users_url, timeout=10)
    users = users_response.json()

    # Fetch all todos
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    todos_response = requests.get(todos_url, timeout=10)
    todos = todos_response.json()

    # Organize tasks by user
    all_tasks = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")

        user_tasks = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in todos if task.get("userId") == user_id
        ]

        all_tasks[str(user_id)] = user_tasks

    # Export to JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file)
