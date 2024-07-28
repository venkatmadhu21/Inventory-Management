import os
import cgi
import cgitb
import sqlite3

cgitb.enable()
form = cgi.FieldStorage()
db_name = "kmce1.db"
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

# Add some spacing between navbar and "Sort Details" heading
print("<div style='margin-top: 20px;'></div>")

# Form to input sorting field for employee details
print("<div style='text-align: center; padding: 20px;'>")
print("<h2>Sort Employee Details</h2>")
print("<form method='post'>")
print("<select name='sort_field'>")
emp_fields = ["EmpId", "Fname", "Mname", "Lname", "DesignationId", "Graduation", "PostGraduation", "Phd", "JoiningDate", "PhoneNo", "DateofLeaving", "DepId", "EmailId", "Area", "Locality", "UnitNo", "PinCode"]
for field in emp_fields:
    print(f"<option value='{field}'>{field}</option>")
print("</select>")
print("<input type='hidden' name='action' value='SortEmp'>")
print("<input type='submit' value='Sort'>")
print("</form>")
print("</div>")

# Form to input sorting field for department details
print("<div style='text-align: center; padding: 20px;'>")
print("<h2>Sort Department Details</h2>")
print("<form method='post'>")
print("<select name='sort_field'>")
dep_fields = ["DepName", "DepId"]
for field in dep_fields:
    print(f"<option value='{field}'>{field}</option>")
print("</select>")
print("<input type='hidden' name='action' value='SortDep'>")
print("<input type='submit' value='Sort'>")
print("</form>")
print("</div>")

# Form to input sorting field for supplier details
print("<div style='text-align: center; padding: 20px;'>")
print("<h2>Sort Supplier Details</h2>")
print("<form method='post'>")
print("<select name='sort_field'>")
supplier_fields = ["SupId", "Sname", "Area", "Locality", "PinCode", "emailId", "PhoneNo1", "PhoneNo2", "PhoneNo3", "Blacklisted"]
for field in supplier_fields:
    print(f"<option value='{field}'>{field}</option>")
print("</select>")
print("<input type='hidden' name='action' value='SortSupplier'>")
print("<input type='submit' value='Sort'>")
print("</form>")
print("</div>")

# Handle form submission and sorting logic
if "action" in form:
    sort_field = form.getvalue('sort_field')
    if form["action"].value == "SortEmp":
        cursor.execute(f"SELECT * FROM empdetails ORDER BY {sort_field}")
        rows = cursor.fetchall()
        # Print employee details table
        print("<h2>Sorted Employee Details</h2>")
        print("<table border='1' style='margin: auto;'>")
        print("<tr><th>EmpId</th><th>Fname</th><th>Mname</th><th>Lname</th><th>DesignationId</th><th>Graduation</th><th>PostGraduation</th><th>Phd</th><th>JoiningDate</th><th>PhoneNo</th><th>DateofLeaving</th><th>DepId</th><th>EmailId</th><th>Area</th><th>Locality</th><th>UnitNo</th><th>PinCode</th></tr>")
        for row in rows:
            print("<tr>")
            for cell in row:
                print(f"<td>{cell}</td>")
            print("</tr>")
        print("</table>")
    elif form["action"].value == "SortDep":
        cursor.execute(f"SELECT * FROM department ORDER BY {sort_field}")
        rows = cursor.fetchall()
        # Print department details table
        print("<h2>Sorted Department Details</h2>")
        print("<table border='1' style='margin: auto;'>")
        print("<tr><th>DepName</th><th>DepId</th></tr>")
        for row in rows:
            print("<tr>")
            for cell in row:
                print(f"<td>{cell}</td>")
            print("</tr>")
        print("</table>")
    elif form["action"].value == "SortSupplier":
        cursor.execute(f"SELECT * FROM Suppliers ORDER BY {sort_field}")
        rows = cursor.fetchall()
        # Print supplier details table
        print("<h2>Sorted Supplier Details</h2>")
        print("<table border='1' style='margin: auto;'>")
        print("<tr><th>SupId</th><th>Sname</th><th>Area</th><th>Locality</th><th>PinCode</th><th>emailId</th><th>PhoneNo1</th><th>PhoneNo2</th><th>PhoneNo3</th><th>Blacklisted</th></tr>")
        for row in rows:
            print("<tr>")
            for cell in row:
                print(f"<td>{cell}</td>")
            print("</tr>")
        print("</table>")

print(footer_html)

conn.close()