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

# Function to calculate quantity available
def calculate_quantity_available(item_id):
    cursor.execute("SELECT SUM(issuequantity) FROM ivtable WHERE itemid=?", (item_id,))
    total_issue_quantity = cursor.fetchone()[0] or 0  # Fetch the sum of issue quantity
    cursor.execute("SELECT SUM(quantitybought) FROM rvtable WHERE itemid=?", (item_id,))
    quantity_bought = cursor.fetchone()[0] or 0  # Fetch the sum of quantity bought
    quantity_available = quantity_bought - total_issue_quantity
    return quantity_available

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
            justify-content: center; /* Center the header */
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
            flex: 10;
            flex: 10;
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
            font-weight: 600; /* Bold */
            font-size: 15px;
   
        }
        .nav__title1 {
            margin-top: 0.4em;  
            font-weight: 600;
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
                <a class="mr-5 hover:text-lightgray text-white" href="inventory.html">GO BACK</a>
                <div class='dropdown'>
                    <!-- Dropdown content -->
                </div>
            </nav>
            <div class='ml-auto mt-4 md:mt-0'>
                <!-- Additional content if any -->
            </div>
        </div>
    </header>
"""

# Common JavaScript code for table styling and alert
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

function showAlert(itemsBelowReorder) {
    if (itemsBelowReorder.length > 0) {
        var message = "The following items are below the reorder level:\\n";
        for (var i = 0; i < itemsBelowReorder.length; i++) {
            message += itemsBelowReorder[i] + "\\n";
        }
        alert(message);
    }
}
</script>
"""

# Footer HTML
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

# Print the Content-type header
print("Content-type: text/html\n")

# Print the header HTML
print(header_html)

# Print the JavaScript code
print(js_code)

# Generate HTML response for the second page
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Items Below Reorder Level</title>
    <style>
        body {
            font-family: 'Poppins', sans-serif;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            margin-bottom:20px;
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
        td {
            text-align: center;
        }
    </style>
</head>
<body>
    <h1>Items Below Reorder Level</h1>
    <table>
        <tr>
            <th>Item ID</th>
            <th>Item Name</th>
            <th>Reorder Level</th>
            <th>Quantity Available</th>
        </tr>
""")

# Fetch items with reorder levels
cursor.execute("SELECT itemid, itemname, reorderlvl FROM itemtable")
items = cursor.fetchall()

items_below_reorder_list = []

# Check and display items below reorder level
items_below_reorder = False
for item in items:
    item_id, item_name, reorder_level = item
    quantity_available = calculate_quantity_available(item_id)
    if quantity_available < reorder_level:
        items_below_reorder = True
        items_below_reorder_list.append(item_name)
        print(f"<tr><td>{item_id}</td><td>{item_name}</td><td>{reorder_level}</td><td>{quantity_available}</td></tr>")

if not items_below_reorder:
    print("<tr><td colspan='4' style='text-align:center;'>No items below reorder level.</td></tr>")

print("""
    </table>
</body>
</html>
""")

# Set JavaScript variable if items are below reorder level
print("<script>")
print(f"showAlert({str(items_below_reorder_list)});")   # Convert items_below_reorder to lowercase boolean string
print("</script>")

# Close cursor and database connection
cursor.close()
conn.close()

# Print the footer HTML
print(footer_html)