from storage import save_task, load_task
from datetime import datetime
from typing import Any

def add_task(task_description: str, tasks: dict[str, dict[str, Any]]) -> str:

    if not isinstance(task_description, str):
        return "task description must be a string"
    
    if not isinstance(tasks, dict):
        return "tasks on memory must a dictionary"

    if not tasks:
        next_id = 1
    else:
        last_id = int(next(reversed(tasks)))
        next_id = generate_id(last_id)

    task = {
        "id" : next_id,
        "description" : task_description,
        "status": "todo",
        "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updatedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    tasks[next_id] = task
    message = save_task(tasks)
    if message == "success":
        return "Ticket saved successfully"
    return message


def generate_id(last_id): return last_id + 1

def update_task(task_id: str, new_description: str, tasks: dict[str, dict[str, Any]]) -> str:
    if not tasks:
        return "No available tasks to update"

    if not isinstance(task_id, str):
        return "Task ID must be a string"

    if not isinstance(new_description, str):
        return "New task description must be a string"

    task = tasks.get(task_id, f"No task with ID: {task_id}")

    if not isinstance(task, dict):
        return task
        
    task["description"] = new_description
    task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = save_task(tasks)
    if message == "success":
        return f"Task with ID: {task_id} updated successfully"
    return message


def delete_task(task_id: str, tasks: dict[str, dict[str, Any]]) -> str:
    if not isinstance(task_id, str) or not task_id:
        return "Task ID must be a non-empty string"
    
    if not tasks:
        return "No available task to delete"
    
    if task_id not in tasks:
        return f"No task with ID: {task_id} found"

    deleted_task = tasks.pop(task_id)
    message = save_task(tasks)
    if message == "success":
        return f"""
Task with ID: {task_id} deleted successfully
-----------------------------------------------
Task Details:
ID: {deleted_task["id"]}
Description: {deleted_task["description"]}
Status: {deleted_task["status"]}
Last Updated: {deleted_task["updatedAt"]}
"""
    return message