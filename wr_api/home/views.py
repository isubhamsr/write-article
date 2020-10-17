from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import sys

# Create your views here.
@csrf_exempt
def upload(request):
    if request.method == 'POST':
        try:
            return JsonResponse({'err':'false', 'message':'All Posts are Fetched'})
        except Exception as err:
            errMessage = f"Oops! {sys.exc_info()[1]}"
            return JsonResponse({'err':'true', 'message' : errMessage})
    else:
        return JsonResponse({'err':'true', 'message' : "HTTP Bad Request"})