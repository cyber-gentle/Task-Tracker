from typing import Any
import json

def save_task(tasks: dict[int, dict[str, Any]]) -> str:
    if not tasks:
        return "Task cannot be empty"
    try:
        with open("tasks.json", "w") as f:
            json.dump(tasks, f, indent=4)
        return "success"
    except Exception as e:
        return str(e)


def load_task() -> tuple[dict[int, dict[str, Any]], str]:
    
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
            return tasks, ""
    except FileNotFoundError:
        return {}, "created a new dictionary"
    except Exception as err:
        return {}, str(err)

