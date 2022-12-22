import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            index = index + 1
            row = f'{index}.{item}'
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("What should this todo be? :")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            todos = functions.get_todos()

            done_todo = int(user_action[9:])
            index = done_todo - 1
            todo_removed = todos[index].strip('\n')
            # removes the break line for the message in line 62
            todos.pop(index)

            functions.write_todos(todos)

            message = f'The todo {todo_removed} was removed from the list of todos.'
            print(message)
        except ValueError:
            print("There is no todo with that number.")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid!")
print("Bye!")
