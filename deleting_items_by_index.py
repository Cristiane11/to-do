tasks = []
#Function to initialize the list with its three default values.
def initialize_task():
    global tasks
    tasks =["do Homework", "Go to the Gym", " Groceries"]
    print("INITIAL TASKS:" + str(tasks))

#Method 1: remove()
print("\nMETHOD 1:")
initialize_task() 
tasks.remove("do Homework") # can use tasks.pop(0) or tasks.remove("do Homework")
print("Updates TASKS:" + str(tasks))

#Method 2: remove()
print("\nMETHOD 2:")
initialize_task() 
tasks.pop(0) # can use tasks.pop(0) or tasks.remove("do Homework")
print("Updates TASKS:" + str(tasks))

#Method 3: remove()
print("\nMETHOD 3:")
initialize_task() 
del tasks[0] # can use tasks.pop(0) or tasks.remove("do Homework")
print("Updates TASKS:" + str(tasks))

#Bonus Method(not recommended for the project):
...
loop through the list, check if any element contains a particular substring.
Use remove() to remove the element if it does.ZeroDivisionError.ZeroDivisionError
...
print("\nMETHOD 4:")
initialize_task() 
for task in tasks[:]:
    if "homework" in task:
        tasks.remove(task)
 # check for specific task and remove
print("CURRENT List" + str(tasks))