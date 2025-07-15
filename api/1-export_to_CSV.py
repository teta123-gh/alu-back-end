#!/usr/bin/python3
"""
Exports employee TODO list data to CSV format.
"""
import csv
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Fetch user info
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url, timeout=10)
    if user_response.status_code != 200:
        print("Employee not found.")
        sys.exit(1)

    user_data = user_response.json()
    username = user_data.get("username")

    # Fetch TODOs
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    todos_response = requests.get(
        todos_url, params={"userId": employee_id}, timeout=10
    )
    todos = todos_response.json()

    # Write to CSV
    filename = f"{employee_id}.csv"
    with open(filename, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])
