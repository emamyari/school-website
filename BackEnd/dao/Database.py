import pyodbc
from django.http import HttpResponse


def test(request):
    connection = pyodbc.connect(
        'DRIVER={ODBC Driver17 for SQL server};'
        'SERVER=185.83.183.254,11201;DATABASE=school;UID=sa;PWD=111')
    cursor = connection.cursor()
    cursor.execute("select * from ")

    rows=cursor.fetchall()
    connection.close()
    list=[]
    for item in rows:
        a=(item[0],item[1],item[2])
        list.append(a._dict_)
    return HttpResponse(json.dumps(list),content_type='application/json')
