import functions
import PySimpleGUI as sg

label = sg.Text("Type a To-Do list")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
# layout expects a list of object instances (e.g. buttons, text boxes)
window = sg.Window('To-Do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 15))
while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todos = value['todo'] + "\n"
            todos.append(new_todos)
            functions.write_todos(todos)
        case sg.WINDOW_CLOSED:
            break
window.close()


