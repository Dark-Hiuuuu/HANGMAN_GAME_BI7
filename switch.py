from tkinter import *
import subprocess
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

def switch_to_main():
    # Replace "path/to/file.py" with the path to the file you want to run
    subprocess.call(["python", "main.py"])


def switch_to_instruction(root):
    instruction_window = Toplevel(root)
    iconitb = PhotoImage(file = "images\LogoITB.png")
    instruction_window.iconphoto(False, iconitb)
    instruction_window.title("Instruction")
    # get screen width and height
    screen_width =instruction_window.winfo_screenwidth()
    screen_height = instruction_window.winfo_screenheight()        

    # set window width and height
    window_width = 725
    window_height = 322

    # set window position
    instruction_window.geometry("%dx%d+%d+%d" % (window_width, window_height,
                            (screen_width - window_width) / 2, (screen_height - window_height) / 2))

    instruction_board_img = PhotoImage(file = f"images\InstructionBoardmain.png")
    instruction_board = Label(instruction_window, image = instruction_board_img, borderwidth = 0,
                                    highlightthickness = 0, relief = "flat", bg="#ffffff", activebackground = "#ffffff")
    instruction_board.place(x = 0, y = 0)

    instruction_window.mainloop()

def switch_to_login():
    subprocess.call(["python", "loginscreen.py"])

   
    