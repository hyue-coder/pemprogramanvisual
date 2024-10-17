import PySimpleGUI as sg
sg.theme("DarkGrey1")
sg.theme_text_color("#E3CF57")

layout = [
    [sg.Text("FTI UNISKA",text_color="#7FFFD4",font=("Helvetica",24))],
    [sg.Text("FAKULTAS TEKNOLOGI INFORMASI",text_color="#7FFFD4",font=("Courier",18,"italic","bold","underline"))],
    [sg.Text("UNISKA MAB BANJARMASIN",text_color="#7FFFD4",font=("Times",18))],
]

window = sg.Window("Latihan Python", layout, size=(400, 200), font=("times",18))
window()
window.close()