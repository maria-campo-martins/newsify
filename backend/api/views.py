from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_data(request):
    data = {
        "message": "Hello from Django!"
    }
    return Response(data)

# Create your views here.
