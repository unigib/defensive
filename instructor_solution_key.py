# Gib University - Computer Science Department
# Second Year Assignment: Robust Tkinter Data Entry Form
# INSTRUCTOR SOLUTION KEY

import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = entry_name.get().strip()
    id_str = entry_id.get().strip()
    age_str = entry_age.get().strip()
    gpa_str = entry_gpa.get().strip()
    
    if not name or not id_str or not age_str or not gpa_str:
        messagebox.showerror("Validation Error", "All fields are required! Please fill out the entire form.")
        return

    try:
        student_id = int(id_str)
    except ValueError:
        messagebox.showerror("Type Error", "Student ID must be a valid integer number.")
        return

    try:
        age = int(age_str)
    except ValueError:
        messagebox.showerror("Type Error", "Age must be a valid integer number.")
        return

    try:
        gpa = float(gpa_str)
    except ValueError:
        messagebox.showerror("Type Error", "GPA must be a valid numerical value (e.g., 3.5).")
        return

    if len(id_str) != 8 or student_id < 0:
        messagebox.showerror("Constraint Error", "Student ID must be exactly 8 digits long.")
        return

    if age < 17 or age > 99:
        messagebox.showerror("Constraint Error", "Age must be between 17 and 99 years old.")
        return

    if gpa < 0.0 or gpa > 4.0:
        messagebox.showerror("Constraint Error", "GPA must be between 0.0 and 4.0.")
        return

    success_msg = f"Registration Successful for {name}!"
    messagebox.showinfo("Success", success_msg)
    
    print("--- New Registration Captured Successfully ---")
    print(f"Name:       {name}")
    print(f"Student ID: {student_id}")
    print(f"Age:        {age}")
    print(f"GPA:        {gpa:.2f}")
    print("-" * 42)
    
    clear_form()

def clear_form():
    entry_name.delete(0, tk.END)
    entry_id.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_gpa.delete(0, tk.END)
    entry_name.focus()

root = tk.Tk()
root.title("GibUni Event Registration - Solution Key")
root.geometry("400x250")
root.resizable(False, False)

frame = tk.Frame(root, padx=20, pady=15)
frame.pack(fill=tk.BOTH, expand=True)

tk.Label(frame, text="Student Name:", anchor="w").grid(row=0, column=0, sticky="ew", pady=5)
tk.Label(frame, text="Student ID (8-digit):", anchor="w").grid(row=1, column=0, sticky="ew", pady=5)
tk.Label(frame, text="Age (17-99):", anchor="w").grid(row=2, column=0, sticky="ew", pady=5)
tk.Label(frame, text="GPA (0.0-4.0):", anchor="w").grid(row=3, column=0, sticky="ew", pady=5)

entry_name = tk.Entry(frame)
entry_id = tk.Entry(frame)
entry_age = tk.Entry(frame)
entry_gpa = tk.Entry(frame)

entry_name.grid(row=0, column=1, sticky="ew", pady=5)
entry_id.grid(row=1, column=1, sticky="ew", pady=5)
entry_age.grid(row=2, column=1, sticky="ew", pady=5)
entry_gpa.grid(row=3, column=1, sticky="ew", pady=5)

frame.columnconfigure(1, weight=1)

btn_clear = tk.Button(frame, text="Clear", command=clear_form, width=10)
btn_clear.grid(row=4, column=0, pady=15, padx=5, sticky="e")

btn_submit = tk.Button(frame, text="Submit", command=submit_form, bg="#005A9C", fg="white", width=12)
btn_submit.grid(row=4, column=1, pady=15, padx=5, sticky="w")

entry_name.focus()
root.mainloop()
