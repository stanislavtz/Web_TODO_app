def get_todos(file_path):
    """
    Reads all the todos from a file and returns a list of todos.
    If the file not exist it prints "File Not Found" and returns an empty list.
    """
    try:
        with open(file_path, "r") as file:
            todos_list = file.readlines()
        return todos_list
    except FileNotFoundError:
        print("File Not Found!")
        return []


def add_todo(file_path, todo_to_add):
    """ Adds new task and save it in the file. """
    with open(file_path, "a") as file:
        file.write(todo_to_add.capitalize())


def save_todos(file_path, todos_list):
    """ Saves all the todos in the file. """
    with open(file_path, "w") as file:
        file.writelines(todos_list)
