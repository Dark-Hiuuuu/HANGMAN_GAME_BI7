from tkinter import *
from switch import *
import pygame
window = Tk()

# get screen width and height
screen_width =window.winfo_screenwidth()
screen_height = window.winfo_screenheight()        

# set window width and height
window_width = 1000
window_height = 850

# set window position
window.geometry("%dx%d+%d+%d" % (window_width, window_height,
                        (screen_width - window_width) / 2, (screen_height - window_height) / 2))

window.configure(bg = "#ffffff")
window.title("Hangman game!")

#icon
iconitb = PhotoImage(file = "images\LogoITB.png")
window.iconphoto(False, iconitb)

#button start
img_startbutton = PhotoImage(file = f"images\MainScreen\ButtonStart.png")
button_start = Button(image = img_startbutton, borderwidth = 0,
                                highlightthickness = 0, relief = "flat", bg="#ffffff", activebackground = "#ffffff",
                                command = lambda: switch_to_main())
button_start.place(x = 86, y = 343, width = 414, height = 85)

#button instruction
img_instructionbutton = PhotoImage(file = f"images\MainScreen\ButtonInstruction.png")
button_instruction = Button(image = img_instructionbutton, borderwidth = 0,
                                highlightthickness = 0, relief = "flat", bg="#ffffff", activebackground = "#ffffff",
                                command = lambda: switch_to_instruction(window))
button_instruction.place(x = 86, y = 453, width = 414, height = 85)

#button login
img_login = PhotoImage(file = f"images\MainScreen\ButtonLogin.png")
button_login = Button(image = img_login, borderwidth = 0,
                                highlightthickness = 0, relief = "flat", bg="#ffffff", activebackground = "#ffffff",
                                command = lambda: switch_to_login())
button_login.place(x = 86, y = 563, width = 414, height = 85)

#ITB CLUB
img_itb = PhotoImage(file = f"images/MainScreen/ITB.png")
itblogo = Label(image = img_itb, borderwidth = 0,
                                highlightthickness = 0, relief = "flat", bg="#ffffff", activebackground = "#ffffff")
itblogo.place(x = 297, y = 63, width = 406, height = 80)

#man
img_man = PhotoImage(file = f"images/MainScreen/Man.png")
man = Label(image = img_man, borderwidth = 0,
                                highlightthickness = 0, relief = "flat", bg="#ffffff", activebackground = "#ffffff")
man.place(x = 543, y = 250, width = 403, height = 394)

#title
img_titlehangman = PhotoImage(file = f"images/MainScreen/Title.png")
title = Label(image = img_titlehangman, borderwidth = 0,
                                highlightthickness = 0, relief = "flat", bg="#ffffff", activebackground = "#ffffff")
title.place(x = 35, y = 187)

window.mainloop()
