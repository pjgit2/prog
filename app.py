#Referenced from the following link to import flask:
#https://elearning.dbs.ie/mod/page/view.php?id=1445635

from flask import Flask
app = Flask(__name__)

#Reference ends to import flask:

#Referenced from the following link to test Hello World on web app
#https://elearning.dbs.ie/mod/page/view.php?id=1445635

@app.route("/")#URL leading to method
def hello(): # Name of the method
 return("Hello World!") #indent this line

#Reference ends for Hello World testing

#Reference starts for setting pyodbc connection and running SQL:
# https://learn.microsoft.com/en-us/sql/connect/python/pyodbc/step-3-proof-of-concept-connecting-to-sql-using-pyodbc?view=sql-server-ver16

import pyodbc

server = 'pgmdbsrv.database.windows.net'
database = 'pgmdb'
username = 'addmin'
password = 'xxxxx'
driver = '{ODBC Driver 18 for SQL Server}'

conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

conn = pyodbc.connect(conn_str)

cursor = conn.cursor()

#Referenced from https://elearning.dbs.ie/mod/page/view.php?id=1445637 to test SQL query execution

SQL_QUERY = ("SELECT * FROM UserDetails;") 

#Referenced from https://elearning.dbs.ie/mod/page/view.php?id=1445637 ends
       
cursor.execute(SQL_QUERY)

#Reference ends for setting pyodbc connection and running SQL.

#Referenced from the following link to run the app
#https://elearning.dbs.ie/mod/page/view.php?id=1445635
if __name__ == "__main__":
 app.run(host='0.0.0.0', port='8080') # indent this line

# Adding a comment to test change update to VM
