from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from home.models import Document
from home.forms import DocumentForm
import json
import sys

# Create your views here.
@csrf_exempt
def upload(request):
    if request.method == 'POST':
        try:
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                print(form)
                return JsonResponse({'err':'true', 'message' : 'Upload Successful'})
        except Exception as err:
            errMessage = f"Oops! {sys.exc_info()[1]}"
            return JsonResponse({'err':'true', 'message' : errMessage})
    else:
        return JsonResponse({'err':'true', 'message' : "HTTP Bad Request"})