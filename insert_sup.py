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
            justify-content: center; /* Center the header */
            align-items: center;
            padding: 10px;
            width: 100%;
            top: 0;
            z-index: 1000;
            text-align: center;
            background-color: #f8f8f8;
            border-bottom: 2px solid: #800000;
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
            font-weight: 600; /* Bold */
            font-size: 15px;
            color: red; /* Red color for field names */
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
print("Content-type: text/html\n")
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
          
                </svg>
            </button>
        </div>
    </div>
</header>
""")

# Add some spacing between navbar and "Employee Details" heading
print("<div style='margin-top: 20px;'></div>")

# Function to insert employee details
# Function to insert supplier details
def insert_supplier(supid, sname, area, locality, pincode, emailid, phoneno1, phoneno2, phoneno3,blacklisted ):
    try:
        cursor.execute("INSERT INTO suppliers (supid, sname, area, locality, pincode, emailid, phoneno1, phoneno2, phoneno3, blacklisted) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                       (supid, sname, area, locality, pincode, emailid, phoneno1, phoneno2, phoneno3, 0))
        conn.commit()
        print("<p>Supplier details inserted successfully.</p>")
    except Exception as e:
        print("<p>Error inserting supplier details: {}</p>".format(str(e)))

# Form to input supplier details for insertion
print("<div style='text-align: center; padding: 20px;'>")
print("<form method='post' action=''>")
print("<div style='display: flex; justify-content: space-between;'>")  # Start of two-column layout
print("<div style='flex: 1;'>")  # Left column
print("<label for='supid' style='color: #800000; font-weight: bold;'>Supplier ID:</label>")
print("<input type='text' id='supid' name='supid' style='margin-left: 10px; padding: 5px; border: 1px solid #800000;'><br>")
print("<label for='sname' style='color: #800000; font-weight: bold;'>Supplier Name:</label>")
print("<input type='text' id='sname' name='sname' style='margin-left: 10px; padding: 5px; border: 1px solid #800000;'><br>")
print("<label for='area' style='color: #800000; font-weight: bold;'>Area:</label>")
print("<input type='text' id='area' name='area' style='margin-left: 10px; padding: 5px; border: 1px solid #800000;'><br>")
print("<label for='locality' style='color: #800000; font-weight: bold;'>Locality:</label>")
print("<input type='text' id='locality' name='locality' style='margin-left: 10px; padding: 5px; border: 1px solid #800000;'><br>")
print("<label for='pincode' style='color: #800000; font-weight: bold;'>Pincode:</label>")
print("<input type='text' id='pincode' name='pincode' style='margin-left: 10px; padding: 5px; border: 1px solid #800000;'><br>")
print("<label for='emailid' style='color: #800000; font-weight: bold;'>Email ID:</label>")
print("<input type='text' id='emailid' name='emailid' style='margin-left: 10px; padding: 5px; border: 1px solid #800000;'><br>")
print("</div>")  # End of left column
print("<div style='flex: 1;'>")  # Right column
print("<label for='phoneno1' style='color: #800000; font-weight: bold;'>Phone Number 1:</label>")
print("<input type='text' id='phoneno1' name='phoneno1' style='margin-left: 10px; padding: 5px; border: 1px solid #800000;'><br>")
print("<label for='phoneno2' style='color: #800000; font-weight: bold;'>Phone Number 2:</label>")
print("<input type='text' id='phoneno2' name='phoneno2' style='margin-left: 10px; padding: 5px; border: 1px solid #800000;'><br>")
print("<label for='phoneno3' style='color: #800000; font-weight: bold;'>Phone Number 3:</label>")
print("<input type='text' id='phoneno3' name='phoneno3' style='margin-left: 10px; padding: 5px; border: 1px solid #800000;'><br>")
print("</div>")  # End of right column
print("</div>")  # End of two-column layout
#print("<button type='submit' style='padding: 5px 10px; background-color: white; color: white; border: none; cursor: pointer; margin-top: 10px;'>Submit</button>")
print("<button type='submit' name='action' value='Insert' style='padding: 5px 10px; background-color: #800000; color: white; border: none; cursor: pointer;'>Insert</button>")
print("</form>")
print("</div>")

# Process form submission for inserting suppliers
if "action" in form and form["action"].value == "Insert":
    if all(key in form for key in ['supid', 'sname', 'area', 'locality', 'pincode', 'emailid', 'phoneno1', 'phoneno2', 'phoneno3' ]):
        supid = form["supid"].value
        sname = form["sname"].value
        area = form["area"].value
        locality = form["locality"].value
        pincode = form["pincode"].value
        emailid = form["emailid"].value
        phoneno1 = form["phoneno1"].value
        phoneno2 = form["phoneno2"].value
        phoneno3 = form["phoneno3"].value
        
        insert_supplier(supid, sname, area, locality, pincode, emailid, phoneno1, phoneno2, phoneno3,0)
    else:
        print("<p>All fields are required for insertion.</p>")




# Add the footer
#print(footer_html)

# Add the footer
print(footer_html)