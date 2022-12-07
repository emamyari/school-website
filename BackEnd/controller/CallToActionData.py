import json
from rest_framework.decorators import api_view
from django.http import HttpResponse
from dao.Database import ConnectDb
from model.CallToAction import CallToAction


@api_view(['''GET'''])
def CallToActionData(request):
    rows = ConnectDb('''CallToAction''')
    li = []
    for row in rows:
        data = CallToAction(row[1], row[2], row[3], row[4])
        data = data.__dict__
        li.append(data)
    return HttpResponse(json.dumps(li), content_type='application/json')
