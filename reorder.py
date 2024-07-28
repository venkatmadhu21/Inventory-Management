#!C:\Users\user\AppData\Local\Programs\Python\Python37\python.exe
import cgi
import cgitb
import sqlite3

# Enable CGI error reporting for easier debugging
cgitb.enable()

# Establish connection to SQLite database
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
            margin: 0; /* Added to remove default margin */
        }
        .header-container {
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 22px;
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
            height: 66px;
            font-family: 'Poppins', sans-serif;
            margin-top:20px;
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

# Print the initial content-type and header HTML
print("Content-type: text/html\n")
print(header_html)

# Fetch and display items with their reorder levels from the database
def display_item_table():
    cursor.execute("SELECT itemid, reorderlvl, itemname FROM itemtable")
    rows = cursor.fetchall()
    if rows:
        print("<div style='max-width: 800px; margin: auto;padding-top: -20px;'>")  # Limiting the width of the table
        print("<table>")
        print("<tr><th>Item ID</th><th>Item Name</th><th>Reorder Level</th></tr>")
        for row in rows:
            print(f"<tr><td>{row[0]}</td><td>{row[2]}</td><td>{row[1]}</td></tr>")
        print("</table>")
        print("</div>")
    else:
        print("<p>No items found.</p>")
 

# Display item table initially
display_item_table()

# HTML form for checking items below reorder level
print("""
    <div class="button-container" style="text-align: center; margin-top: 0px;">
        <form method="post" action="itembelowreorder.py">
            <button type="submit" class="button" name="check_reorder_button"  style="background-color:#800000 ; color: white;height: 40px; margin-top:20px;">Check Items Below Reorder Level</button>
        </form>
    </div>
""")

# Print the footer HTML
print(footer_html)

# Close the database connection
conn.close()
