#Referenced from the following link to import flask:
#https://elearning.dbs.ie/mod/page/view.php?id=1445635
#https://flask.palletsprojects.com/en/2.3.x/quickstart

from flask import Flask, render_template, request, redirect
app = Flask(__name__)

#Reference ends to import flask:

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

#Idea from https://elearning.dbs.ie/mod/page/view.php?id=1445635
#And https://elearning.dbs.ie/mod/page/view.php?id=1445637 
#And https://medium.com/techcrush/how-to-render-html-file-in-flask-3fbfb16b47f6
@app.route("/report")#URL leading to method
def report(): # Name of the method
 SQL_QUERY = ("SELECT * FROM UserDetails;")     
 cursor.execute(SQL_QUERY)
 results = cursor.fetchall()
 return render_template('report.html',render_results=results)

@app.route("/")#URL leading to method
def index(): # Name of the method
 return render_template('index.html')

@app.route("/create",methods=['POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        number = request.form['number']
        SQL_QUERY = ("insert into UserDetails values (%s,%s)" %(name, number))
        cursor.execute(SQL_QUERY)
        conn.commit()
    return render_template('create.html')

#Referenced from the following link to run the app
#https://elearning.dbs.ie/mod/page/view.php?id=1445635
if __name__ == "__main__":
 app.run(host='0.0.0.0', port='8080') # indent this line

# Adding a comment to test change update to VM
