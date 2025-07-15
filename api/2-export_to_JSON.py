#!/usr/bin/python3
"""
Exports employee TODO list data to JSON format.
"""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Fetch user info
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url, timeout=10)
    if user_response.status_code != 200:
        print("Employee not found.")
        sys.exit(1)

    username = user_response.json().get("username")

    # Fetch TODOs
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    todos_response = requests.get(
        todos_url, params={"userId": employee_id}, timeout=10
    )
    todos = todos_response.json()

    # Format data
    tasks = []
    for task in todos:
        tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    output = {str(employee_id): tasks}

    # Write to JSON file
    filename = f"{employee_id}.json"
    with open(filename, mode="w") as json_file:
        json.dump(output, json_file)
