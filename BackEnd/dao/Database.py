import pyodbc
from dao.Model import Products
import os

def ConnectDB(TableName):
    conn = pyodbc.connect(
        r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + str(os.getcwd()) + "\DB.accdb;")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ' + str(TableName))
    json = cursor.fetchall()
    connection.close()
    return json
# import pyodbc
#
#
# def ConnectDb(TableName):
#     connection = pyodbc.connect(
#         'DRIVER={ODBC Driver 17 for SQL server};'
#         'SERVER=.;'
#         'DATABASE=school;'
#         'UID=sa;'
#         'PWD=111;')
#     cursor = connection.cursor()
#     cursor.execute('''SELECT * FROM ''' + str(TableName))
#     rows = cursor.fetchall()
#     connection.close()
#     return rows
