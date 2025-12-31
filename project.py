'''
GUI CALACULATOR APPLICATION
A tkinter based desktop application

what is tkinter?
tkinter is python's built inn library for creating graphical user interface(gui) applications.
it provides widgets like window,button,entry,label,etc.
it follows an event-driven programming model(code runs when a user clicks a button)

purpose of this program:
creates a calculator GUI
allows user to:
enter numbers and operators
performs arthemtic calaculations
clear the input
uses python eval() function to evaluate mathematical expression.

key concepts used:
concept              description
Tkinter Widgets-    Tk,entry,button
Event Handling-     button click actions
lambda functions-   passing button values
grid layout-        positioning UI elements
exepction handling- handling invalid exxpressions
'''


import tkinter as tk
'''Imports tkinter module
tk is an alias for easy access'''

def press(v):
    '''Called when a number or operator button is clicked
    Inserts the pressed value at the end of entry widget'''
    entry.insert(tk.END, v)

def clear():
    entry.delete(0, tk.END)

def backspace():
    '''Deletes last character'''
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def calc():
    '''Called when equals button is clicked
    Evaluates the expression in entry widget using eval()
    Displays result or error message'''
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# main window creation
root = tk.Tk()
root.title("Calculator")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

# entry widget (display screen)
entry = tk.Entry(
    root,
    font=("Times New Roman", 20),
    bg="#2d2d2d",
    fg="white",
    bd=0,
    justify="right"
)

entry.grid(row=0, column=0, columnspan=4, padx=12, pady=12, ipady=10)

# button labels
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# dynamic button creation
row_val = 1
col_val = 0

for b in buttons:
    cmd = calc if b == "=" else lambda x=b: press(x)

    tk.Button(
        root,
        text=b,
        command=cmd,
        font=("Calibri", 14),
        width=5,
        height=2,
        bg="#ff9500" if b in "+-*/=" else "#3a3a3a",
        fg="white",
        bd=0
    ).grid(row=row_val, column=col_val, padx=6, pady=6)

    col_val += 1
    if col_val == 4:
        row_val += 1
        col_val = 0

# backspace button
tk.Button(
    root,
    text="\u232B",
    command=backspace,
    font=("Calibri", 14),
    bg="#6c6c6c",
    fg="white",
    bd=0,
    width=10,
    height=2
).grid(row=row_val, column=0, columnspan=2, pady=6)

# clear button
tk.Button(
    root,
    text="C",
    command=clear,
    font=("Calibri", 14),
    bg="#ff3b3b",
    fg="white",
    bd=0,
    width=10,
    height=2
).grid(row=row_val, column=2, columnspan=2, pady=6)

root.mainloop()
'''Starts the Tkinter event loop
Waits for user interaction'''
