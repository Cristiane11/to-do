tasks=[]

# Function to display option

def display_menu():
    print("1. Add task")
    print("2. View task")
    print("3. Delete task")
    print("4. Quit")

    # Function to add a task to the list.
def add_task():
    try:
        new_task = input("Enter the task: ").strip()
        if new_task == "":
            print("Task cannot be empty.")
        else:
            tasks.append(new_task)
            print(f"{new_task} added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

#Functin to view tasks in the tasks list.
def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    
#Function to Delete all tasks in the tasks list.
def delete_task():
    try:
        if not tasks:
            print("No tasks to delete.")
            return  
        view_tasks()
        choice = int(input("Enter the task number to delete: "))
        if 1 <= choice <= len(tasks):
            removed_task = tasks.pop(choice - 1)
            print(f"{removed_task} deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("write the task to Delete ")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Delete task operation complete.")

    # Main Function of the  application.
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")
#Run the Program
if __name__ == "__main__":
    main()
