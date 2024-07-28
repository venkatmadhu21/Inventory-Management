#!C:\Users\user\AppData\Local\Programs\Python\Python37\python.exe
import cgi
import cgitb
import sqlite3
import json

# Enable traceback for debugging CGI scripts
cgitb.enable()

# Establish connection to SQLite database
db_name="project.db"
conn=sqlite3.connect(db_name)
cursor = conn.cursor()

# Function to get suppliers based on item name
def get_suppliers(itemname):
    cursor.execute(""" 
                   SELECT 
               supid,
               sname, 
               emailid, 
               phoneno1, 
               phoneno2, 
               phoneno3, 
               blacklisted, 
               area || ', ' || locality || ', ' || pincode AS address 
                   FROM suppliers WHERE supid IN (SELECT supid FROM itemtable WHERE itemname=?)""", (itemname,))
    suppliers = cursor.fetchall()
    return suppliers

# Generate HTML for dropdown menu
def generate_dropdown():
    cursor.execute("SELECT DISTINCT itemname FROM itemtable")
    items = cursor.fetchall()
    dropdown_html = "<select name='itemname' id='itemname'>"
    for item in items:
        dropdown_html += "<option value='{}'>{}</option>".format(item[0], item[0])
    dropdown_html += "</select>"
    return dropdown_html

# Get form data
form = cgi.FieldStorage()

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
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        table, th, td {
            border: 1px solid #ddd;
            padding: 8px;
        }
        th {
            padding-top: 12px;
            padding-bottom: 12px;
            text-align: left;
            background-color: #4CAF50;
            color: white;
        }
        .centered {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .centered form {
            width: 100%;
            max-width: 600px;
            text-align: center;
        }
        .centered table {
            width: 100%;
            max-width: 800px;
        }
    </style>
    <title>Supplier Details</title>
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
    <header class='text-gray-600 body-font navbar' style='background-color: #800000;'>
        <div class='container mx-auto relative flex flex-wrap p-3 flex-col md:flex-row items-start' style='margin-top: -20px;'>
            <nav class='flex flex-wrap items-start text-base justify-start'>
                <a class='mr-5 hover:text-lightgray text-white' href='index.html'>HOME</a>
                <a class='mr-5 hover:text-lightgray text-white' href='about.html'>ABOUT US</a>
                <a class="mr-5 hover:text-lightgray text-white" href="inventory.html">GO BACK</a>
                <div class='dropdown'>
                    <div class='dropdown-content'></div>
                </div>
            </nav>
            <div class='ml-auto mt-4 md:mt-0'></div>
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
            <li><a href="mailto:admin@kmce.in" style="color: white;">admin@kmce.in</a></li>
        </ul>
    </div>
    <div class="footer__section">
        <h2 class="nav__title">Landline:</h2>
        <ul class="nav__ul" style="color: white;">
            <li><a href="tel:040-xxxx-123">040-xxxx-123</a></li>
        </ul>
    </div>
    <div class="footer__section">
        <h2 class="nav__title">Address:</h2>
        <ul class="nav__ul" style="color: white;">
            <li><a href="#">Koheda Road, Ibrahimpatnam</a></li>
        </ul>
    </div>
</footer>
</body>
</html>
"""

# Generate HTML response
print("Content-type: text/html\n")
print(header_html)

# Get item name from form submission
itemname = form.getvalue("itemname")
suppliers = []
if itemname:
    suppliers = get_suppliers(itemname)

# Output HTML response
print("<div class='centered'>")
print("<h1 style='font-size: 32px;'>Supplier Details</h1>")
print("<form id='supplierForm' method='post'>")
print("<label for='itemname' style='font-size: 18px;'>Select Item name:</label>")
print(generate_dropdown())
print("<button type='submit' style='background-color: #800000; color: white;padding: 10px 20px; font-size: 16px; border: none; cursor: pointer; margin-top:20px;'>Display Suppliers</button>")
print("</form>")
print("</div>")
print("<div class='centered' id='supplierTable'>")
if suppliers:
    print("<table>")
    print("<tr><th>Supplier ID</th><th>Supplier Name</th><th>Email ID</th><th>Phone No 1</th><th>Phone No 2</th><th>Phone No 3</th><th>Blacklisted</th><th>Address</th></tr>")
    for supplier in suppliers:
        print("<tr>")
        for field in supplier:
            print("<td>{}</td>".format(field))
        print("</tr>")
    print("</table>")
else:
    if itemname:
        print("<p>No suppliers found for the selected item '{}'.</p>".format(itemname))
    else:
        print("<p>Please select an item to view suppliers.</p>")
print("</div>")

print(footer_html)
cursor.close()
conn.close()