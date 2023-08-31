import tkinter as tk
import ctypes
import time
import threading

blackout_duration = 500

def set_screen_brightness(value):
    if value < 0:
        value = 0
    elif value > 100:
        value = 100

    user32 = ctypes.windll.user32
    user32.SetDisplayBrightness(value)

def show_blackout_window():
    root = tk.Tk()
    root.title("Blackout Information")

    label = tk.Label(root, text="Information about blackouts goes here.")
    label.pack()

    def on_window_close():
        root.destroy()
        blackout_thread = threading.Thread(target=blackout_screen)
        blackout_thread.start()

    root.protocol("WM_DELETE_WINDOW", on_window_close)
    root.mainloop()

def blackout_screen():
    set_screen_brightness(0)
    time.sleep(blackout_duration)
    set_screen_brightness(100)

# Main program
show_blackout_window()
