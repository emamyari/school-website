import pyodbc
import os

def Connect():
    conn = pyodbc.connect(
        r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + str(os.getcwd()) + "\OnlineShop.accdb;")
    return conn.cursor()
# def Read(TableName):
#     cursor = Connect()
#     cursor.execute('SELECT * FROM ' + str(TableName))
#     rows = cursor.fetchall()
#     json = []
#     if str(TableName) == '''counters''':
#         for row in rows:
#             obj = Products(row[0], row[1], row[2], row[3])
#             json.append(obj)
#     return json
