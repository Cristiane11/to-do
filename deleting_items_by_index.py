tasks = ["do Homework", "Go to the Gym", " Groceries"]



#Method 4:
print("\nMETHOD 4:")
for i, task  in enumerate(tasks, 1):
    print(f"{i}.{task}")
#prompt the user for which task they want to delete. Cast the type to 'integer' .input() returns a string by default.
choice = int(input("Which task do you want to delete?"))
tasks.pop(choice -1)
# tasks.remove(tasks[choice]) My code
print(tasks)