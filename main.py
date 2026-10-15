import sys
from storage import load_task, save_task
from tasks import add_task, update_task

def main():
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("Length of argument must be 2 or 3")
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

        case _:
            print(f"Unknown command or invalid arguments for '{command}'")


if __name__ == "__main__":
    main()
