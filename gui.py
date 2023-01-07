import functions
import PySimpleGUI as sg

label = sg.Text('Type in to-do')
input_box = sg.InputText(tooltip='Enter to-do', key='todo')
add_button = sg.Button('Add')

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 15))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.read_file()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_file(todos)
        case sg.WINDOW_CLOSED:
            break


window.close()