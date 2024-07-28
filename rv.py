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
    dropdown_html = "<select name='suppliers' id='suppliers'>"
    dropdown_html += "<option value=''>Select Supplier</option>"
    for supplier in suppliers:
        dropdown_html += "<option value='{}'>{}</option>".format(supplier[0], supplier[0])
    dropdown_html += "</select>"
    return dropdown_html

# Generate HTML for dropdown menu with item names
def generate_item_dropdown():
    cursor.execute("SELECT DISTINCT itemname FROM itemtable")
    items = cursor.fetchall()
    dropdown_html = "<select name='itemname' id='itemname'>"
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
if itemname:
    cursor.execute("INSERT INTO indent (itemname, supplier, quantity) VALUES (?, ?, ?)", (itemname, supplier, quantity))
    conn.commit()
    insertion_status = "Values inserted into indent table: {} {} {}".format(itemname, supplier, quantity)

# Generate HTML response
print("Content-type: text/html\n")

print("<h1>Item Details</h1>")
print("<div id='formDiv'>")
print("<form id='supplierForm' method='post'>")
print("<label for='itemname'>Select Item name:</label>")
print(generate_item_dropdown())
print("<br>")
print("<label for='quantity'>Quantity:</label>")
print("<input type='text' id='quantity' name='quantity'>")
print("<button type='submit'>Display Suppliers</button>")  # Changed type to submit
print("</form>")
print("</div>")
print("<div id='supplierTable'>")
if itemname:
    suppliers = get_suppliers(itemname)
    print("<label for='suppliers'>Select Supplier:</label>")
    print(generate_dropdown(suppliers))
    print("<br>")
    print("<button class='mr-5 hover:text-lightgray' onclick='redirectToPrint()'>Submit</button>")

    print("<br>")
    #print("<button type='submit'>Submit</button>")  # Changed type to submit
else:
    print("<p>No suppliers found for the selected item.</p>")
    print("<br>")
    print("<a class='mr-5 hover:text-lightgray' href='about.html'>submit</a>")
   # print("<label for='quantity'>Quantity:</label>")
   #   print("<input type='text' id='quantity' name='quantity'>")
    print("<br>")
print("</div>")

print("<div id='selectedOptions'></div>")

# Print insertion status message
if insertion_status:
    print("<p>{}</p>".format(insertion_status))


print("<script>")
print("function submitForm() {")
print("    redirectToPrint();")  # Redirect to print.py
print("    return false;")  # Prevent default form submission
print("}")
print("function displaySelected() {")
print("    var itemname = document.getElementById('itemname').value;")
print("    var supplier = document.getElementById('suppliers').value;")
#print("    var quantity = document.getElementById('quantity').value;")
print("    var selectedDiv = document.getElementById('selectedOptions');")
print("    var tableHtml = '<table border=\"1\" style=\"margin: auto;\"><tr><th>Item</th><th>Supplier</th><th>Quantity</th></tr>';")
print("    tableHtml += '<tr><td>' + itemname + '</td><td>' + supplier + '</td><td>' + quantity + '</td></tr></table>';")
print("    selectedDiv.innerHTML = tableHtml;")
print("    selectedDiv.innerHTML += '<button onclick=\"hideAllAndCenterTable()\">OK</button>';")  # Add OK button
print("}")
print("function hideAllAndCenterTable() {")
print("    document.getElementById('formDiv').style.display = 'none';")  # Hide formDiv
print("    document.getElementById('supplierTable').style.display = 'none';")  # Hide supplierTable
print("    var selectedDiv = document.getElementById('selectedOptions');")
print("    selectedDiv.style.textAlign = 'center';")  # Center the content
print("    selectedDiv.style.marginTop = '50px';")  # Add some top margin for better appearance
print("    selectedDiv.style.display = 'block';")  # Ensure the selected options are displayed
print("    selectedDiv.style.visibility = 'visible';")  # Ensure the selected options are visible
print("}")
print("function redirectToPrint() {")
print("    window.location.href = 'rvprint.py';")  # Redirect to print.py
print("}")
print("</script>")

