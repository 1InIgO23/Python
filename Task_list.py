task_list = [] #The list must be empty from the beginning

remove = ""
add = ""
selection = ""
choice = ""
completed_or_not = "" #The variables must be empty from the beginnig
k = ""
n = ""


def remove_():
    try:
        remove = input("Enter the element to be removed: ")
        task_list.remove(remove)
        print(task_list)
    except ValueError:
        print(str(remove) + " is not the list.")

def add_():
    add = input("Enter the element to be added: ")
    task_list.append(add)
    print(task_list)

def select():
    try:
        selection = int(input("Select element index: "))
        print("The element " + str(task_list[selection]) + " has been selected.")
        completed_or_not = input("Type Y for completed or N for not completed: ")
        if completed_or_not == "Y":
            task_list[selection] += "(Completed)"
        elif completed_or_not == "N":
            k = "(Completed)"
            string = task_list[selection]
            new_string = string.replace(k, "")
            task_list[selection] = new_string
        else:
            print("Invalid input")
        print(task_list)
    except IndexError:
        print("Invalid index.")

def clear():
    task_list = []
    print(task_list)

def invalid_input():
    print("Invalid input")
    print(task_list)

print(task_list)

while True:
    i = input("Add, remove, select or clear: ")
    if i == "add" or i == "Add":
        add_()
    elif i == "remove" or i == "Remove":
        remove_()
    elif i == "select" or i == "Select":
        select()
    elif i == "clear" or i == "Clear":
        task_list = []
        print(task_list)
    else:
        invalid_input()
