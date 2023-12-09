#Referenced from the following link to import flask:
#https://elearning.dbs.ie/mod/page/view.php?id=1445635

from flask import Flask
app = Flask(__name__)

#Reference ends to import flask:

#Reference starts for setting pyodbc connection and running SQL:
# https://learn.microsoft.com/en-us/sql/connect/python/pyodbc/step-3-proof-of-concept-connecting-to-sql-using-pyodbc?view=sql-server-ver16

import pyodbc

server = 'pgmdbsrv.database.windows.net'
database = 'pgmdb'
username = 'addmin'
password = 'Login123'
driver = '{ODBC Driver 18 for SQL Server}'

conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

conn = pyodbc.connect(conn_str)

cursor = conn.cursor()
cursor.execute(SQL_QUERY)

#Reference ends for setting pyodbc connection and running SQL.

#Referenced from the following link to run the app
#https://elearning.dbs.ie/mod/page/view.php?id=1445635
if __name__ == "__main__":
 app.run(host='0.0.0.0', port='8080') # indent this line
