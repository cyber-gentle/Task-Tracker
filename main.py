import sys
from storage import load_task, save_task
from tasks import add_task, update_task, delete_task, status_marker, list_all_tasks, list_by_status

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print("Invalid number of arguments. Usage: python3 main.py <command> [args]")
        return
        
    command = sys.argv[1].lower()
    tasks, message = load_task()
    
    if message:
        print(message)

    match command:
        case _ if command == "add" and len(sys.argv) == 3:
            task_description = sys.argv[2]
            print(add_task(task_description, tasks))
            
        case _ if command == "update" and len(sys.argv) == 4:
            task_id = str(sys.argv[2])
            new_description = str(sys.argv[3])
            print(update_task(task_id, new_description, tasks))

        case _ if command == "delete" and len(sys.argv) == 3:
            task_id = str(sys.argv[2])
            print(delete_task(task_id, tasks))

        case _ if command in ("mark-in-progress", "mark-done", "mark-todo") and len(sys.argv) == 3:
            task_id = str(sys.argv[2])

            match command:
                case "mark-todo":
                    print(status_marker(task_id, "todo", tasks))
                case "mark-in-progress":
                    print(status_marker(task_id, "in-progress", tasks))
                case "mark-done":
                    print(status_marker(task_id, "done", tasks))

        case _ if command == "list":
            if len(sys.argv) == 2:
                print(list_all_tasks(tasks))
            elif len(sys.argv) == 3:
                status = str(sys.argv[2])
                print(list_by_status(status, tasks))
            else:
                print("Usage: python3 main.py list [todo|in-progress|done]")

        case _:
            print(f"Unknown command or invalid arguments for '{command}'")


if __name__ == "__main__":
    main()
