def read_file(filepath='todos.txt'):
    """
    Read a text file and return a list of
    to-do items.
    """
    with open(filepath, 'r') as local_file:
        local_todos = local_file.readlines()
    return local_todos


def write_file(todos_args, filepath='todos.txt'):
    """
    Write a new to-do items into the file
    """
    with open(filepath, 'w') as local_file:
        local_file.writelines(todos_args)

