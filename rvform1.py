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
            <a class="mr-5 hover:text-lightgray text-white" href="inventory.html">GO BACK</a>
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

def generate_supplier_dropdown():
    cursor.execute("SELECT DISTINCT supid FROM itemtable")
    suppliers = cursor.fetchall()
    dropdown_html = "<select name='supid' id='supid' style='border: 1px solid #800000; padding: 5px; display: inline-block;'>"
    dropdown_html += "<option value='' selected disabled>Select Supplier</option>"  # Set default option
    for supplier in suppliers:
        dropdown_html += "<option value='{}'>{}</option>".format(supplier[0], supplier[0])
    dropdown_html += "</select>"
    return dropdown_html

def generate_item_dropdown():
    cursor.execute("SELECT DISTINCT itemname FROM itemtable")
    items = cursor.fetchall()
    dropdown_html = "<select name='itemname' id='itemname' onchange='displaySuppliers()' style='border: 1px solid #800000; padding: 5px; display: inline-block;'>"
    dropdown_html += "<option value='' selected disabled>Select Item</option>"  # Set default option
    for item in items:
        dropdown_html += "<option value='{}'>{}</option>".format(item[0], item[0])
    dropdown_html += "</select>"
    return dropdown_html

def generate_quantity_input():
    return "<input type='text' id='quantity' name='quantity' style='border: 1px solid #800000; padding: 5px;' placeholder='Enter Quantity'>"

def generate_amount_input():
    return "<input type='text' id='amount' name='amount' style='border: 1px solid #800000; padding: 5px;' placeholder='Enter Amount'>"

def generate_payment_date_input():
    return "<input type='date' id='paymentDate' name='paymentDate' style='border: 1px solid #800000; padding: 5px;'>"

def generate_mode_of_payment_dropdown():
    modes = ["Cash", "Credit Card", "Debit Card", "Net Banking"]
    dropdown_html = "<select name='modeOfPayment' id='modeOfPayment' style='border: 1px solid #800000; padding: 5px; display: inline-block;'>"
    dropdown_html += "<option value='' selected disabled>Select Mode of Payment</option>"  # Set default option
    for mode in modes:
        dropdown_html += "<option value='{}'>{}</option>".format(mode, mode)
    dropdown_html += "</select>"
    return dropdown_html

def generate_supplier_input():
    return "<input type='text' id='supid' name='supid' style='border: 1px solid #800000; padding: 5px;' placeholder='Enter Supplier ID'>"

def generate_receipt_number_input():
    return "<input type='text' id='receiptnumber' name='receiptnumber' style='border: 1px solid #800000; padding: 5px;' placeholder='Enter Receipt Number'>"

def generate_receipt_date_input():
    return "<input type='date' id='receiptdate' name='receiptdate' style='border: 1px solid #800000; padding: 5px;'>"

def generate_order_date_input():
    return "<input type='date' id='orderdate' name='orderdate' style='border: 1px solid #800000; padding: 5px;'>"

def generate_arrival_date_input():
    return "<input type='date' id='arrivaldate' name='arrivaldate' style='border: 1px solid #800000; padding: 5px;'>"

# Add the heading for RV Details
print("<div style='text-align: center;'>")
print("<h2 style='color: red;'>RV Details</h2>")
print("</div>")


# Add form container with center alignment
print("<div style='text-align: center; display: flex; justify-content: center;'>")

# Print the form elements
print("<form id='rvDetailsForm' method='post' style='display: flex; justify-content: center;'>")

# Print the first 5 inputs
print("<div style='margin-right: 50px;'>")
print("<label for='itemname' style='color: red;'>Select Item name:</label><br>")
print(generate_item_dropdown())
print("<br>")

print("<label for='quantity' style='color: red;'>Quantity:</label><br>")
print(generate_quantity_input())
print("<br>")

print("<label for='amount' style='color: red;'>Amount:</label><br>")
print(generate_amount_input())
print("<br>")

print("<label for='paymentDate' style='color: red;'>Payment Date:</label><br>")
print(generate_payment_date_input())
print("<br>")

print("<label for='modeOfPayment' style='color: red;'>Mode of Payment:</label><br>")
print(generate_mode_of_payment_dropdown())
print("</div>")

# Print the next 5 inputs
print("<div>")
print("<label for='supid' style='color: red;'>Select Supplier ID:</label><br>")
print(generate_supplier_dropdown())
print("<br>")

print("<label for='receiptnumber' style='color: red;'>Receipt Number:</label><br>")
print(generate_receipt_number_input())
print("<br>")

print("<label for='receiptdate' style='color: red;'>Receipt Date:</label><br>")
print(generate_receipt_date_input())
print("<br>")

print("<label for='orderdate' style='color: red;'>Order Date:</label><br>")
print(generate_order_date_input())
print("<br>")

print("<label for='arrivaldate' style='color: red;'>Arrival Date:</label><br>")
print(generate_arrival_date_input())
print("<br>")
print("</div>")



# Close form
print("</form>")

# Close form container
print("</div>")
print("""
    <div style='text-align: center; padding: 20px;'>
        <form method='post' action='rvprint.py'>
            <button type='submit' name='action' value='Search' style='padding: 5px 10px; background-color: #800000; color: white; border: none; cursor: pointer;'>Submit</button>
        </form>
    </div>
    """)



if form.getvalue("itemname"):
    itemname = form.getvalue("itemname")
    quantity = form.getvalue("quantity")
    amount = form.getvalue("amount")
    payment_date = form.getvalue("paymentDate")
    mode_of_payment = form.getvalue("modeOfPayment")
    supid = form.getvalue("supid")
    receiptnumber = form.getvalue("receiptnumber")
    receiptdate = form.getvalue("receiptdate")
    orderdate = form.getvalue("orderdate")
    arrivaldate = form.getvalue("arrivaldate")

    cursor.execute("SELECT rvnumber FROM rvtable ORDER BY rvnumber DESC LIMIT 1")
    last_rv_number = cursor.fetchone()

    # If there are existing RV numbers
    if last_rv_number:
        last_rv_number = last_rv_number[0]
        # Extract the last three digits from the RV number
        last_digits = int(last_rv_number.split("-")[1])
        # Increment the last three digits by 1
        new_digits = last_digits + 1
        # Format the new RV number
        new_rv_number = "RV-{0:03d}-2024".format(new_digits)
    else:
        # If there are no existing RV numbers, start from RV-001-2024
        new_rv_number = "RV-001-2024"

    # Insert the form data into the rvtable table
    try:
        cursor.execute("""
            INSERT INTO rvtable (rvnumber, itemid, quantitybought, supid, amount, modeofpayment, receiptnumber, receiptdate, orderdate, arrivaldate)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (new_rv_number, itemname, quantity, supid, amount, mode_of_payment, receiptnumber, receiptdate, orderdate, arrivaldate))
        conn.commit()
        print("Data inserted successfully.")
    except sqlite3.Error as e:
        print("Error inserting data:", e)

   
    # Redirect to rvprint.py using JavaScript after inserting data
    redirect_script = """
    <script>
    window.location.replace("rvprint.py");
    </script>
    """
    print(redirect_script)

# Print the footer HTML
print(footer_html)

# Close the database connection
conn.close()