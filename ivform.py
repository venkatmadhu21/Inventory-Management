#!C:\Users\user\AppData\Local\Programs\Python\Python37\python.exe
import os
import cgi
import cgitb
import sqlite3
import datetime

cgitb.enable()
form = cgi.FieldStorage()
db_name = "project.db"

try:
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
except Exception as e:
    print("Content-Type: text/html\n")
    print(f"<html><body><h1>Database connection error: {e}</h1></body></html>")
    exit()

# Common header HTML with CSS styles and scripts
header_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
    body {
        font-family: 'Poppins', sans-serif;
    }
    .header-container {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 10px;
        width: 100%;
        top: 0;
        z-index: 1000;
        text-align: center;
        background-color: #f8f8f8;
        border-bottom: 2px solid #800000;
    }
    .logo-column {
        flex: 1;
        text-align: left;
    }
    .logo {
        width: 120px;
        height: 120px;
        border-radius: 50%;
        object-fit: cover;
    }
    .text-column {
        flex: 2;
        text-align: center;
        margin-left: -600px; /* Add this line to shift the text column to the left */
    }
    .text-column h1 {
        margin: 0;
        color: #cc0000;
    }
    .text-column p {
        margin: 5px 0;
        color: #333;
    }
    .footer {
        display: flex;
        justify-content: space-between; /* Corrected syntax */
        align-items: center; /* Adjusted alignment */
        padding: 0 30px;
        color: #ffffff;
        background-color: #870E03;
        position: absolute;
        height: 66px;
        bottom: 0;
        left: 0;
        right: 0;
        font-family: 'Poppins', sans-serif;
    }
    .footer__section {
        flex: 1;
    }
    .footer__addr {
        margin-bottom: 2em;
    }
    .footer__logo {
        font-family: 'Poppins', sans-serif;
        font-weight: 400;
        text-transform: uppercase;
        font-size: 1.5rem;
    }
    .footer__addr h2 {
        margin-top: 0.4em;
        font-size: 15px;
        font-weight: 400;
    }
    .nav__title {
        margin-top: 0.4em;
        font-weight: 600;
        font-size: 15px;
        color: red;
    }
    .nav__title1 {
        margin-top: 0.4em;
        font-weight: 400;
        font-size: 15px;
        margin-left: 110px;
    }
    .footer address {
        margin-top: 0.4em;
        font-style: normal;
        color: white;
    }
    .footer__btn {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 36px;
        max-width: max-content;
        background-color: rgb(33, 33, 33, 0.07);
        border-radius: 100px;
        color: white;
        line-height: 0;
        margin: 0.6em 0;
        font-size: 1rem;
        padding: 0 1.3em;
    }
    .footer ul {
        list-style: none;
        padding-left: 0;
    }
    .footer li {
        line-height: 2em;
    }
    .footer a {
        text-decoration: none;
    }
    .footer__nav {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
        align-items: flex-start;
        width: 100%;
    }
    .nav__ul a {
        color: white;
    }
    .nav__ul1 {
        margin-left: 110px;
    }
</style>
    
    <title>Inventory Management</title>
</head>
<body>
    <div class="header-container">
        <div class="logo-column">
            <img src="images/logo.png" class="logo">
        </div>
        <div class="text-column">
            <h1 class="text-4xl font-semibold main-heading">Keshav Memorial College Of Engineering</h1>
            <p class="text-lg font-medium sub-heading mt-2">A unit of Keshav Memorial Technical Educational Society (KMTES)</p>
            <p class="text-sm highlight mt-1">Approved by AICTE, New Delhi - Affiliated to Jawaharlal Nehru Technological University, Hyderabad</p>
        </div>
    </div>

    <header class="text-gray-600 body-font navbar">
        <div class="container mx-auto relative flex flex-wrap p-5 flex-col md:flex-row items-start">
            <nav class="flex flex-wrap items-start text-base justify-start">
              
                <div class="dropdown">
                    <!-- Dropdown content -->
                </div>
            </nav>
            <div class="ml-auto mt-4 md:mt-0">
             
              
            </div>
        </div>
    </header>
"""

footer_html = """
<footer class="footer">
    <div class="footer_section footer_addr">
        <h2>Contact</h2>
        <address style="color: white;">
            Office : 8499981497<br>
        </address>
    </div>
    
    <div class="footer__section">
        <h2 class="nav__title1">Email id:</h2>
        <ul class="nav__ul1">
            <li>
                <a href="mailto:admin@kmce.in" style="color: white;">admin@kmce.in</a>
            </li>
        </ul>
    </div>
    
    <div class="footer__section">
        <h2 class="nav__title">Landline:</h2>
        <ul class="nav__ul" style="color: white;">
            <li>
                <a href="tel:040-xxxx-123">040-xxxx-123</a>
            </li>
        </ul>
    </div>
    
    <div class="footer__section">
        <h2 class="nav__title">Address:</h2>
        <ul class="nav__ul" style="color: white;">
            <li>
                <a href="#">Koheda Road, Ibrahimpatnam</a>
            </li>
        </ul>
    </div>
