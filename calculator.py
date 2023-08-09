import tkinter as tk

# Function to update the input field
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

# Function to clear the input field
def clear():
    entry.delete(0, tk.END)

# Function to perform calculations
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("250x250")

# Entry widget to input the expression
entry = tk.Entry(root, width=40)
entry.grid(row=0, column=0, columnspan=4)

# Buttons layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '.', '0', '+', '='
]

row_num = 1
col_num = 0
for button in buttons:
    if button == '=':
        tk.Button(root, text=button, padx=20, pady=10, command=calculate).grid(row=row_num, column=col_num)
    else:
        tk.Button(root, text=button, padx=20, pady=10, command=lambda num=button: button_click(num)).grid(row=row_num, column=col_num)
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1

# Start the GUI event loop
root.mainloop()
