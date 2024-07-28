#!C:\Users\akshi\AppData\Local\Programs\Python\Python312\python.exe
import os
import cgi
import cgitb
import sqlite3
from datetime import datetime

cgitb.enable()
print("Content-type: text/html\n\n")
print("<html><body style='text-align:center;'>")
print("<h1 style='color: #800000;'>LOGIN PAGE</h1>")
form = cgi.FieldStorage()
db_name = "project.db"
name = ""
pwd = ""

if os.environ['REQUEST_METHOD'].upper() == 'POST':
    if form.getvalue("username"):
        name = form.getvalue("username")
    if form.getvalue("password"):
        pwd = form.getvalue("password")

    if name and pwd:  # Check if username and password are not empty
        def connect_to_db(db_name):
            try:
                con = sqlite3.connect(db_name)
                return con
            except sqlite3.Error as error:
                print("<p>Error while connecting to SQLite: " + str(error) + "</p>")
                return None

        con = connect_to_db(db_name)

        if con:
            try:
                cur = con.cursor()
                sql_select = "SELECT designation, empid FROM signup WHERE username = ? AND password = ?"
                cur.execute(sql_select, (name, pwd))
                rec = cur.fetchone()
                if rec:
                    designation = rec[0]
                    empid = rec[1]  # Assuming the empid is in the second column
                    logintime = datetime.now().strftime('%H:%M:%S')
                    logdate = datetime.now().strftime('%d-%b-%Y').lower()

                    # Debugging print statements
                    print(f"<p>Designation: {designation}</p>")
                    print(f"<p>EmpID: {empid}</p>")
                    print(f"<p>Login Time: {logintime}</p>")
                    print(f"<p>Login Date: {logdate}</p>")

                    sql_insert = "INSERT INTO login (empid, logintime, logdate) VALUES (?, ?, ?)"
                    cur.execute(sql_insert, (empid, logintime, logdate))
                    con.commit()

                    if designation == 'hod':
                        print('<meta http-equiv="refresh" content="0;url=hod.html" />')
                    elif designation == 'admin':
                        print('<meta http-equiv="refresh" content="0;url=inventory.html" />')
                    elif designation == 'storekeeper':
                        print('<meta http-equiv="refresh" content="0;url=store.html" />')    
                    elif designation == 'director':
                        print('<meta http-equiv="refresh" content="0;url=director.html" />')
                    elif designation == 'inventory':
                        print('<meta http-equiv="refresh" content="0;url=indeventoryman.html" />')
                    else:
                        print("<script>alert('Designation not recognized.'); window.location.href = 'login_form.html';</script>")
                else:
                    print("<script>alert('Login failed. Please try again.'); window.location.href = 'login_form.html';</script>")
            except sqlite3.Error as error:
                print(f"<p>Error while executing SQL query: {error}</p>")
            finally:
                con.close()
        else:
            print("<p>Failed to connect to the database</p>")
    else:
        print("<script>alert('Username and password cannot be empty.'); window.location.href = 'login_form.html';</script>")

print("</body></html>")
