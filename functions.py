FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Opens the file containing the todos in
    read mode and returns it as a list. """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Opens the todos list in write mode and takes a list as an arg.
    Writes the new list in filepath. """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("hello")
    print(get_todos())
