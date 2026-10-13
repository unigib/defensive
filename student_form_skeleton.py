"""
Gibraltar University - CS Second Year
Assignment 1: Crash-Proof Data Entry Form
Starter Template Skeleton

Student Name: [Your Name]
Student ID: [Your Student ID]
"""

import tkinter as tk
from tkinter import messagebox

def submit_form():
    # 1. Retrieve raw data string from the input widgets
    name_input = name_entry.get().strip()
    id_input = id_entry.get().strip()
    age_input = age_entry.get().strip()
    gpa_input = gpa_entry.get().strip()
    
    # 2. Check for empty fields using conditional checks
    # TODO: If any fields are empty, show an error messagebox and return out of the function
    
    # 3. Data type conversion and Validation
    try:
        # TODO: Typecast student ID and Age to int, and GPA to float
        # Hint: Wrap this logic within this try block to capture format conversion problems
        pass
        
    except ValueError:
        # TODO: Handle conversion failure (e.g., user inputs text inside a number field)
        # Display an appropriate error message and terminate the function safely
        return

    # 4. Range Validation via Conditionals
    # TODO: Check if Student ID is exactly 8 characters long
    # TODO: Check if Age is between 17 and 99 (inclusive)
    # TODO: Check if GPA is between 0.0 and 4.0 (inclusive)
    # If any checks fail, display a helpful error messagebox and return out of the function
    
    # 5. Form Success State
    # TODO: If all validations clear, display a success messagebox
    # TODO: Print details cleanly to the console terminal
    # TODO: Call the clear_fields() helper function to reset the interface
    pass

def clear_fields():
    # TODO: Use the entry delete method to wipe all values out of form inputs
    pass

# --- GUI Setup Setup ---
root = tk.Tk()
root.title("GibUni Event Registration")
root.geometry("400x300")

# Labels & Entry Widgets Layout Setup
# Row 0: Name
tk.Label(root, text="Student Name:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
name_entry = tk.Entry(root, width=25)
name_entry.grid(row=0, column=1, padx=10, pady=10)

# Row 1: Student ID
tk.Label(root, text="Student ID (8 digits):").grid(row=1, column=0, padx=10, pady=10, sticky="e")
id_entry = tk.Entry(root, width=25)
id_entry.grid(row=1, column=1, padx=10, pady=10)

# Row 2: Age
tk.Label(root, text="Age (17-99):").grid(row=2, column=0, padx=10, pady=10, sticky="e")
age_entry = tk.Entry(root, width=25)
age_entry.grid(row=2, column=1, padx=10, pady=10)

# Row 3: GPA
tk.Label(root, text="GPA (0.0-4.0):").grid(row=3, column=0, padx=10, pady=10, sticky="e")
gpa_entry = tk.Entry(root, width=25)
gpa_entry.grid(row=3, column=1, padx=10, pady=10)

# Row 4: Interactive Operational Buttons
submit_btn = tk.Button(root, text="Submit", command=submit_form, bg="#A41D35", fg="white", width=10)
submit_btn.grid(row=4, column=0, padx=10, pady=20, columnspan=1)

clear_btn = tk.Button(root, text="Clear", command=clear_fields, width=10)
clear_btn.grid(row=4, column=1, padx=10, pady=20, columnspan=1)

# Initialize application main event loop
root.mainloop()
