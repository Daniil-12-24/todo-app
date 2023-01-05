from functions import write_file, read_file
import time

import functions # after creating import function add f.e. to read_file() - functions/ functions.read_file()

now = time.strftime('%m %b %Y, %H:%M:%S')
print('Today is', now)

while True:
    user_action = input('type add, show, edit, complete, or exit: ')
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'
        print(f'The todo "{user_action[4:]}" was added successfully')

        todos = read_file()

        todos.append(todo)

        write_file(todos)

    elif user_action.startswith('show'):

        todos = read_file()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f'{index + 1}.{item}'
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = read_file()

            new_todo = input('Enter a new to-do: ')
            todos[number] = new_todo + '\n'

            write_file(todos)

        except ValueError:
            print('Your command is not valid!')
            continue

    elif user_action.startswith('complete'):
        try:
            user_chose = int(user_action[9:])

            todos = read_file()

            index = user_chose - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_file(todos)

            message = f'Todo "{todo_to_remove}" was removed from the list.'
            print(message)

        except IndexError:
            print('There is no such item you are looking for!')
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print('Wrong action. Try again')

print('Bye!')