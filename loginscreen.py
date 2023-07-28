from tkinter import *
from PIL import ImageTk, Image
import csv
from tkinter import messagebox
import pandas as pd

# Lessen blurry effects
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)
window = Tk()

# get screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# set window width and height
window_width = 1000
window_height = 850

# set window position
window.geometry("%dx%d+%d+%d" % (window_width, window_height,
                                 (screen_width - window_width) / 2, (screen_height - window_height) / 2))

window.configure(bg="#ffffff")

data_info = pd.read_csv('info.csv', delimiter=',', encoding='utf-8')
data_info = data_info.astype(str)

# Background
image = Image.open("images/LoginScreen/Login.png")
background_image = ImageTk.PhotoImage(image)
background_label = Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

window.title("Hangman game!")

#icon
iconitb = PhotoImage(file = "images\LogoITB.png")
window.iconphoto(False, iconitb)
# Entry Name
name_entry = Entry(window, bd=0, font=("Syncopate", 14))
name_entry.place(x=297, y=300, height=44, width=548)

# Entry Phone
phone_entry = Entry(window, bd=0, font=("Syncopate", 14))
phone_entry.place(x=297, y=419, height=44, width=548)

# Entry Email
email_entry = Entry(window, bd=0, font=("Syncopate", 14))
email_entry.place(x=297, y=536, height=44, width=548)

# Button Enter
enter_img = PhotoImage(file="images/LoginScreen/ButtonEnter.png")
itblogo = Button(image=enter_img, borderwidth=0,
                 highlightthickness=0, relief="flat", bg="#ffffff", activebackground="#ffffff",
                 command=lambda: click_enter_button())
itblogo.place(x=447, y=646, width=195, height=54)


def click_enter_button():
    if name_entry.get().strip() == '' or \
            phone_entry.get() == '' or \
            email_entry.get() == '':
        messagebox.showerror('Entry Error', 'You have not fully filled in the Entries yet.')
    else:
        name_info = name_entry.get()
        phone_info = phone_entry.get()
        email_info = email_entry.get()
        with open('info.csv', mode='a', newline='', encoding='utf-8') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([name_info, phone_info, email_info])
            messagebox.showinfo('Success', 'Your information has been added successfully.')
            window.destroy()


window.mainloop()
