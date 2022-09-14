import json
from django.http import HttpResponse
from rest_framework.decorators import api_view
from djangoProject2.dao.GetDatas import getFunFactData





def FUNFACT(request):
    listt=getFunFactData()

    return HttpResponse(json.dumps(listt), content_type="application/json")





# def Funfact(request):
#     connection = pyodbc.connect(
#         'DRIVER={ODBC Driver 17 for SQL Server};'
#         'SERVER=185.83.183.254,11201;DATABASE=school;UID=sa;PWD=111@a')
#     cursor = connection.cursor()
#     cursor.execute("select * from FunFacts")
#
#     rows=cursor.fetchall()
#     connection.close()
#     list=[]
#     for item in rows:
#         a=(item[0],item[1],item[2])
#         list.append(a)
#     return HttpResponse(json.dumps(list), content_type='application/json')



