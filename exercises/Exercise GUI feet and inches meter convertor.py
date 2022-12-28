import PySimpleGUI as Ps
from Convertors import convert

label_feet = Ps.Text("Enter Feet: ")
label_inch = Ps.Text("Enter Inches: ")

input_feet = Ps.InputText(key='feet')
input_inches = Ps.InputText(key='inches')

convert_button = Ps.Button("Convert")
label_meters = Ps.Text("", key='output')
window = Ps.Window("Convertor", layout=[[label_feet, input_feet],
                                        [label_inch, input_inches],
                                        [convert_button, label_meters]])
while True:
    event, values = window.read()
    feet = float(values['feet'])
    inches = float(values['inches'])
    result = convert(feet, inches)
    window['output'].update(value=f"{result} meters")

