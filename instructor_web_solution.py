# instructor_web_solution.py
# Gib University - Second Year Computer Science
# Benchmark Solution Key: Crash-Proof Flask Registration Web Form

from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>GibUni Event Registration</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background-color: #f9f9f9; }
        .container { max-width: 500px; background: white; padding: 25px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; font-weight: bold; }
        input[type="text"] { width: 100%; padding: 8px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; }
        button { background-color: #003366; color: white; padding: 10px 15px; border: none; border-radius: 4px; cursor: pointer; }
        .error { color: #d32f2f; background-color: #fde8e8; padding: 10px; border-radius: 4px; margin-bottom: 15px; }
        .success { color: #388e3c; background-color: #e8f5e9; padding: 10px; border-radius: 4px; margin-bottom: 15px; }
    </style>
</head>
<body>
<div class="container">
    <h2>GibUni Web Registration Form</h2>
    
    {% if error_msg %}
        <div class="error"><strong>Error:</strong> {{ error_msg }}</div>
    {% endif %}
    {% if success_msg %}
        <div class="success"><strong>Success:</strong> {{ success_msg }}</div>
    {% endif %}

    <form method="POST" action="/">
        <div class="form-group">
            <label>Student Name:</label>
            <input type="text" name="student_name" value="{{ form_data.get('student_name', '') }}">
        </div>
        <div class="form-group">
            <label>Student ID (8 digits):</label>
            <input type="text" name="student_id" value="{{ form_data.get('student_id', '') }}">
        </div>
        <div class="form-group">
            <label>Age (17 - 99):</label>
            <input type="text" name="age" value="{{ form_data.get('age', '') }}">
        </div>
        <div class="form-group">
            <label>GPA (0.0 - 4.0):</label>
            <input type="text" name="gpa" value="{{ form_data.get('gpa', '') }}">
        </div>
        <button type="submit">Submit Registration</button>
    </form>
</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def register_student():
    if request.method == "POST":
        form_data = request.form
        
        student_name = form_data.get("student_name", "").strip()
        student_id_raw = form_data.get("student_id", "").strip()
        age_raw = form_data.get("age", "").strip()
        gpa_raw = form_data.get("gpa", "").strip()

        # 1. Presence Check using Conditionals
        if not student_name or not student_id_raw or not age_raw or not gpa_raw:
            return render_template_string(HTML_TEMPLATE, error_msg="All form fields are completely required!", form_data=form_data)

        # 2. Type Conversion Validation using Try/Except
        try:
            student_id = int(student_id_raw)
        except ValueError:
            return render_template_string(HTML_TEMPLATE, error_msg="Student ID must contain only digits.", form_data=form_data)

        try:
            age = int(age_raw)
        except ValueError:
            return render_template_string(HTML_TEMPLATE, error_msg="Age must be a valid whole number.", form_data=form_data)

        try:
            gpa = float(gpa_raw)
        except ValueError:
            return render_template_string(HTML_TEMPLATE, error_msg="GPA must be a valid decimal number.", form_data=form_data)

        # 3. Structural & Business Constraint Checks using Conditionals
        if len(str(student_id_raw)) != 8:
            return render_template_string(HTML_TEMPLATE, error_msg="Student ID must be exactly 8 digits long.", form_data=form_data)

        if age < 17 or age > 99:
            return render_template_string(HTML_TEMPLATE, error_msg="Age boundary invalid. Must be between 17 and 99.", form_data=form_data)

        if gpa < 0.0 or gpa > 4.0:
            return render_template_string(HTML_TEMPLATE, error_msg="GPA scale bound invalid. Must be between 0.0 and 4.0.", form_data=form_data)

        # 4. Registration Success Hook
        print(f"\n--- New Clean Data Registered ---")
        print(f"Name: {student_name} | ID: {student_id} | Age: {age} | GPA: {gpa}\n")
        
        success_message = f"Registration Successfully completed for {student_name}!"
        return render_template_string(HTML_TEMPLATE, success_msg=success_message, form_data={})

    return render_template_string(HTML_TEMPLATE, form_data={})

if __name__ == "__main__":
    app.run(debug=True)
