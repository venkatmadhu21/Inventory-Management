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
             <a class="mr-5 hover:text-lightgray text-white" href="indeventoryman.html">GO BACK</a>
            <div class='dropdown'>
                
                <div class='dropdown-content'>
                </div>
            </div>
        </nav>
        <div class='ml-auto mt-4 md:mt-0'>
          
                </svg>
            </button>
        </div>
    </div>
</header>
""")

# Add some spacing between navbar and "Supplier Details" heading
print("<div style='margin-top: 20px;'></div>")

# Function to delete supplier details

# Fetch item names
cursor.execute("SELECT itemname FROM itemtable")
items = cursor.fetchall()

print("<div style='text-align: center; padding: 20px;'>")
print("<form method='post' action=''>")  # Change method to 'post'
print("<label for='itemname' style='color: #800000; font-weight: bold;'>Select item Name:</label>")
print("<select id='itemname' name='itemname' style='margin-left: 10px; padding: 5px; border: 1px solid #800000;'>")
# Add empty option for "Select"
print("<option value='' selected disabled>Select</option>")
for (itemname,) in items:
    print(f"<option value='{itemname}'>{itemname}</option>")
print("</select>")
print("<div style='display: flex; justify-content: center; margin-top: 10px;'>")
print("<button type='submit' name='action' value='OK' class='footer__btn bg-red-700 hover:bg-red-800 text-white font-bold py-2 px-4 rounded'>OK</button>")
print("</div>")
print("</form>")
print("</div>")

# Process form submission
if "action" in form and form["action"].value == "OK":
    if "itemname" in form:
        itemname = form["itemname"].value
        # Fetch item ID first
        cursor.execute("SELECT itemid FROM itemtable WHERE itemname=?", (itemname,))
        item_id = cursor.fetchone()  # Assuming you want to fetch one item ID
        
        if item_id:
            item_id = item_id[0]  # Extract the actual item ID
            query = """
            SELECT SUM(requirement.quantity) FROM requirement
            JOIN itemtable ON requirement.itemid = itemtable.itemid
            WHERE requirement.reqmet = 0 and requirement.itemid = ?
            GROUP BY requirement.itemid
            """
            
            
            # Fetch quantity bought from rvtable table for the item ID
            cursor.execute("SELECT SUM(quantitybought) FROM rvtable WHERE itemid=?", (item_id,))
            quantity_bought = cursor.fetchone()
            
            if quantity_bought:
                cursor.execute(query, (item_id,))
                sumreq = cursor.fetchone()
                sumreq_value = sumreq[0] if sumreq else 0
                
                # Fetch total issue quantity from ivtable table for the item ID
                cursor.execute("SELECT SUM(issuequantity) FROM ivtable WHERE itemid=?", (item_id,))
                total_issue_quantity = cursor.fetchone()
                total_issue_quantity_value = total_issue_quantity[0] if total_issue_quantity[0] is not None else 0
                quantity_bought_value = quantity_bought[0]
                # Calculate quantity available
                quantity_available = quantity_bought_value - total_issue_quantity_value
                if quantity_available >= 0:
                    # Print the quantity available below the message
                    print("<div style='text-align: center;'>")
                    print(f"<p>Quantity Available: {quantity_available}</p>")
                    print(f"<p>Quantity Required: {sumreq_value}</p>")
                    print("</div>")

                    # Add buttons for issue voucher and generate indent form
                    print("<div style='text-align: center; margin-top: 20px;'>")
                    print("<div style='display: inline-block; margin-right: 20px;'>")  # Container for buttons
                    print("<form action='ivform.py'>")
                    print("<button type='submit' class='footer__btn bg-red-700 hover:bg-red-800 text-white font-bold py-2 px-4 rounded'>Go to Issue Voucher</button>")
                    print("</form>")
                    print("</div>")
                    print("<div style='display: inline-block;'>")  # Container for buttons
                    print("<form action='indent.py'>")
                    print("<button type='submit' class='footer__btn bg-red-700 hover:bg-red-800 text-white font-bold py-2 px-4 rounded'>Generate Indent Form</button>")
                    print("</form>")
                    print("</div>")
                    print("</div>")
                else:
                    print("<p>Quantity Available: 0</p>")
            else:
                print("<div style='text-align: center;'>")
                print("<p>Item ID not found in rvtable.</p>")
                print("</div>")
        else:
            print("<div style='text-align: center;'>")
            print("<p>No matching item found.</p>")
            print("</div>")
    else:
        print("<div style='text-align: center;'>")
        print("<p>No Item name provided.</p>")
        print("</div>")
else:
    print("<div style='text-align: center;'>")
    print("<p>Click the 'OK' button to display the quantity available.</p>")
    print("</div>")

# Add the footer
print(footer_html)
