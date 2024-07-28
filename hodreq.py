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
            padding: 2px;
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
    <header class="navbar">
        <div class="container mx-auto relative flex flex-wrap p-5 flex-col md:flex-row items-start">
            <nav class="flex flex-wrap items-start text-base justify-start">
                <a class='mr-5 hover:text-lightgray text-white' href='index.html'>HOME</a>
                <a class='mr-5 hover:text-lightgray text-white' href='about.html'>ABOUT US</a>
                <a class="mr-5 hover:text-lightgray text-white" href="reqdetails.py">GO BACK</a>
            </nav>
        </div>
    </header>
"""

footer_html = """
<footer class="footer">
        <div class="footer__section footer_addr">
            <h2>Contact</h2>
            <address>
                Office : 8499981497<br>
            </address>
        </div>

        <div class="footer__section">
            <h2 class="nav__title">Email id:</h2>
            <ul class="nav__ul">
                <li>
                    <a href="mailto:admin@kmce.in">admin@kmce.in</a>
                </li>
            </ul>
        </div>

        <div class="footer__section">
            <h2 class="nav__title">Landline:</h2>
            <ul class="nav__ul">
                <li>
                    <a href="tel:040-xxxx-123">040-xxxx-123</a>
                </li>
            </ul>
        </div>

        <div class="footer__section">
            <h2 class="nav__title">Address:</h2>
            <ul class="nav__ul">
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

# Add some spacing between navbar and "Department Details" heading
print("<div style='margin-top: 10px;'></div>")


# Query the database for logs from the current date

query = """
SELECT requirement.rowid, requirement.empid, requirement.itemid, itemtable.itemname, requirement.quantity, requirement.reqdate, requirement.reqmet
FROM requirement
JOIN itemtable ON requirement.itemid = itemtable.itemid
WHERE requirement.reqmet = 0
"""

cursor.execute(query)
#cursor.execute("SELECT rowid, empid, itemid, quantity, reqdate, reqmet FROM requirement WHERE reqmet = 0")
logs = cursor.fetchall()

# Prepare log data with additional employee information
data = []
for log in logs:
    empid = log[1]
    empname = list(cursor.execute("SELECT fname FROM employee WHERE empid = ?", (empid,)))
    depid = list(cursor.execute("SELECT depid FROM employee WHERE empid = ?", (empid,)))
    
    empname_value = empname[0][0] if empname else "Unknown"
    depid_value = depid[0][0] if depid else "Unknown"
    
    data.append([log[0], empid, empname_value, depid_value, log[2], log[3], log[4], log[5], log[6]])

# Display logs if there are any records for the current date
if data:
    print("<div style='margin-top: 7px; margin-bottom: 5px; text-align: center;'>")
    print("<h1 style='color: #800000;font-size: 1.5rem;'>REQUIREMENTS</h1>")
    print("</div>")
    print("<div style='margin-top: 5px; margin-bottom: 5px; text-align: center;'>")
    print("<table class='styled-table' style='margin: 0 auto;'>")
    print("<thead><tr><th>Request No</th><th>Employee ID</th><th>Employee Name</th><th>Department ID</th><th>Item ID</th><th>Item Name</th><th>Quantity</th><th>Request Date</th><th>Request Met</th></tr></thead>")
    print("<tbody>")
    for log in data:
        print("<tr>")
        print("<td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td>".format(log[0], log[1], log[2], log[3], log[4], log[5], log[6], log[7], log[8]))
        print("</tr>")
    print("</tbody>")
    print("</table>")
    print("</div>")
else:
    print("<p style='text-align: center; color: red;'>No new logs found</p>")

print("<div style='text-align: center; margin-top: 25px;'>")  # Center the buttons    
print("<div style='display: inline-block; '>")  # Container for buttons
print("<form method='POST' action='update_hodreq.py' style='display: inline-block;'>")  # Form for Update button
print("<button type='submit' style='background-color: #800000; color: white; padding: 6px 45px; margin-right: 35px; border: none; border-radius: 5px;'>Update requirement</button>")
print("</form>")
print("<form method='POST' action='check_indent.py' style='display: inline-block;'>")  # Form for View full details button
print("<button type='submit' style='background-color: #800000; color: white; padding: 7px 45px; border: none; border-radius: 5px;'>Check for quantity left</button>")
print("</form>")
print("</div>")
print("</div>")


# Close the database connection
conn.close()

print(footer_html)
