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
    }
    .header-container {
        display: flex;
        justify-content: left; 
        align-items: left; 
        padding: 10px;
        width: 100%;
        top: 0;
        z-index: 1000;
        margin-right: 100px;
        text-align: center;
        background-color: #f8f8f8;
        border-bottom: 2px solid #800000;
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
    </style>
    
    <title>Inventory Management</title>
</head>
<body>
    <div class="header-container">
        <div class="logo-column">
            
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

# Generate HTML response
print("Content-type: text/html\n")
print(header_html)

# JavaScript code for table styling
js_code = """
<script>
document.addEventListener("DOMContentLoaded", function() {
    var tableRows = document.querySelectorAll("table tr");
    for (var i = 0; i < tableRows.length; i++) {
        tableRows[i].style.backgroundColor = i % 2 == 0 ? "#f2f2f2" : "#ffffff";
        tableRows[i].addEventListener("mouseover", function() {
            this.style.backgroundColor = "#e0e0e0";
        });
        tableRows[i].addEventListener("mouseout", function() {
            var rowIndex = Array.prototype.indexOf.call(this.parentNode.children, this);
            this.style.backgroundColor = rowIndex % 2 == 0 ? "#f2f2f2" : "#ffffff";
        });
    }
});
</script>
"""

# Insert the JavaScript code into the HTML
print(js_code)

# Insert the extracted navbar HTML here
print("""
<header class='text-gray-600 body-font navbar'>
    <div class='container mx-auto relative flex flex-wrap p-3 flex-col md:flex-row items-start' style='margin-top: -20px;'>
        <nav class='flex flex-wrap items-start text-base justify-start'>    
            <div class='dropdown-content'>
            </div>
        </nav>  
        <div class='ml-auto mt-4 md:mt-0'>
        </div>
    </div>
</header>
""")

# Fetch the row with the largest ivnumber from ivtable
cursor.execute("SELECT issuedate, itemid, issuequantity, ivnumber, depname FROM ivtable INNER JOIN department ON ivtable.depid = department.depid ORDER BY ivnumber DESC LIMIT 1")
row = cursor.fetchone()

if row:
    current_date = datetime.datetime.now().date()
    reqdate = current_date.strftime("%d-") + current_date.strftime("%b").lower() + current_date.strftime("-%Y")
    
    # Display the formatted IV Number
    print("<div style='text-align: center; margin-bottom: 30px;'>")
    print("<p>ISSUE VOUCHER:</p>")
    print("</div>")
    print("<div style='text-align: left; margin-bottom: -25px; margin-left: 10px;'>")
    print(f"<p>IV NO: {row[3]}</p>")  # Display IV Number
    print("</div>")
    print("<div style='text-align: right; margin-bottom: 60px;'>")
    print(f"<p>DATE: {reqdate}</p>")  # Display current date
    print("</div>")

    # Display the table header
    print("<div style='text-align: center;'>")
    print("<table style='margin: 0 auto; border-collapse: collapse;'>")
    print("<tr>")
    print("<th style='padding: 10px; border: 1px solid #ccc;'>S.No</th>")

    print("<th style='padding: 10px; border: 1px solid #ccc;'>Item Name</th>")
    print("<th style='padding: 10px; border: 1px solid #ccc;'>Quantity</th>")
    print("<th style='padding: 10px; border: 1px solid #ccc;'>Department</th>")
    print("</tr>")

    # Fetch item name using item ID
    cursor.execute("SELECT itemname FROM itemtable WHERE itemid=?", (row[1],))
    item_name = cursor.fetchone()[0]
    
    cursor.execute("SELECT depid FROM department WHERE depname=?", (row[4],))
    dep_name = cursor.fetchone()[0]

    # Display the fetched row
    print("<tr style='height: 50px;'>")  # Adjust the height as needed
    print(f"<td style='padding: 10px; border: 1px solid #ccc;'>1</td>")  # Serial number

    print(f"<td style='padding: 10px; border: 1px solid #ccc;'>{item_name}</td>")  # Item Name
    print(f"<td style='padding: 10px; border: 1px solid #ccc;'>{row[2]}</td>")  # Quantity
    print(f"<td style='padding: 10px; border: 1px solid #ccc;'>{dep_name}</td>")  # Department
    print("</tr>")

    # Add six empty rows
    for _ in range(6):
        print("<tr style='height: 50px;'>")  # Adjust the height as needed
        for _ in range(4):  # Adjusted to print only the first 5 columns
            print("<td style='padding: 10px; border: 1px solid #ccc;'></td>")
        print("</tr>")

    print("</table>")
    print("</div>")

    # Add additional formatting as needed
    print("<div style='text-align: left; margin-bottom: 20px;'>")
    print("<p>&nbsp;&nbsp;</p>")  # Adjust as needed
    print("</div>")

    # Additional information
    print("<div style='text-align: left; margin-top: 80px; margin-left: 30px;'>")
    print("<p>Inventory Clerk: &nbsp;&nbsp;</p>")  # Adjust as needed
    print("</div>")
    print("<div style='text-align: right; margin-top: -30px; margin-left: 30px;'>")
    print("<p>Issued By: &nbsp;&nbsp;</p>")  # Adjust as needed
    print("</div>")

print("</div>")
print("</body>")
print("</html>")