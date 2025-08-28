
# Function to display option 
def display_menu(): 
    print("1. Add task") 
    print("2. View task") 
    print("3. Delete task") 
    print("4. Quit") 
# Function to add a task to the list.
def add_task(): 
    global tasks 
    new_task = input("Enter the task: ") 
    tasks.append(new_task) 
    print(f"{new_task} added successfully.") 
    print(tasks) 
    #Function to view all tasks in the tasks list. 
def view_task(): 
    print("theis needs to update") 
#Function to Deleteall tasks in the tasks list. 
def delete_task(): 
    print("this Delete to update")
     
# Main Function of the application. 
def main(): 
    while True: 
        display_menu() 
        choice = input("Enter your choice: ") 
        if choice == '1': 
            add_task() 
        elif choice == '2': 
            view_task() 
        elif choice == '3':
            delete_task() 
        elif choice == '4': 
            print("Exiting the application.") 
        break 
    else: print("Invalid choice. Please try again.") 
main()