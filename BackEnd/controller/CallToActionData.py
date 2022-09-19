import json
from rest_framework.decorators import api_view
from django.http import HttpResponse
from DAO.CallToAction import DAO


@api_view(['''GET'''])
def CallToActionData(request):
    data = DAO()
    return HttpResponse(json.dumps(data), content_type='application/json')
