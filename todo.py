# Sample TO-DO list ACM Dev fa25
# With the current implementation, tasks are not saved between runs.
import os

# clearing screen helps with scroller fatigue
def clear_screen():
    os.system('cls') # for windows
    os.system('clear') # for mac and linux
    
    if os.name != 'nt' and os.name != 'posix':
        print("\n" * 100)  # for unsupported OS

tasks = []

def add_task():
    clear_screen()
    print("Add a New Task")
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print(f"'{task}' was added to your list.")
    else:
        print("Task cannot be empty.")
    input("\nPress Enter to return to menu...")

def show_tasks():
    clear_screen()
    print("Your Tasks:\n")
    if not tasks:
        print("Your task list is empty.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    input("\nPress Enter to return to menu...")

def remove_task():
    clear_screen()
    if not tasks:
        print("No tasks to remove.")
        input("\nPress Enter to return to menu...")
        return
    print("Remove a Task\n")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    try:
        num = int(input("\nEnter the task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Removed '{removed}' from your list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
    input("\nPress Enter to return to menu...")

def main():
    while True:
        clear_screen()
        print("===== TO-DO LIST MENU =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Quit")

        choice = input("\nChoose an option (1-4): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            clear_screen()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
            input("\nPress Enter to try again...")

main()