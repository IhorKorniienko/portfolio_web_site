# custom function:
FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    # Doc string:
    """ Read a text file and return
    the list of to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write to-do item list in the file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("The text is:")
    print(get_todos())

# to read the documentation :
#print(get_todos.__doc__)
#print(write_todos.__doc__)
