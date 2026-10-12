import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

PRICE = 20
DISCOUNTS = {
    "NONE": 0.0,
    "STUDENT": 0.20,
}


def calculate_booking():
    # Clear any result from the previous calculation.
    result.set("")

    # TASK 1:
    # Reject a blank or spaces-only name.
    # Raise ValueError, catch it, show an error and return.
    name = fields["Name"].get().strip()

    # TASK 2:
    # Catch invalid integer input.
    # Also reject ages below 18 or above 100.
    age = int(fields["Age"].get())

    # TASK 3:
    # Catch invalid integer input.
    # Also reject ticket quantities below 1 or above 6.
    tickets = int(fields["Tickets"].get())

    # TASK 4:
    # Catch invalid dates.
    # Require a real date in exact YYYY-MM-DD format.
    date_text = fields["Date"].get().strip()
    booking_date = datetime.strptime(
        date_text, "%Y-%m-%d"
    ).date()

    # TASK 5:
    # Catch KeyError if the discount code is unknown.
    # Valid codes: NONE and STUDENT.
    discount_code = fields["Discount"].get().strip().upper()
    discount = DISCOUNTS[discount_code]

    # This should run only after all checks succeed.
    total = tickets * PRICE * (1 - discount)

    result.set(
        f"Name: {name}\n"
        f"Age: {age}\n"
        f"Date: {booking_date.isoformat()}\n"
        f"Tickets: {tickets}\n"
        f"Total: GBP {total:.2f}"
    )


# Create the application window.
root = tk.Tk()
root.title("Booking Form: Find the Five Validation Problems")

frame = ttk.Frame(root, padding=20)
frame.grid(row=0, column=0, sticky="nsew")

ttk.Label(
    frame,
    text="Booking Form",
    font=("Arial", 18, "bold"),
).grid(row=0, column=0, columnspan=2, pady=(0, 15))

# These defaults form a valid booking.
defaults = {
    "Name": "Alex",
    "Age": "20",
    "Tickets": "2",
    "Date": "2026-11-15",
    "Discount": "NONE",
}

fields = {}

for row, (label, default_value) in enumerate(
    defaults.items(), start=1
):
    ttk.Label(frame, text=label).grid(
        row=row,
        column=0,
        sticky="w",
        padx=(0, 15),
        pady=6,
    )

    entry = ttk.Entry(frame, width=30)
    entry.insert(0, default_value)
    entry.grid(row=row, column=1, pady=6)

    fields[label] = entry

ttk.Label(
    frame,
    text=(
        "Date format: YYYY-MM-DD\n"
        "Discount codes: NONE or STUDENT\n"
        "Ticket price: GBP 20"
    ),
).grid(
    row=6,
    column=0,
    columnspan=2,
    sticky="w",
    pady=12,
)

ttk.Button(
    frame,
    text="Calculate",
    command=calculate_booking,
).grid(row=7, column=0, columnspan=2, pady=10)

result = tk.StringVar()

ttk.Label(
    frame,
    textvariable=result,
    wraplength=400,
).grid(
    row=8,
    column=0,
    columnspan=2,
    sticky="w",
    pady=10,
)

root.mainloop()