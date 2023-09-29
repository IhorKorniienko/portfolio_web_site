# from functions import get_todos, write_todos

import functions
import time

time_now = time.strftime("%b %d, %Y %H:%M:%S")
print("Date & Time: ", time_now)

while True:
    user_action = input("Enter add, edit, show, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        # List comprehension
        # [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}.{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter a new item to edit the old one: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("You entered an invalid command!")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"The item: '{todo_to_remove}' is removed from the ToDo list"
            print(message)
        except IndexError:
            print("There's no item with such number.")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid, please try again!")

print("Have a great day!")


