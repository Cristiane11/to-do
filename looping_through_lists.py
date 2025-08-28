tasks= ["do Homework", "Go to the Gym", " Groceries", "Go to Pool"]
#Method 1:
print("\nMETHOD 1:")
for task in tasks:
    print(task)
print(tasks[0])
print(tasks[1])
print(tasks[2])

#Method 2:
print("\nMETHOD 2:")
for i  in range(len(tasks)):
    print(tasks[i])

#Method 3:

print("\nMETHOD 3:")
for i  in range(len(tasks)):
   # print(f"{i}-{tasks[i]}")
    print(f"{i + 1}.{tasks[i]}")

#Method 4:
print("\nMETHOD 4:")
for i, task  in enumerate(tasks, 1):
    print(f"{i}.{task}")