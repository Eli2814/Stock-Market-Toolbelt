import tkinter as tk
from tkinter import messagebox

def calculate_percentage_difference(v1, v2):
    try:
        difference = abs(v1 - v2)
        average = (v1 + v2) / 2
        return (difference / average) * 100
    except ZeroDivisionError:
        return None

def on_calculate():
    try:
        v1 = float(entry1.get())
        v2 = float(entry2.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")
        return

    result = calculate_percentage_difference(v1, v2)
    if result is None:
        messagebox.showerror("Error", "Cannot calculate percentage difference with a zero average.")
    else:
        lbl_result.config(text=f"{result:.2f}%")

def on_clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    lbl_result.config(text="")

def on_quit():
    root.destroy()

root = tk.Tk()
root.title("Percentage Difference Calculator")

# Layout
tk.Label(root, text="Value #1:").grid(row=0, column=0, padx=8, pady=8, sticky="e")
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=8, pady=8)

tk.Label(root, text="Value #2:").grid(row=1, column=0, padx=8, pady=8, sticky="e")
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=8, pady=8)

btn_calc = tk.Button(root, text="Calculate", command=on_calculate)
btn_calc.grid(row=2, column=0, padx=8, pady=8, sticky="we")

btn_clear = tk.Button(root, text="Clear", command=on_clear)
btn_clear.grid(row=2, column=1, padx=8, pady=8, sticky="we")

lbl_result = tk.Label(root, text="", font=("Arial", 14))
lbl_result.grid(row=3, column=0, columnspan=2, padx=8, pady=16)

btn_quit = tk.Button(root, text="Exit", command=on_quit)
btn_quit.grid(row=4, column=0, columnspan=2, padx=8, pady=8, sticky="we")

root.mainloop()
