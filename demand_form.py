#!C:\Users\user\AppData\Local\Programs\Python\Python37\python.exe
import os
import cgi
import cgitb
import sqlite3
import datetime

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
            display: flex;
            flex-direction: column;
            min-height: 100vh;
            margin: 0;
        }
        .header-container {
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 10px;
            width: 100%;
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
        }
        .text-column h1 {
            margin: 0;
            color: #cc0000;
        }
        .text-column p {
            margin: 5px 0;
            color: #333;
        }
        .navbar {
            background-color: #870E03;
            padding: 10px;
        }
        .content {
            display: flex;
            flex: 1;
            margin: 20px;
            justify-content: space-around;
        }
        .form-container, .table-container {
            padding: 20px;
        }
        .form-container {
            flex: 1;
            max-width: 400px;
            border: 1px solid #ccc;
            border-radius: 10px;
            padding: 20px;
        }
        .table-container {
            flex: 2;
        }
        .footer {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            padding: 0 30px;
            color: #ffffff;
            background-color: #870E03;
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
        .styled-table {
            border-collapse: collapse;
            margin: 25px 0;
            font-size: 0.9em;
            font-family: 'Poppins', sans-serif;
            min-width: 400px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
        }
        .styled-table thead tr {
            background-color: #009879;
            color: #ffffff;
            text-align: left;
        }
        .styled-table th,
        .styled-table td {
            padding: 12px 15px;
        }
        .styled-table tbody tr {
            border-bottom: 1px solid #dddddd;
        }
        .styled-table tbody tr:nth-of-type(even) {
            background-color: #f3f3f3;
        }
        .styled-table tbody tr:last-of-type {
            border-bottom: 2px solid #009879;
        }
        .form-container h2 {
            text-align: center;
            color: #800000;
            margin-bottom: 20px;
        }
        .form-container label {
            color: #800000;
        }
        .form-container input[type="text"], .form-container select {
            width: calc(100% - 22px);
            padding: 10px;
            margin: 10px 0;
            border: 1px solid black;
            border-radius: 5px;
        }
        .form-container button {
            width: 100%;
            padding: 10px;
            background-color: #800000;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
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
                <a class='mr-5 hover:text-lightgray text-white' href='index.html'>HOME</a>
                <a class='mr-5 hover:text-lightgray text-white' href='about.html'>ABOUT US</a>
                <a class="mr-5 hover:text-lightgray text-white" href="hod.html">GO BACK</a>
            </nav>
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

# Handling form submission for inserting new department records
current_date = datetime.datetime.now().date()
reqdate = current_date.strftime("%d-") + current_date.strftime("%b").lower() + current_date.strftime("-%Y")

if "action" in form and form["action"].value == "Insert" and "empid" in form and "itemid" in form and "quantity" in form:
    empid = form["empid"].value
    itemid = form["itemid"].value
    quantity = form["quantity"].value
    reqmet = 0

    # Insert the new entry
    cursor.execute("INSERT INTO requirement (empid, itemid, quantity, reqdate, reqmet) VALUES (?, ?, ?, ?, ?)", (empid, itemid, quantity, reqdate, reqmet))
    conn.commit()
    print("<p style='text-align: center; color: green;'>Requirement sent successfully!</p>")
else:
    if "action" in form and form["action"].value == "Insert":
        print("<p style='text-align: center; color: red;'>Filing the requirement failed. Please check your input.</p>")

# Fetch items from itemtable
cursor.execute("SELECT itemid, itemname FROM itemtable")
items = cursor.fetchall()

# HTML form for inserting new department records with dropdown for itemid
print("""
<div class="content">
    <div class="form-container">
        <h2>Requirement Form</h2>
        <form method="POST" action="">
            <input type="hidden" name="action" value="Insert">
            <label for="empid">EmpID:</label>
            <input type="text" id="empid" name="empid" required><br><br>
            <label for="itemid">ItemID:</label>
            <select id="itemid" name="itemid" required>
""")

# Populate the dropdown with items
for item in items:
    print(f"<option value='{item[0]}'>{item[0]}-{item[1]}</option>")

print("""
            </select><br><br>
            <label for="quantity">Quantity:</label>
            <input type="text" id="quantity" name="quantity" required><br><br>
            <button type="submit">Submit</button>
        </form>
    </div>
    <div class="table-container">
""")

# Query the database for logs from the current date
cursor.execute("SELECT empid, itemid, quantity, reqdate, reqmet FROM requirement WHERE reqdate = ?", (reqdate,))
logs = cursor.fetchall()

# Prepare log data with additional employee information
data = []
for log in logs:
    empid = log[0]
    empname = list(cursor.execute("SELECT fname FROM employee WHERE empid = ?", (empid,)))
    depid = list(cursor.execute("SELECT depid FROM employee WHERE empid = ?", (empid,)))
    
    empname_value = empname[0][0] if empname else "Unknown"
    depid_value = depid[0][0] if depid else "Unknown"
    
    data.append([empid, empname_value, depid_value, log[1], log[2], log[3], log[4]])

# Display logs if there are any records for the current date
if data:
    print("<div style='margin-top: 20px; text-align: center;'>")
    print("<h2 style='color: #800000;'>Logs for " + reqdate + "</h2>")
    print("<table class='styled-table' style='margin: 0 auto;'>")
    print("<thead><tr><th>Employee ID</th><th>Employee Name</th><th>Department ID</th><th>Item ID</th><th>Quantity</th><th>Request Date</th><th>Request Met</th></tr></thead>")
    print("<tbody>")
    for log in data:
        print("<tr>")
        print("<td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td>".format(log[0], log[1], log[2], log[3], log[4], log[5], log[6]))
        print("</tr>")
    print("</tbody>")
    print("</table>")
    print("</div>")
else:
    print("<p style='text-align: center; color: red;'>No logs found for " + reqdate + "</p>")

print("</div></div>")  # Close table-container and content divs

# Close the database connection
conn.close()

print(footer_html)