</footer>
</body>
</html>
"""

# Generate HTML response
print("Content-Type: text/html\n")
print(header_html)

# JavaScript code for table styling
js_code = """
<script>
document.addEventListener("DOMContentLoaded", function() {
    var tableRows = document.querySelectorAll("table tr");
    for (var i = 0; i < tableRows.length; i++) {
        tableRows[i].style.backgroundColor = i % 2 == 0 ? "#f2f2f2" : "#ffffff"; // Alternate row colors
        tableRows[i].addEventListener("mouseover", function() {
            this.style.backgroundColor = "#e0e0e0"; // Hover effect
        });
        tableRows[i].addEventListener("mouseout", function() {
            var rowIndex = Array.prototype.indexOf.call(this.parentNode.children, this);
            this.style.backgroundColor = rowIndex % 2 == 0 ? "#f2f2f2" : "#ffffff"; // Restore original color on mouseout
        });
    }
});
</script>
"""

# Insert the JavaScript code into the HTML
print(js_code)

# Insert the extracted navbar HTML here
print("""
<header class='text-gray-600 body-font navbar' style='background-color: #800000;'>
    <div class='container mx-auto relative flex flex-wrap p-3 flex-col md:flex-row items-start' style='margin-top: -20px;'>
        <nav class='flex flex-wrap items-start text-base justify-start'>
            <a class='mr-5 hover:text-lightgray text-white' href='index.html'>HOME</a>
            <a class='mr-5 hover:text-lightgray text-white' href='about.html'>ABOUT US</a>
            <a class="mr-5 hover:text-lightgray text-white" href="indeventoryman.html">GO BACK</a>
            <div class='dropdown'>
                <div class='dropdown-content'>
                </div>
            </div>
        </nav>
        <div class='ml-auto mt-4 md:mt-0'>
        </div>
    </div>
</header>
""")

def generate_item_dropdown():
    cursor.execute("SELECT DISTINCT itemname FROM itemtable")
    items = cursor.fetchall()
    dropdown_html = "<select name='itemname' id='itemname' onchange='displayDepartments()' style='border: 1px solid #800000; padding: 5px; display: inline-block;'>"
    dropdown_html += "<option value='' selected disabled>Select Item</option>"  # Set default option
    for item in items:
        dropdown_html += "<option value='{}'>{}</option>".format(item[0], item[0])
    dropdown_html += "</select>"
    return dropdown_html



# Function to generate dropdown for departments
def generate_department_dropdown():
    cursor.execute("SELECT DISTINCT depname FROM department")
    departments = cursor.fetchall()
    dropdown_html = "<select name='department' id='department' style='border: 1px solid #800000; padding: 5px; display: inline-block;'>"
    dropdown_html += "<option value='' selected disabled>Select Department</option>"  # Set default option
    for department in departments:
        dropdown_html += "<option value='{}'>{}</option>".format(department[0], department[0])
    dropdown_html += "</select>"
    return dropdown_html

# Function to generate quantity input
def generate_quantity_input():
    return "<input type='text' id='quantity' name='quantity' style='border: 1px solid #800000; padding: 5px;' placeholder='Enter Quantity'>"

# Function to generate issue date input
def generate_issue_date_input():
    return "<input type='date' id='issueDate' name='issueDate' style='border: 1px solid #800000; padding: 5px;'>"

# Generate HTML response
# Add the heading for IV Details
print("<div style='text-align: center;'>")
print("<h2 style='color: red;'>IV Details</h2>")
print("</div>")

# Add form container with center alignment
print("<div style='text-align: center;'>")

# Print the form elements
print("<form id='ivDetailsForm' method='post'>")

# Select Item Dropdown
print("<label for='itemname' style='color: red;'>Select Item name:</label>")
print(generate_item_dropdown())
print("<br>")

# Select Department Dropdown
print("<label for='department' style='color: red;'>Select Department:</label>")
print(generate_department_dropdown())
print("<br>")

# Quantity Input
print("<label for='quantity' style='color: red;'>Quantity:</label>")
print(generate_quantity_input())
print("<br>")

# Issue Date Input
print("<label for='issueDate' style='color: red;'>Issue Date:</label>")
print(generate_issue_date_input())
print("<br>")

# Submit Button
print("<input type='submit' value='Submit' style='background-color: #800000; color: white; border: none; padding: 10px 20px; cursor: pointer;'>")

# Close form
print("</form>")

# Close form container
print("</div>")

# Check if the form has been submitted
if form.getvalue("itemname"):
    itemname = form.getvalue("itemname")
    department = form.getvalue("department")
    quantity = form.getvalue("quantity")
    issue_date = form.getvalue("issueDate")

    try:
        # Fetch itemid from itemtable based on itemname
        cursor.execute("SELECT itemid FROM itemtable WHERE itemname=?", (itemname,))
        item_result = cursor.fetchone()
        item_id = item_result[0] if item_result else None

        # Fetch depid from department table based on department
        cursor.execute("SELECT depid FROM department WHERE depname=?", (department,))
        department_result = cursor.fetchone()
        dep_id = department_result[0] if department_result else None

        # If either item_id or dep_id is None, display an error message
        if item_id is None or dep_id is None:
            print(f"<html><body><h1>Invalid item or department selected.</h1></body></html>")
        else:
            # Generate new ivnumber (similar to rvnumber)
            cursor.execute("SELECT ivnumber FROM ivtable ORDER BY ivnumber DESC LIMIT 1")
            last_iv_number = cursor.fetchone()

            if last_iv_number:
                last_digits = int(last_iv_number[0].split("-")[1]) + 1
                new_iv_number = "IV-{0:03d}-2024".format(last_digits)
            else:
                new_iv_number = "IV-001-2024"

            # Insert data into ivprint table
            cursor.execute("INSERT INTO ivtable (ivnumber, itemid,  issuequantity, depid,issuedate) VALUES (?, ?, ?, ?, ?)",
                           (new_iv_number, item_id, quantity, dep_id, issue_date))

            conn.commit()

            # Redirect to ivprint.py
            redirect_script = """
            <script>
            window.location.replace("ivprint.py");
            </script>
            """
            print(redirect_script)

    except Exception as e:
        print(f"<html><body><h1>Error: {e}</h1></body></html>")

# Footer HTML (previously defined)
print(footer_html)

# Close the database connection
conn.close()
