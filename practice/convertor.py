import PySimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text('Select files to compress:')
input1 = sg.Input()
chose_b1 = sg.FilesBrowse('Choose', key='files')

label2 = sg.Text('Select destination folder:')
input2 = sg.Input()
chose_b2 = sg.FolderBrowse('Choose', key='folder')

compress_b = sg.Button('Compress')

exit_button = sg.Button('Exit')
window = sg.Window('File Compressor', layout=[[label1, input1, chose_b1],
                                              [label2, input2, chose_b2],
                                              [compress_b, exit_button]])

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values['files'].split(';')
    folder = values['folder']
    make_archive(filepaths, folder)
    match event:
        case 'Exit':
            break

window.close()