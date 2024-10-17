import PySimpleGUI as sg
sg.theme("DarkGrey1")
sg.theme_text_color("#E3CF57")

susunan = [
    [sg.Push(),
    sg.Text("UNISKA MABA",font=("helvetica",24)),
    sg.Push()],
    [sg.Push(),
    sg.Text("BANJARMASIN",font=("helvetica",24)),
    sg.Push()]
]


window = sg.Window("Latihan Python", susunan, size=(400, 200), font=("times",18))
window()
window.close()