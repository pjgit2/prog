
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

#Reference ends for setting pyodbc connection and running SQL:
