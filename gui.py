import functions
import PySimpleGUI as sg

label = sg.Text("Type a To-Do list")
input_box = sg.InputText()
add_button = sg.Button("Add")
# layout expects a list of object instances (e.g. buttons, text boxes)
window = sg.Window('To-Do App', layout=[[label], [input_box, add_button]])
window.read()
window.close()


