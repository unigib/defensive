import tkinter as tk
from tkinter import messagebox

from validation import parse_count


def submit():
    try:
        count = parse_count(entry.get())
    except ValueError as error:
        messagebox.showerror("Input error", str(error))
        return

    messagebox.showinfo("Accepted", f"Count: {count}")


root = tk.Tk()
root.title("Count (1-10)")

entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Check", command=submit).pack()

root.mainloop()
