# import the required libraries
from tkinter import *

# create an instance of Tkinter window
window = Tk()
window.title("Calculator")
# size and color of window
window.geometry('225x300')
window.configure(bg="#C0C0C0")
window.resizable(0, 0)

# input field entry
input_text = StringVar()
input_field = Entry(window, textvariable=input_text, bg="#90EE90", bd="7px", fg="black",)
input_field.grid(row="0", columnspan="4")
expression = ""









# To load calculator window
window.mainloop()

