#!C:\Users\user\AppData\Local\Programs\Python\Python37\python.exe
import os
import cgi
import cgitb
import sqlite3
import re

cgitb.enable()
form = cgi.FieldStorage()
db_name = "project.db"
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# Function to get the largest indent number
def get_largest_indent_number(cursor):
    cursor.execute("SELECT indentno FROM indenttable")
    indent_numbers = cursor.fetchall()
    largest_indent = max(indent_numbers, key=lambda x: int(re.search(r'IN-(\d+)-2024', x[0]).group(1)))
    return largest_indent[0]

# Fetch the largest indent number
largest_indent_number = get_largest_indent_number(cursor)

# Fetch the details of the indent with the largest indent number
cursor.execute("SELECT * FROM indenttable WHERE indentno=?", (largest_indent_number,))
indent_data = cursor.fetchall()

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
        <div class="logo-column"></div>
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
            <div class="ml-auto mt-4 md:mt-0"></div>
        </div>
    </header>
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
        <div class='dropdown-content'></div>
        <div class='ml-auto mt-4 md:mt-0'></div>
    </div>
</header>
""")

# Add some spacing between navbar and "Employee Details" heading
print("<div style='margin-top: 20px;'></div>")

# Display the details of the largest indent in an HTML table
print("<div style='text-align: center; margin-bottom: 25px;'>")
print("<p>INDENT FORM &nbsp;&nbsp;</p>")
print("</div>")
print("<div style='text-align: center; margin-bottom: -25px;'>")
print("<p>: &nbsp;&nbsp;</p>")
print("</div>")
print("<div style='text-align: left; margin-bottom: -25px;'>")
print(f"<p>INDENT NO: {largest_indent_number} &nbsp;&nbsp;</p>")
print("</div>")
print("<div style='text-align: right; margin-bottom: 30px;'>")
print("<p>&nbsp;&nbsp; DATE: 2024-06-10</p>")
print("</div>")
print("<div style='text-align: left; margin-bottom: 20px;'>")
print("<p>&nbsp;&nbsp;NAME OF THE DEPARTMENT: </p>")
print("</div>")

print("<div style='text-align: center;'>")
print("<table style='margin: 0 auto; border-collapse: collapse;'>")
print("<tr><th style='padding: 10px; border: 1px solid #ccc;'>S.No</th><th style='padding: 10px; border: 1px solid #ccc;'>Item Name</th><th style='padding: 10px; border: 1px solid #ccc;'>Supplier</th><th style='padding: 10px; border: 1px solid #ccc;'>Quantity</th><th style='padding: 10px; border: 1px solid #ccc;'>Amount</th><th style='padding: 10px; border: 1px solid #ccc;'>Remarks</th></tr>")

for i, row in enumerate(indent_data, start=1):
    print("<tr style='height: 50px;'>")
    print(f"<td style='padding: 10px; border: 1px solid #ccc;'>{i}</td>")
    for item in row[1:]:  # Skip the indent number column
        print(f"<td style='padding: 10px; border: 1px solid #ccc;'>{item}</td>")
    print("<td style='padding: 10px; border: 1px solid #ccc;'></td>")  # Add empty cell for Amount
    print("<td style='padding: 10px; border: 1px solid #ccc;'></td>")  # Add empty cell for Remarks
    print("</tr>")

# Add ten empty rows
for _ in range(6):
    print("<tr style='height: 50px;'>")
    for _ in range(6):  # 6 columns in total including empty cells for Amount and Remarks
        print("<td style='padding: 10px; border: 1px solid #ccc;'></td>")
    print("</tr>")

print("</table>")
print("</div>")

print("<div style='text-align: left; margin-bottom: 20px;'>")
print("<p>  &nbsp;&nbsp;</p>")
print("</div>")

print("<div style='text-align: left; margin-bottom: 20px;'>")
print("<p>Requested By: &nbsp;&nbsp;</p>")
print("</div>")

print("<div style='text-align: left; margin-bottom: -20px;'>")
print("<p>Principle:  &nbsp;&nbsp;</p>")
print("</div>")
print("<div style='text-align: right; margin-bottom: 20px;'>")
print("<p>Director:  &nbsp;&nbsp; </p>")
print("</div>")
