# Initialize an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task():
    task_description = input("Enter task description: ")
    tasks.append({"description": task_description, "done": False})

# Function to list tasks
def list_tasks():
    print("To-Do List:")
    for index, task in enumerate(tasks):
        status = "Done" if task["done"] else "Not Done"
        print(f"{index + 1}. {task['description']} - {status}")

# Function to mark a task as done
def mark_task_done():
    list_tasks()
    task_index = int(input("Enter the task number to mark as done: ")) - 1
    
    if 0 <= task_index < len(tasks):
        tasks[task_index]["done"] = True
        print("Task marked as done.")
    else:
        print("Invalid task number.")

def delete_task():
    list_tasks()
    task_index = int(input("Enter the task number to delete: ")) - 1
    
    if 0 <= task_index < len(tasks):
        deleted_task = tasks.pop(task_index)
        print(f"Task '{deleted_task['description']}' deleted.")
    else:
        print("Invalid task number.")

import json

# Function to save tasks to a file
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

# Function to load tasks from a file
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Load tasks when the program starts
tasks = load_tasks()
4
# Main loop
while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task as Done")
    print("4. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        mark_task_done()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
