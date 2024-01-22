#Ava Marcus
#1/18
#To-Do List #2

x = ["Sour Patch Kids", "Milk Duds", "Kit Kat", "Twix", "Gummy Bears"]
while True:
    option = int(input("1. Add a task to the to-do list\n2. View the current to-do list\n3. Mark a task as completed \n4. Remove a task from the to-do list\n5. Remove all tasks from the to-do list\n6. Sort to-do list in alphabetical order\n7. Display total number of to-do list items\n8. End program"))
    if (option == 1):
        item = input("What would you like to add?")
        x.append(item)
    elif (option == 2):
        print(x)
    elif (option == 3):
        pos = (input("What item do you want to mark complete?"))
        i = x.index(pos)
        x[i] = "✓"
    elif (option == 4):
        y = x.index(input("What item would you like to remove?"))
        x.pop(y)
    elif (option == 5):
        x.clear()
    elif (option == 6):
        x.sort()
    elif (option == 7):
        print(len(x))
    elif (option == 8):
        print("Program Ended.")
        break
    else:
        print("Invalid Input.")
