import numpy as numpy

from dao.Database import ConnectDb
from model.Services import ServicesData
import pyodbc
# from dao.Model import Products
import os

def ConnectDb(TableName):
    print(str(os.getcwd()))
    conn = pyodbc.connect(
        r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + str(os.getcwd()) + "\dao\mmd.accdb;")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ' + str(TableName))
    json = cursor.fetchall()
    print(json)
    conn.close()
    return json
def ConnectDb2(TableName):
    print(str(os.getcwd()))
    conn = pyodbc.connect(
        r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + str(os.getcwd()) + "\dao\mmd.accdb;")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ' + str(TableName))
    json = cursor.fetchall()
    print(json)
    conn.close()
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


def Services():
    rows = ConnectDb('''ServicesData''')
    li = []
    for row in rows:
        rowDetails = ConnectDb2('''previewImages''')


        a = ServicesData(row[0],row[1], row[2], row[3])
        li.append(a.__dict__)
    return li
