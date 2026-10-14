from storage import save_task, load_task
from datetime import datetime

def add_task(task_description: str, tasks: dict[str, dict[str, str]]) -> str:

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
    return save_task(tasks)


def generate_id(last_id): return last_id + 1

if __name__ == "__main__":
    print(add_task("add rice", {
    "1": {
        "id": 1,
        "description": "add beans",
        "status": "todo",
        "createdAt": "2026-10-14 16:45:30",
        "updatedAt": "2026-10-14 16:45:30"
    }
}))
    