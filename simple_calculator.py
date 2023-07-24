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
input_field = Entry(window, textvariable=input_text, bg="#90EE90", bd="7px", fg="black", )
input_field.grid(row="0", columnspan="4")
expression = ""


# press method
def press(press_value):
    global expression
    expression = expression + str(press_value)
    input_text.set(expression)


# calculate total and error checking
def equal_press():
    try:
        global expression
        total = str(eval(expression))
        input_text.set(total)

    except ZeroDivisionError:
        input_text.set("zero Division error")
    except:
        input_text.set("error")


# clear display area
def clear():
    global expression
    input_text.set("")
    expression = ""


# buttons and grids are added
button7 = Button(window, text="7", bd=10, padx=10, pady=3, command=lambda: press(7))
button7.grid(row="2", column="0", padx=5, pady=5)
button8 = Button(window, text="8", bd=10, padx=10, pady=3, command=lambda: press(8))
button8.grid(row="2", column="1", padx=15)
button9 = Button(window, text="9", bd=10, padx=10, pady=3, command=lambda: press(9))
button9.grid(row="2", column="2")
button4 = Button(window, text="4", bd=10, padx=10, pady=3, command=lambda: press(4))
button4.grid(row="3", column="0", padx=5, pady=5)
button5 = Button(window, text="5", bd=10, padx=10, pady=3, command=lambda: press(5))
button5.grid(row="3", column="1")
button6 = Button(window, text="6", bd=10, padx=10, pady=3, command=lambda: press(6))
button6.grid(row="3", column="2")
button1 = Button(window, text="1", bd=10, padx=12, pady=3, command=lambda: press(1))
button1.grid(row="4", column="0", padx=5, pady=12)
button2 = Button(window, text="2", bd=10, padx=10, pady=3, command=lambda: press(2))
button2.grid(row="4", column="1")
button3 = Button(window, text="3", bd=10, padx=10, pady=3, command=lambda: press(3))
button3.grid(row="4", column="2")
button0 = Button(window, text="0", bd=10, padx=10, pady=3, command=lambda: press(0))
button0.grid(row="5", column="0")
decimal = Button(window, text=".", bd=10, padx=12, pady=3, command=lambda: press("."))
decimal.grid(row="5", column="1")
equal_to = Button(window, text="=", bd=10, padx=10, pady=3, command=equal_press)
equal_to.grid(row="5", column="2")
plus = Button(window, text="+", bd=10, padx=10, pady=3, command=lambda: press("+"))
plus.grid(row="5", rowspan="2", column="3", ipady=5)
minus = Button(window, text="-", bd=10, padx=11, pady=3, command=lambda: press("-"))
minus.grid(row="4", column="3")
multiply = Button(window, text="*", bd=10, padx=11, pady=3, command=lambda: press("*"))
multiply.grid(row="3", column="3")
divide = Button(window, text="/", bd=10, padx=13, pady=3, command=lambda: press("/"))
divide.grid(row="2", column="3")
percent = Button(window, text="%", bg="grey", fg="black", bd=10, padx=9, pady=3, command=lambda: press("%"))
percent.grid(row="1", column="3", padx=20, pady=20)
clear = Button(window, text="C", bg="orange", bd=10, padx=20, pady=3, command=clear)
clear.grid(row="1", column="0", columnspan="3", padx=20, pady=20)

# To load calculator window
window.mainloop()
