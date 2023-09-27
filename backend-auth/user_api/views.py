from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# available routes for using this api
@api_view(['GET'])
def getRoutes(request):
    routes=[
        'api/token',
        'api/token/refresh',

    ]
    return Response(routes)
