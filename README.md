<p align="center">
  <img src="logo.png" alt="GIB University logo" width="180">
</p>

<h1 align="center">Gibraltar University</h1>

# Python lab: defensive programming

Build a program that accepts whole numbers from 1 to 10
and lets users correct invalid input.

Python uses `try/except` for exception handling.

## Files

| File | Purpose |
| --- | --- |
| starter.py | Initial version without defensive checks |
| validation.py | Shared conversion and range checks |
| cli_lab.py | Command-line version with retry handling |
| gui_lab.py | Tkinter version with error messages |
| student_form_skeleton.py | Crash-proof Tkinter starter for a safe data-entry form |
| grade_import.py | Booking-form exercise with five input-validation tasks |

Keep the four number-entry lab files in the same folder. The booking-form
exercise is in `grade_import.py`.

## Before you start

Use Python 3. Open a terminal in this folder.

The commands below use `python`. If your Python 3 installation
uses `python3` or `py`, substitute that command.

For the graphical exercise, check Tkinter with:

```bash
python -m tkinter
```

A demonstration window should open. If Tkinter is unavailable,
ask your tutor for installation guidance.

## 1. Discover the problems

Run:

```bash
python starter.py
```

Predict and test what happens with `5`, `hello` and `0`.
Restart the program for each test.

- Which input causes an exception?
- Which input converts successfully but breaks the lab rule?

The starter deliberately lacks defensive checks.

## 2. Explore the shared validator

Read `validation.py`.

- What does `int()` check?
- Why do we also need the range check?
- What does `raise ValueError(...)` tell the calling code?
- Why does the function return a number only after validation?

## 3. Try command-line recovery

Run:

```bash
python cli_lab.py
```

Enter `hello`, then `0`, then `5`.

Explain what `continue` and `break` do.
The program should let you correct invalid input without restarting.

## 4. Try the Tkinter version

Run:

```bash
python gui_lab.py
```

Enter a value and click Check.

- Where does `entry.get()` obtain its text?
- Why does the button use `command=submit`?
- Why does the error handler use `return`?
- How do both applications reuse the same validation function?

## Crash-proof Tkinter form skeleton

Use the file `student_form_skeleton.py` as a guided starting point for a
crash-free Tkinter form. It is designed to help you build a form that handles
bad input safely instead of raising errors in the middle of the GUI.

Run it with:

```bash
python student_form_skeleton.py
```

The skeleton shows a simple student-registration form with fields for name,
student ID, age and GPA. It is intentionally incomplete: each section includes
`TODO` markers so you can add the defensive checks in a structured order.

The important pattern is:

- Read the value from each `Entry` widget with `.get().strip()`.
- Check for empty input before converting it.
- Wrap conversion such as `int()` and `float()` in a `try/except ValueError`
  block.
- Validate ranges using normal `if` checks after conversion succeeds.
- Use `messagebox.showerror(...)` to report problems and then `return` so the
  form exits cleanly without crashing.
- Clear the fields only after a successful submission.

This template demonstrates the defensive-programming pattern that keeps the
application responsive and prevents uncaught exceptions from stopping the
Tkinter window.

## Web solution in Flask

The same defensive ideas can be used in a web form built with Flask. Instead of
reading data from Tkinter `Entry` widgets, the server reads values from
`request.form`.

A typical Flask version follows the same structure:

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    error = ""
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        age_text = request.form.get('age', '').strip()

        if not name:
            error = 'Please enter your name.'
        else:
            try:
                age = int(age_text)
            except ValueError:
                error = 'Age must be a whole number.'
            else:
                if age < 18 or age > 100:
                    error = 'Age must be between 18 and 100.'
                else:
                    return f"Valid submission: {name}, age {age}"

    return render_template('index.html', error=error)
