#References:
#https://elearning.dbs.ie/mod/page/view.php?id=1445635
#https://flask.palletsprojects.com/en/2.3.x/quickstart
#https://flask-login.readthedocs.io/en/latest/

from flask import Flask, render_template, request, redirect
from flask_login import LoginManager

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

#https://learn.microsoft.com/en-us/sql/connect/python/pyodbc/step-3-proof-of-concept-connecting-to-sql-using-pyodbc?view=sql-server-ver16

import pyodbc
server = 'pgmdbsrv.database.windows.net'
database = 'pgmdb'
username = 'addmin'
password = 'xxxxx'
driver = '{ODBC Driver 18 for SQL Server}'

conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

#Idea taken from https://elearning.dbs.ie/mod/page/view.php?id=1445635
#And https://elearning.dbs.ie/mod/page/view.php?id=1445637 
#And https://medium.com/techcrush/how-to-render-html-file-in-flask-3fbfb16b47f6
@app.route("/report")#URL leading to method
def report(): # Name of the method
 SQL_QUERY = ("SELECT * FROM UserDetails;")     
 cursor.execute(SQL_QUERY)
 results = cursor.fetchall()
 return render_template('report.html',render_results=results)

@app.route("/")
def index(): 
 return render_template('index.html')

#Idea taken from https://www.educative.io/answers/how-to-add-data-to-databases-in-flask
#And https://stackoverflow.com/questions/43491381/pyodbc-the-sql-contains-0-parameter-markers-but-1-parameters-were-supplied-hy0
@app.route("/create",methods=['GET','POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        number = request.form['number']
        cursor.execute("insert into UserDetails values (?,?)", (name, number))
        conn.commit()
    return render_template('create.html')

@app.route("/delete",methods=['GET','POST'])
def delete():
    if request.method == 'POST':
        id = request.form['identity']
        cursor.execute("delete from UserDetails where id = ?", (id))
        conn.commit()
    return render_template('delete.html')

@app.route("/update",methods=['GET','POST'])
def update():
    if request.method == 'POST':
        id = request.form['identity']
        number = request.form['number']
        cursor.execute("update UserDetails set PhoneNumber = ? where id = ?", (number,id))
        conn.commit()
    return render_template('update.html')

#Reference:
#https://elearning.dbs.ie/mod/page/view.php?id=1445635
if __name__ == "__main__":
 app.run(host='0.0.0.0', port='8080') # indent this line


