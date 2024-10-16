def show_tasks(tasks):
    print("\nTo-Do List:")
    for idx, task in enumerate(tasks, 1):
        status = "Done" if task['completed'] else "Not Done"
        print(f"{idx}. {task['title']} [{status}]")
    print()

def add_task(tasks):
    title = input("Enter the task title: ")
    tasks.append({"title": title, "completed": False})

def mark_task_completed(tasks):
    try:
        task_num = int(input("Enter the task number to mark as complete: "))
        tasks[task_num - 1]['completed'] = True
    except (IndexError, ValueError):
        print("Invalid task number!")

def delete_task(tasks):
    try:
        task_num = int(input("Enter the task number to delete: "))
        tasks.pop(task_num - 1)
    except (IndexError, ValueError):
        print("Invalid task number!")

def to_do_list():
    tasks = []
    while True:
        print("1. View tasks\n2. Add task\n3. Mark task as complete\n4. Delete task\n5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    to_do_list()
