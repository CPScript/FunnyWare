from tkinter import *
from tkinter import messagebox
import random
import threading

def no():
    messagebox.showinfo('The Gay Survey', 'Your gay')
    quit()

def motionMouse(event):
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    btnYes.place(x=x, y=y)

def create_popup():
    for _ in range(10):
        x = random.randint(0, root.winfo_screenwidth() - 100)
        y = random.randint(0, root.winfo_screenheight() - 100)
        popup = Toplevel(root)
        popup.geometry(f'+{x}+{y}')
        popup.title('Your Gay)')
        popup['bg'] = 'white'
        Label(popup, text='Your Gay', font='Arial 16').pack()
        popups.append(popup)
    
    root.after(100, create_popup)

def disable_window():
    root.attributes('-disabled', True)

root = Tk()
root.geometry('600x600')
root.title('The Gay Survey')
root.resizable(width=False, height=False)
root['bg'] = 'white'

title_label = Label(root, text='The Gay Survey', font='Arial 24 bold', bg='white')
title_label.pack(pady=20)

text_label = Label(root, text='This is a program called "Gayware", belonging to this repo\n Github.com/CPScript/Funnyware\n this is used to test if your gay or not so choose wisly', font='Arial 16', bg='white')
text_label.pack()

btnYes = Button(root, text='No. Im not gay', font='Arial 20 bold')
btnYes.place(x=50, y=300)
btnYes.bind('<Enter>', motionMouse)
btnYes['command'] = lambda: threading.Thread(target=create_popup).start()
btnNo = Button(root, text='Yes. I am gay', font='Arial 20 bold', command=no)
btnNo.place(x=350, y=300)

popups = []

btnNo['command'] = lambda: [disable_window(), threading.Thread(target=create_popup).start()]

root.mainloop()
