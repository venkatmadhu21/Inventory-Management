#!C:\Users\user\AppData\Local\Programs\Python\Python37\python.exe
import cgi
import sqlite3

# Enable CGI traceback for debugging
import cgitb
cgitb.enable()

# Connect to the SQLite database
db_name = "venkat2.db"  # Replace "your_database.db" with the name of your SQLite database file
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# Execute the SELECT query to fetch data from the issuevoucher table
cursor.execute("SELECT * FROM issuevoucher")
employees = cursor.fetchall()
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
				padding: 10px 30px;
				color: #ffffff;
				background-color: #870E03;
				position: relative;
				bottom: 0;
                margin-top: 200px;
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
            font-weight: 600;
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
             <a class="mr-5 hover:text-lightgray text-white" href="store.html">GO BACK</a>
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

# Adjusted header with buttons
print("<header class='text-gray-600 body-font navbar' style='justify-content: center;'>")  # Center the header
print("<div class='container mx-auto relative flex flex-wrap p-5 flex-col md:flex-row items-start'>")
print("<nav class='flex flex-wrap items-start text-base justify-center md:justify-start'>")
print("</nav>")
print("</div>")
print("</header>")

# Add some padding between "Employee Details" heading and the table
print("<div class='employee-details' style='text-align: left; padding-top: 10px; color: #800000;'>")  # Add padding between heading and table and change text color
print("<h1 style='color: #800000; font-size: 24px; font-weight: bold; text-align: left;'>Issue Voucher Details:-</h1>")
print("<div style='overflow-x:auto; padding-top: 20px;'>")  # Add padding to the table container
print("<table style='margin: auto; border: 1px solid #800000; font-size: 14px;'>")  # Add border to the table and reduce font size
print("<tr>")
print("<th class='nav__title'>depid</th>")
print("<th class='nav__title'>itemid</th>")
print("<th class='nav__title'>ivnumber</th>")
print("<th class='nav__title'>quantity</th>")
print("<th class='nav__title'>rvnumber </th>")
print("<th class='nav__title'>dateofissue</th>")
print("</tr>")
if employees:
    for employee in employees:
        print("<tr>")
        for field in employee:
            print("<td style='word-wrap: break-word; border: 1px solid #800000;'>{}</td>".format(field))  # Add border to each cell
        print("</tr>")
else:
    print("<tr><td colspan='14'>No employees found.</td></tr>")
print("</table>")
print("</div>")
print("</div>")

# Add the footer
print(footer_html)
