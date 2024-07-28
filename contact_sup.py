    #!C:\Users\user\AppData\Local\Programs\Python\Python37\python.exe

    import cgi
    import cgitb
    import sqlite3

    # Enable traceback for debugging CGI scripts
    cgitb.enable()

    # Establish connection to SQLite database
    db_name = "venkat2.db"
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Function to get suppliers based on item name
    def get_suppliers(itemname):
        cursor.execute("SELECT supid FROM itemtable WHERE itemname=?", (itemname,))
        suppliers = cursor.fetchall()
        return suppliers

    # Generate HTML for dropdown menu with suppliers
    def generate_dropdown(suppliers):
        dropdown_html = "<select name='suppliers' id='suppliers' class='form-select'>"
        dropdown_html += "<option value=''>Select Supplier</option>"
        for supplier in suppliers:
            dropdown_html += "<option value='{}'>{}</option>".format(supplier[0], supplier[0])
        dropdown_html += "</select>"
        return dropdown_html

    # Generate HTML for dropdown menu with item names
    def generate_item_dropdown():
        cursor.execute("SELECT DISTINCT itemname FROM itemtable")
        items = cursor.fetchall()
        dropdown_html = "<select name='itemname' id='itemname' class='form-select'>"
        for item in items:
            dropdown_html += "<option value='{}'>{}</option>".format(item[0], item[0])
        dropdown_html += "</select>"
        return dropdown_html

    # Get form data
    form = cgi.FieldStorage()

    # Get selected values from form submission
    itemname = form.getvalue("itemname")
    supplier = form.getvalue("suppliers")
    quantity = form.getvalue("quantity")

    # Initialize variable to track insertion status
    insertion_status = ""

    # Insert values into indent table
    if form.getvalue("action") == "insert" and itemname and supplier and quantity:
        cursor.execute("INSERT INTO indent (itemname, supplier, quantity) VALUES (?, ?, ?)", (itemname, supplier, quantity))
        conn.commit()
        insertion_status = "Values inserted into indent table: {} {} {}".format(itemname, supplier, quantity)

    # Generate HTML response
    print("Content-type: text/html\n")

    print("""
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
        <script src="https://cdn.tailwindcss.com"></script>
        <style>
            body {{
                font-family: 'Poppins', sans-serif;
                margin: 0;
                display: flex;
                flex-direction: column;
                min-height: 100vh;
            }}

            .header-container {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 10px;
                background-color: #f8f8f8;
                border-bottom: 2px solid #cc0000;
                text-align: center;
                position: fixed;
                width: 100%;
                top: 0;
                z-index: 1000;
            }}

            .logo {{
                width: 100px;
                height: 100px;
                border-radius: 50%;
                object-fit: cover;
            }}

            .logo-column {{
                flex: 2;
                text-align: left;
            }}

            .header-container .text-column {{
                flex: 1;
            }}

            .header-container h1,
            .header-container h2,
            .header-container p {{
                margin: 0;
            }}

            .header-container h1 {{
                color: #cc0000;
                font-size: 1.5rem;
                margin-bottom: 5px;
            }}

            .header-container p {{
                color: #333;
                font-size: 1rem;
            }}

            .navbar {{
                background-color: maroon;
                color: white;
                padding-top: 120px;
            }}

            .navbar a {{
                color: white;
            }}

            .navbar a:hover {{
                color: lightgray;
            }}

            .content {{
                display: flex;
                justify-content: center;
                align-items: center;
                flex-direction: column;
                margin-top: 50px;
                font-size: 1.2rem;
            }}

            .form-label {{
                font-size: 1.2rem;
                margin: 10px 0;
            }}

            .form-select, .form-input {{
                font-size: 1.2rem;
                padding: 10px;
                margin: 10px 0;
                width: 300px;
            }}

            .form-button {{
                background-color: #800000;
                color: white;
                font-size: 1.0rem;
                padding: 10px 20px;
                border: none;
                cursor: pointer;
                margin: 10px 0;
            }}

            .form-button:hover {{
                background-color: #a00000;
            }}

            .footer {{
                display: flex;
                justify-content: space-between;
                align-items: flex-start;
                padding: 0px 30px;
                color: #ffffff;
                background-color: #870E03;
                position: absolute;
                bottom: 0;
                width: 100%;
                font-family: 'Poppins', sans-serif;
                flex-wrap: wrap;
            }}

            .footer__section {{
                flex: 1;
            }}

            .footer__addr {{
                margin-top: 0.4em;
                font-size: 15px;
                font-weight: 400;
            }}

            .footer__logo {{
                font-family: 'Poppins', sans-serif;
                font-weight: 400;
                text-transform: uppercase;
                font-size: 1.5rem;
            }}

            .footer__addr h2 {{
                margin-top: 0.4em;
                font-size: 15px;
                font-weight: 400;
            }}

            .nav__title {{
                margin-top: 0.4em;
                font-size: 15px;
                font-weight: 400;
                margin-left: auto;
            }}

            .footer address {{
                margin-top: 0.4em;
                font-style: normal;
                color: white;
            }}

            .footer__btn {{
                display: flex;
                align-items: center;
                justify-content: center;
                height: 36px;
                max-width: max-content;
                background-color: rgba(33, 33, 33, 0.07);
                border-radius: 100px;
                color: white;
                line-height: 0;
                margin: 0.6em 0;
                font-size: 1rem;
                padding: 0 1.3em;
            }}

            .footer ul {{
                list-style: none;
                padding-left: 0;
            }}

            .footer li {{
                line-height: 30px;
            }}

            .footer a {{
                text-decoration: none;
            }}

            .footer__nav {{
                display: flex;
                justify-content: space-between;
                flex-wrap: wrap;
                align-items: flex-start;
                width: 100%;
            }}

            .nav__ul a {{
                color: white;
            }}

            @media screen and (min-width: 24.375em) {{
                .legal .legal__links {{
                    margin-left: auto;
                }}
            }}

            @media screen and (min-width: 40.375em) {{
                .footer__nav {{
                    flex: 2 0px;
                }}

                .footer__addr {{
                    flex: 1 0px;
                }}
            }}

        </style>

        <title>Item Details</title>
    </head>

    <body>
        <header class="header-container">
            <img src="images/logo.png" class="logo">
            <div class="text-column">
                <h1 class="text-4xl font-semibold main-heading">Keshav Memorial College Of Engineering</h1>
                <p class="text-lg font-medium sub-heading mt-2">A unit of Keshav Memorial Technical Educational Society (KMTES)</p>
                <p>Approved by AICTE, New Delhi - Affiliated to Jawaharlal Nehru Technological University, Hyderabad</p>
            </div>
        </header>

        <header class="text-gray-600 body-font navbar" role="navigation">
            <div class="container mx-auto relative flex flex-wrap p-5 flex-col md:flex-row items-center">
                <a href="index.html" class="flex title-font font-medium items-center mb-4 md:mb-0"></a>
                <nav class="md:ml-auto md:mr-auto flex flex-wrap items-center text-base justify-center">
                    <a class="mr-5 hover:text-lightgray" href="index.html">HOME</a>
                    <a class="mr-5 hover:text-lightgray" href="about.html">ABOUT US</a>
                    <a class="mr-5 hover:text-lightgray" href="indent.py">GENERATE AN INDENT</a>
                    <a class="mr-5 hover:text-lightgray" href="rv.py">GENERATE AN RV</a>
                    <a class="mr-5 hover:text-lightgray" href="iv.py">GENERATE AN IV</a>
                </nav>
            </div>
        </header>

        <div class="content">
            <div id='formDiv'>
                <form id='supplierForm' method='post'>
                    <label class='form-label' for='itemname'>Select Item name:</label>
                    {item_dropdown}
                    <br>
                    <label class='form-label' for='quantity'>Quantity:</label>
                    <input type='text' id='quantity' name='quantity' class='form-input'>
                    <input type='hidden' name='action' value='display_suppliers'>
                    <button type='submit' class='form-button'>Display Suppliers</button>
                </form>
            </div>
        </div>
    """.format(item_dropdown=generate_item_dropdown()))

    if itemname and form.getvalue("action") == "display_suppliers":
        suppliers = get_suppliers(itemname)
        print("""
            <div id='supplierTable'>
                <form method='post'>
                    <label class='form-label' for='suppliers'>Select Supplier:</label>
                    {supplier_dropdown}
                    <br>
                    <input type='hidden' name='itemname' value='{itemname}'>
                    <input type='hidden' name='quantity' value='{quantity}'>
                    <input type='hidden' name='action' value='insert'>
                    <button type='submit' class='form-button'>Submit</button>
                </form>
            </div>
        """.format(supplier_dropdown=generate_dropdown(suppliers), itemname=itemname, quantity=quantity))

    print("<div id='selectedOptions'></div>")

    if insertion_status:
        print("<p>{}</p>".format(insertion_status))
        print("<button class='form-button' style='width: 10%; margin: 0 auto;' onclick=\"redirectToPrint()\">OK</button>")

    print("""
        <script>
        function redirectToPrint() {
            window.location.href = 'print_indent.py';
        }
        </script>
        <footer class="footer">
            <div class="footer_section footer_addr">
                <h2>Contact</h2>
                <address>Office : 8499981497<br></address>
            </div>
            <div class="footer__section">
                <h2 class="nav__title">Email id:</h2>
                <ul class="nav__ul">
                    <li><a href="mailto:admin@kmce.in">admin@kmce.in</a></li>
                </ul>
            </div>
            <div class="footer__section">
                <h2 class="nav__title">Landline:</h2>
                <ul class="nav__ul">
                    <li><a href="tel:040-xxxx-123">040-xxxx-123</a></li>
                </ul>
            </div>
            <div class="footer__section">
                <h2 class="nav__title">Address:</h2>
                <ul class="nav__ul">
                    <li><a href="#">Koheda Road, Ibrahimpatnam</a></li>
                </ul>
            </div>
        </footer>
    </body>
    </html>
    """)
