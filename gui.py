import functions
import PySimpleGUI as sg
import time

sg.theme('BrightColors')

clock = sg.Text('', key='clock')
label = sg.Text('Type in to-do')
input_box = sg.InputText(tooltip='Enter to-do', key='todo')
add_button = sg.Button('Add')
list_box = sg.Listbox(values=functions.read_file(),
                      key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button('Edit')

complete_button = sg.Button('Complete')

exit_button = sg.Button('Exit')

window = sg.Window('My To-Do app',
                   layout=[[clock],
                           [label], [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read(timeout=10)
    window['clock'].update(value=time.strftime('%b %d %Y, %H:%M:%S'))
    match event:
        case 'Add':
            todos = functions.read_file()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_file(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = functions.read_file()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_file(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup('Please select a To-Do first!', font=('Helvetica', 15))
        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.read_file()
                todos.remove(todo_to_complete)
                functions.write_file(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup('Please select a To-Do first!')
        case 'Exit':
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WINDOW_CLOSED:
            break


window.close()