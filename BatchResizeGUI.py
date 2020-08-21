import os
import os.path
import glob
import PySimpleGUI as sg
from PIL import Image

def windowGUI():
    sg.theme('Dark Blue 3')  # Add a touch of color
    # All the stuff inside the window.
    file_list_column = [
        [
            sg.Text("Photo Folder"),
            sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
            sg.FolderBrowse(),
        ],
        [sg.Button("Downscale")],
        [sg.Text("Width (px)  "), sg.InputText()],
        [sg.Text("Height (px) "), sg.InputText()],
        [sg.Text("List of images to be downscaled:")],
        [
            sg.Listbox(
                values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
            )
        ],
    ]

 # ----- Full layout -----
    layout = [
        [
            sg.Column(file_list_column),
        ]
    ]

    window = sg.Window("Batch Downscale Image Tool - Rev A", layout)

    # Run the Event Loop
    while True:
        event, values = window.read()
        # Ends the program if window closed
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        # Makes a list of files in the folder
        if event == "-FOLDER-":
            folder = values["-FOLDER-"]
            try:
                # Get list of files in folder
                file_list = os.listdir(folder)
                os.chdir(folder)

            except:
                file_list = []
                sg.PopupError('File list is empty')  # Shows red error button

            global fnames
            fnames = [
                f
                for f in file_list
                if os.path.isfile(os.path.join(folder, f))
                   and f.lower().endswith((".jpg")) or f.lower().endswith((".png"))
            ]
            window["-FILE LIST-"].update(fnames)

        elif event == 'Downscale':
            try:

                width = values[0]
                height = values[1]
                sg.popup('Results', ' The files have been successfully downscaled')

            except ValueError:
                sg.PopupError('Error',
                              'No objects to downscale. Try selecting a different folder or entering valid dimensions')  # Shows red error button
            else:
                sg.PopupError('Unexpected error:', 'Something went wrong and I do not know what')
                raise
    window.close()

def main():

    for file in os.listdir(f):
        f_img = f + "/" + file
        img = Image.open(f_img)
        img = img.resize((2296, 1724))
        img.save(f_img)


windowGUI()