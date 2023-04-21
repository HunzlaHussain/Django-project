from django.shortcuts import render
from django.http import HttpResponse
from feature.models import login
from django.views.decorators.csrf import csrf_exempt
import os
# Create your views here.
def homepage(request):
    return render(request,"login.html")

@csrf_exempt
def saveform(request):
    if request.method == "POST":
        username = request.POST
        password = request.POST
        en=login(username=username, password=password)

        en.save()
    







