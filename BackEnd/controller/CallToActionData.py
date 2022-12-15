import json
from rest_framework.decorators import api_view
from django.http import HttpResponse
from dao.Database import ConnectDb
from model.CallToAction import CallToAction
import pyodbc
# from dao.Model import Products
import os

def ConnectDb(TableName):
    print(str(os.getcwd()))
    conn = pyodbc.connect(
        r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + str(os.getcwd()) + "\dao\DB.accdb;")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ' + str(TableName))
    json = cursor.fetchall()
    print(json)
    conn.close()
    return json


@api_view(['''GET'''])
def CallToActionData(request):
    rows = ConnectDb('''CallToAction''')
    for row in rows:
        data = CallToAction(row[1], row[2], row[3], row[4])
    return HttpResponse(json.dumps(data.__dict__), content_type='application/json')
