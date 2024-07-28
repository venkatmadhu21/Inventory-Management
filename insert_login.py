#!C:\Users\user\AppData\Local\Programs\Python\Python37\python.exe
import os
import cgi
import cgitb
import sqlite3
from datetime import datetime

cgitb.enable()  # Enable detailed error reporting

# Send an HTTP header indicating the content type as HTML
print("Content-type: text/html\n\n")

# Start an HTML document with center-aligned content
print("<html><body style='text-align:center;'>")

# Display a heading with text "LOGIN PAGE"
print("<h1 style='color: m ;'>LOGIN PAGE</h1>")

# Parse form data submitted via the CGI script
form = cgi.FieldStorage()

# Initialize variables
name = ""
pwd = ""

# Check if the request method is POST
if os.environ['REQUEST_METHOD'].upper() == 'POST':
    # Check if the "username" and "password" fields are present in the form data
    if form.getvalue("username"):
        name = form.getvalue("username")
    
    if form.getvalue("password"):
        pwd = form.getvalue("password")

    # Connect to the database
    def connect_to_db(db_name):
        try:
            con = sqlite3.connect(db_name)
            return con
        except sqlite3.Error as error:
            print("<p>Error while connecting to SQLite: " + str(error) + "</p>")
            return None

    # Database connection and user authentication
    db_name = "project.db"
    con = connect_to_db(db_name)

    if con:
        try:
            cur = con.cursor()
            # Use parameterized query to prevent SQL injection
            sql_select = "SELECT * FROM signup WHERE username = ? AND password = ?"
            cur.execute(sql_select, (name, pwd))
            rec = cur.fetchone()
            
            if rec:  # If a matching record is found
                empid = rec[0]  # Assuming the employee ID is in the first column
                logintime = datetime.now().strftime('%H:%M:%S')
                logdate = datetime.now().strftime('%Y-%m-%d')

                sql_insert = "INSERT INTO loginout (empid, logintime, logdate) VALUES (?, ?, ?)"
                cur.execute(sql_insert, (empid, logintime, logdate))
                con.commit()

                print('<meta http-equiv="refresh" content="0;url=inventory.html" />')
            else:  # If no matching record is found
                print("<script>alert('Login failed. Please try again.'); window.location.href = 'hello_form[1].html';</script>")
        except sqlite3.Error as error:
            print("<p>Error while executing SQL query: " + str(error) + "</p>")
        finally:
            con.close()
    else:
        print("<p>Failed to connect to the database</p>")
        

print("</body></html>")