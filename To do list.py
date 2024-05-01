import json
import datetime

# Data Structure
tasks = []

# File Handling
def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks():
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

# Task Functions
def add_task():
    description = input("Enter task description: ")
    priority = input("Enter priority (high, medium, low): ")
    due_date_str = input("Enter due date (YYYY-MM-DD): ")
    due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d").date()
    tasks.append({"description": description, "priority": priority, "due_date": due_date_str, "completed": False})
    save_tasks()
    print("Task added!")

def remove_task():
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task['description']}")
    choice = int(input("Enter task number to remove: ")) - 1
    del tasks[choice]
    save_tasks()
    print("Task removed!")

def mark_complete():
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task['description']}")
    choice = int(input("Enter task number to mark complete: ")) - 1
    tasks[choice]["completed"] = True
    save_tasks()
    print("Task marked as complete!")

def view_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        for task in tasks:
            status = "Completed" if task["completed"] else "Pending"
            print(f"Description: {task['description']}, Priority: {task['priority']}, Due Date: {task['due_date']}, Status: {status}")

# Main Loop
while True:
    print("\nTo-Do List")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Mark Complete")
    print("4. View Tasks")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        remove_task()
    elif choice == '3':
        mark_complete()
    elif choice == '4':
        view_tasks()
    elif choice == '5':
        break
    else:
        print("Invalid choice.")

# Load tasks from file on startup
tasks = load_tasks()