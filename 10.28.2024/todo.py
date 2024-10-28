# A program that allows the user to create a todo list

# this is an empty list to use as the todo
todo = []

def show_todo_list():
    # this will print each item enumarated in its own line
    if len(todo) > 0:
        for i in range(len(todo)):
            print(f"{i + 1} - {todo[i]}")
    else:
        print("There are no items in the todo list, add items first")

# Keep the program running, until the user decides to quite
while True:
    # prompt the user for an action
    print("1. Add an Todo")
    print("2. Complete a Todo")
    print("3. Update Item")
    print("4. Print ToDo List")
    print("5. Quit")

    user_input = input("Enter Choice: ")

    if user_input == "1":
        # prompt the user for the item to add
        item = input("Enter a 'ToDo' to add: ")

        todo.append(item)
        print(f"'{item}' was added to the list")
    elif user_input == "2":
        # show only when the todo has items
        show_todo_list()

        if len(todo) > 0:
            user_choice = int(input(f"Enter the number to remove an item (1 - {len(todo)}): "))

            try:
                # if popping outside of the range, it will throw index error, we need to catch it
                removedItem = todo.pop(user_choice - 1)
                print(f"'{removedItem}' has been completed and removed")
            except IndexError:
                print(f"Invalid Item Index '{user_choice}' to remove")
    elif user_input == "3":
        show_todo_list()

        if len(todo) > 0:
            user_choice = int(input(f"Enter the number to update an item (1 - {len(todo)}): "))

            try:
                item_update = input("Enter the Updated Item: ")
                todo[user_choice - 1] = item_update
                print(f"Item at Index '{user_choice}' has been updated to '{item_update}'")
            except IndexError:
                print(f"Invalid Item Index '{user_choice}' to update")
    elif user_input == "4":
        # This works, prints the representation of the list
        # print(todo)

        show_todo_list()
    elif user_input == "5":
        # this will break the loop
        break
    else:
        pass

    # print an empty space to make it easier to read
    print()

print("Thank you for using our ToDo List Program. Buh bye!")