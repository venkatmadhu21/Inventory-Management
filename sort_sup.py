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
            padding: 0px 30px;
            color: #ffffff;
            background-color: #870E03;
            position: relative;
            bottom: 0;
            left: 0;
            right: 0;
            font-family: 'Poppins', sans-serif;
            flex-wrap: wrap;
            z-index: 1000;
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
        .form-container {
            text-align: center;
            padding: 20px;
        }
        .form-container form {
            display: inline-block;
            margin: auto;
            text-align: left;
        }
        .form-container label {
            color: #800000;
            font-weight: bold;
        }
        .form-container select, .form-container button {
            margin-left: 10px;
            padding: 5px;
            border: 1px solid #800000;
        }
        .form-container button {
            background-color: #800000;
            color: white;
            border: none;
            cursor: pointer;
            padding: 5px 15px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            font-size: 0.9em;
            min-width: 400px;
            overflow-x: auto;
        }
        table thead tr {
            background-color: #800000;
            color: #ffffff;
            text-align: left;
            font-weight: bold;
        }
        table th, table td {
            padding: 12px 15px;
            text-align: center;
        }
        table tbody tr {
            border-bottom: 1px solid #dddddd;
        }
        table tbody tr:nth-of-type(even) {
            background-color: #f3f3f3;
        }
        table tbody tr:last-of-type {
            border-bottom: 2px solid #800000;
        }
        table tbody tr:hover {
            background-color: #f1f1f1;
        }
        @media (max-width: 768px) {
            .text-column h1 {
                font-size: 1.5em;
            }
            .text-column p {
                font-size: 1em;
            }
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

    <header class='text-gray-600 body-font navbar' style='background-color: #800000;'>
        <div class='container mx-auto relative flex flex-wrap p-3 flex-col md:flex-row items-start' style='margin-top: -20px;'>
            <nav class='flex flex-wrap items-start text-base justify-start'>
                <a class='mr-5 hover:text-lightgray text-white' href='index.html'>HOME</a>
                <a class='mr-5 hover:text-lightgray text-white' href='about.html'>ABOUT US</a>
                <a class='mr-5 hover:text-lightgray text-white' href='inventory.html'>GO BACK</a>
                <div class='dropdown'>
                    <div class='dropdown-content'>
                    </div>
                </div>
            </nav>
            <div class='ml-auto mt-4 md:mt-0'>
            </div>
        </div>
    </header>

    <div style='margin-top: 20px;'></div>

    <!-- Form to select field for sorting employee details -->
    <div class="form-container">
        <form method='post' action=''>
            <label for='sort_field'>Select Field to Sort By:</label>
            <select id='sort_field' name='sort_field'>
                <option value='supid'>Supplier ID</option>
                <option value='sname'>Supplier Name</option>
                <option value='address'>Address</option>
                <option value='emailid'>Email ID</option>
                <option value='phoneno1'>Phone No 1</option>
                <option value='phoneno1'>Phone No 2</option>
                <option value='phoneno1'>Phone No 3</option>
                <option value='blacklisted'>Blacklisted</option>
            </select><br><br>
            <button type='submit' name='action' value='Sort'>Sort</button>
        </form>
    </div>
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

# Handle form submission
if "action" in form and form["action"].value == "Sort":
    sort_field = form.getvalue('sort_field')

    # Sanitize input to prevent SQL injection
    valid_sort_fields = ['supid', 'sname', 'address', 'emailid', 'phoneno1', 'phoneno2', 'phoneno3', 'blacklisted']
    if sort_field not in valid_sort_fields:
        sort_field = 'supid'  # Default sort field

    query = f"""
    SELECT supid, sname, area || ', ' || locality || ', ' || pincode AS address, emailid, phoneno1, phoneno2, phoneno3, blacklisted from suppliers ORDER BY {sort_field}
    """
    
    cursor.execute(query)
    rows = cursor.fetchall()

    # Display sorted data in a table
    print("<div style='overflow-x: auto;'>")
    print("<table id='employeeTable'>")
    print("<thead>")
    print("<tr>")
    print("<th>Supplier ID</th>")
    print("<th>Supplier Name</th>")
    print("<th>Address</th>")
    print("<th>Email ID</th>")
    print("<th>Phone No 1</th>")
    print("<th>Phone No 2</th>")
    print("<th>Phone No 3</th>")
    print("<th>Blacklisted</th>")
    print("</tr>")
    print("</thead>")
    print("<tbody>")

    for row in rows:
        print("<tr>")
        for cell in row:
            print(f"<td>{cell}</td>")
        print("</tr>")

    print("</tbody>")
    print("</table>")
    print("</div>")

# Close the database connection
conn.close()

print(footer_html)