import tkinter as tk
from tkinter import messagebox

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        messagebox.showerror("Error", "Division by zero is not allowed.")
        return None

def calculate():
    try:
        num1 = float(entry_num1.get())
        operator = entry_operator.get()
        num2 = float(entry_num2.get())

        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        else:
            messagebox.showerror("Error", "Invalid operator")
            return

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

root = tk.Tk()
root.title("Simple Calculator")

# Entry widgets
entry_num1 = tk.Entry(root, width=10)
entry_operator = tk.Entry(root, width=2)
entry_num2 = tk.Entry(root, width=10)

# Button
calculate_button = tk.Button(root, text="Calculate", command=calculate)

# Result label
result_label = tk.Label(root, text="Result: ")

# Arrange widgets in the grid
entry_num1.grid(row=0, column=0)
entry_operator.grid(row=0, column=1)
entry_num2.grid(row=0, column=2)
calculate_button.grid(row=1, column=0, columnspan=3, pady=10)
result_label.grid(row=2, column=0, columnspan=3)

root.mainloop()
