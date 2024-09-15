from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .scraper import scrape
import json

@csrf_exempt
def scrape_view(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        maxArticles = data.get('maxArticles', 15)
        result = scrape(maxArticles)
        return JsonResponse(result, safe=False)
    return JsonResponse({'error': 'Invalid request'}, status=400)


