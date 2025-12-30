import tkinter as tk
import math

def click(key):
    try:
        current = entry.get()
        if key == "=":
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        elif key == "C":
            entry.delete(0, tk.END)
        elif key == "sin":
            result = math.sin(math.radians(float(current)))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        elif key == "cos":
            result = math.cos(math.radians(float(current)))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        elif key == "tan":
            result = math.tan(math.radians(float(current)))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        elif key == "√":
            result = math.sqrt(float(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        elif key == "log":
            result = math.log10(float(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        else:
            entry.insert(tk.END, key)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Scientific Calculator")

entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('C', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('sin', 2, 4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('cos', 3, 4),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), ('tan', 4, 4),
    ('√', 5, 0), ('log', 5, 1)
]

for (text, row, col) in buttons:
    tk.Button(root, text=text, width=5, height=2, command=lambda t=text: click(t)).grid(row=row, column=col)

root.mainloop()