```

The page template can include a form with fields for name and age, and it can
show the `error` message when validation fails. The advantage of the Flask
version is that the browser stays open and the user can correct invalid input
without restarting the app.

This is the same defensive pattern as the Tkinter starter:

- trim input before validation
- reject empty values early
- convert with `try/except`
- check ranges with `if` statements
- show a helpful message and stop the action cleanly

## 5. Test both applications

Run each listed input separately.

| Input | Expected result |
| --- | --- |
| hello or 3.5 | Enter a whole number. |
| Empty input or spaces only | Enter a whole number. |
| 0, -1 or 11 | Use a number from 1 to 10. |
| 1 or 10 | Accept the value. |
| Spaces around 5 | Accept as 5. |

Recovery check: enter `hello`, then `5` without restarting.

The command-line program exits after a valid value.
The Tkinter window remains open for another check.

## Booking-form challenges

This exercise is intended for students who are comfortable with Python
functions, exceptions, dictionaries and basic Tkinter. It gives you practice
validating user input, handling errors in a GUI, and testing edge cases.

Run the exercise with:

```bash
python grade_import.py
```

The form starts with a valid example booking. Change one field at a time and
click **Calculate** to explore how the current program behaves. At first,
invalid input may produce an uncaught exception instead of a useful message.

### Challenge 1: Validate the name

- Reject an empty name and a name containing only spaces.
- Remove leading and trailing spaces before displaying the name.
- Show a useful error message and do not calculate a total when the name is
  invalid.

### Challenge 2: Validate the age

- Handle text that cannot be converted to an integer.
- Accept ages from 18 through 100, inclusive; reject values outside that range.
- Explain the difference between a conversion error and a value that converts
  successfully but is outside the permitted range.

### Challenge 3: Validate the ticket quantity

- Handle non-integer input.
- Accept between 1 and 6 tickets, inclusive.
- Check that an invalid quantity does not leave a stale result from a previous
  successful calculation.

### Challenge 4: Validate the booking date

- Require an actual calendar date in the exact `YYYY-MM-DD` format.
- Reject malformed dates such as `15/11/2026` and impossible dates such as
  `2026-02-30`.
- Show a clear error instead of allowing a parsing exception to escape.

### Challenge 5: Validate the discount code

- Accept `NONE` and `STUDENT` regardless of letter case or surrounding spaces.
- Reject unknown codes with a helpful message.
- Do not calculate or display a total until every field is valid.

### Challenge 6: Test the completed form

For each row, enter the value in the named field while leaving the other
fields at their defaults. Record the observed result and whether it matches
the expected behavior.

| Field | Input | Expected behavior |
| --- | --- | --- |
| Name | Empty or spaces only | Show an error; do not display a booking |
| Age | `abc` | Show an integer-input error |
| Age | `17` or `101` | Reject as outside the allowed range |
| Age | `18` or `100` | Accept |
| Tickets | `2.5` | Show an integer-input error |
| Tickets | `0` or `7` | Reject as outside the allowed range |
| Tickets | `1` or `6` | Accept |
| Date | `15/11/2026` | Reject the format |
| Date | `2026-02-30` | Reject the impossible date |
| Discount | ` student ` | Accept the student discount |
| Discount | `VIP` | Show an unknown-code error |

Also test recovery: submit an invalid booking, correct the field, then submit
again without restarting the application.

### Challenge 7: Improve the design

- Move booking validation and total calculation into functions that can be
  tested without opening a Tkinter window.
- Keep GUI code responsible for reading fields and displaying success or error
  messages.
- Add automated unit tests for valid bookings, invalid values, and the
  calculated total. Include tests for both discount codes.
- Consider how to prevent the form from showing an old successful result after
  a later submission fails.

### Challenge 8: Create and raise your own exception

Python calls a throwable error an *exception*. Define a custom exception named
`BookingValidationError` that inherits from `ValueError`.

- Raise `BookingValidationError` when a booking rule is broken, such as when
  the name is blank or the ticket quantity is outside the allowed range.
- Include a useful message that explains what the user needs to correct.
- Catch `BookingValidationError` in the GUI callback and show its message with
  a Tkinter error dialog, such as `messagebox.showerror`.
- Do not use a broad `except Exception` handler. Let unexpected programming
  errors remain visible so they can be fixed.
- Write a small test that calls the validation function with invalid data and
  checks that it raises `BookingValidationError`.

Explain why a custom exception can make validation errors clearer than raising
`ValueError` for every kind of failure.

## Challenge

Change the allowed range to 1-20 in `validation.py`.
Update the error message and both interface prompts to match.
Test `20` and `21` in both applications.

## Submission

Submit your code and a short test log:

| Application | Input | Expected result | Actual result | Pass/fail |
| --- | --- | --- | --- | --- |
| | | | | |

Explain why conversion and range checking are separate.

## References

- https://docs.python.org/3/tutorial/errors.html
- https://docs.python.org/3/library/tkinter.html
- https://docs.python.org/3/library/tkinter.messagebox.html
