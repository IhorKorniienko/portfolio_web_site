import functions
import PySimpleGUI as sg
import time

clock = sg.Text("", key='clock')
sg.theme("Black")

# Adding input box & list box, labels
label = sg.Text("Type a To-Do list:", font=("Times New Roman", 18))
input_box = sg.InputText(tooltip="Enter todo", key='todo', size=[55], border_width=6)
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[60, 15], horizontal_scroll=True)

# Adding buttons
add_button = sg.Button("Add", font=("Times New Roman", 15), button_color="Yellow", border_width=0)
added_buttons = [[sg.Button("Edit", font=("Times New Roman", 15), button_color="Yellow", border_width=0)],
                 [sg.Button("Complete", font=("Times New Roman", 15), button_color="Yellow", border_width=0)],
                 [sg.Button("Exit", font=("Times New Roman", 15), button_color="Yellow", border_width=0)]]

layout_edit_complete_exit = sg.Column(added_buttons, vertical_alignment='Top')

# layout expects a list of object instances (e.g. buttons, text boxes)
window = sg.Window('To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, layout_edit_complete_exit]],
                   font=('Times New Roman', 14))

while True:
    event, value = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"), background_color="Black")

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todos = value['todo'] + "\n"
            todos.append(new_todos)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update('')

        case "Edit":
            try:
                todo_to_edit = value['todos'][0]
                new_todo = value['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first and update it and press Edit to confirm your changes!",
                         font=("Times New Roman", 14))

        case "Complete":
            try:
                todo_to_complete = value['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update('')
            except IndexError:
                sg.popup("You have to select an item and press Complete!", font=("Times New Roman", 14))

        case "Exit":
            break

        case 'todos':
            try:
                window['todo'].update(value=value['todos'][0])
            except IndexError:
                sg.popup("You cannot select the empty field!", font=("Times New Roman", 14))

        case sg.WINDOW_CLOSED:
            break
window.close()
