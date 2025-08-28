# Create the original list
tasks=["update Austin's file", "Travel", "buy appropriate size "]
# Print Out the List
print(tasks)

# add a new Task to the list
def add_task():
    new_task = input("Enter a new task:")
    #append the ew taskt to the list
    tasks.append(new_task)
    print(f"{new_task} added successfully.")
    #print out the updated List
    print(tasks)
add_task() # call the function to add