#!C:\Users\user\AppData\Local\Programs\Python\Python37\python.exe
import os
import cgi
import cgitb
import sqlite3

cgitb.enable()
form = cgi.FieldStorage()
db_name = "project.db"
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

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
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            background-color: #f0f0f0;
        }
        .header-container {
            display: flex;
            justify-content: center; /* Center the header */
            align-items: center;
            padding: 20px;
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
            width: 100px;
            height: 100px;
            border-radius: 50%;
            object-fit: cover;
        }
        .text-column {
            flex: 2;
            text-align: center;
        }
        .text-column h1 {
            margin: 0;
            color: #cc0000;
            font-size: 1.5rem;
        }
        .text-column p {
            margin: 5px 0;
            color: #333;
        }
        .navbar {
            background-color: #870E03;
            padding: 3px;
        }
        .navbar a {
            color: white;
            margin-right: 20px;
            text-decoration: none;
        }
        .navbar a:hover {
            text-decoration: underline;
        }
        .footer {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
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
            font-weight: 600; /* Bold */
            font-size: 15px;
            color: red; /* Red color for field names */
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
            margin-left:110px;
        }
        .content {
            margin: 20px auto;
            padding: 20px;
            max-width: 800px;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
        }
        .content h1 {
            text-align: center;
            color: black;
            font-size: 1.5rem;
            margin-bottom: 20px;
        }
        .form-group {
            margin-bottom: 10px;
        }
        .form-group label {
            display: block;
            margin-bottom: 20px;
            font-weight: 450;
        }
        .form-group select,
        .form-group input {
            width: 50%;
            padding: 5px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 1rem;
        }
        .form-group button:hover {
            background-color: #660000;
        }
        .notification {
            text-align: center;
            color: green;
            font-weight: 600;
            margin-bottom: 20px;
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
                <a class="mr-5 hover:text-lightgray text-white" href="index.html">HOME</a>
                <a class="mr-5 hover:text-lightgray text-white" href="about.html">ABOUT US</a>
                <a class="mr-5 hover:text-lightgray text-white" href="hodreq.py">GO BACK</a>
                <div class="dropdown">
                    <div class="dropdown-content">
                    </div>
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
print("Content-type: text/html\n")
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


# Add some spacing between navbar and "Employee Details" heading
print("<div style='margin-top: 5px;'></div>")

def get_req(reqno):
    cursor.execute("SELECT reqmet FROM requirement WHERE rowid=?", (reqno,))
    reqs = cursor.fetchone()
    return reqs
    
def generate_dropdown_reqmet():
    reqnos = [0, 1]
    dropdown_html = "<select name='reqmet' id='reqmet'>"
    for req in reqnos:
        dropdown_html += "<option value='{}'>{}</option>".format(req, req)
    dropdown_html += "</select>"
    return dropdown_html

def generate_dropdown_req():
    cursor.execute("SELECT rowid FROM requirement WHERE reqmet = 0")
    reqnos = cursor.fetchall()
    dropdown_html = "<select name='reqno' id='reqno'>"
    for req in reqnos:
        dropdown_html += "<option value='{}'>{}</option>".format(req[0], req[0])
    dropdown_html += "</select>"
    return dropdown_html

reqno = form.getvalue("reqno")
reqmet = form.getvalue("reqmet")

if reqno and reqmet:
    cursor.execute("UPDATE requirement SET reqmet = ? WHERE rowid = ?", (reqmet, reqno))
    conn.commit()
    print("<p class='notification'>Requirement updated successfully.</p>")

print("<div class='content'>")  # Centering main content
print("<h1>Updating HOD requirements</h1>")
print("<div class='form-group'>")
print("<form id='reqForm' method='post'>")
print("<div style='display: flex; justify-content: space-between;'>")  # Adjust input boxes to the right of labels
print("<label for='reqno'>Select Request No:</label>")
print(generate_dropdown_req())
print("</div>")
print("<div style='display: flex; justify-content: space-between;'>")  # Adjust input boxes to the right of labels
print("<label for='reqmet'>Request met (1 for yes/0 for no):</label>")
print(generate_dropdown_reqmet())
print("</div>")  # Center the buttons
print("<div style='text-align: center; margin-top: 25px;'>")  # Center the buttons
print("<div style='display: inline-block;'>")  # Container for buttons
print("<form id='reqForm' method='post' style='display: inline-block;'>")  # Form for Update button
print("<button type='submit' style='background-color: #800000; color: white; padding: 6px 45px; margin-right: 35px; border: none; border-radius: 5px;'>Update</button>")
print("</form>")
print("<form method='POST' action='hodreq.py' style='display: inline-block;'>")  # Form for View full details button
print("<button type='submit' style='background-color: #800000; color: white; padding: 7px 10px; border: none; border-radius: 5px;'>View updated table</button>")
print("</form>")
print("</div>")
print("</div>")


conn.close()
print(footer_html)
