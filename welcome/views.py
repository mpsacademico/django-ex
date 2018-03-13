import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from . import database
from .models import PageView

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['general']
sensor = db['sensor']

# Create your views here.

def index(request):
    hostname = os.getenv('HOSTNAME', 'unknown')
   

    return render(request, 'welcome/index.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': 1
    })

def health(request):
    return HttpResponse(1)

def show(request):
	text = ""
	page = sensor.find({})
	for p in page:
		text = text + "<br>" + str(p)
	return HttpResponse(text)

def mongo(request):
    data = {"serialnumber": request.GET.get('serialnumber'), "key": request.GET.get('key'), "data": request.GET.get('data')}
    teste = sensor.insert_one(data).inserted_id
    return HttpResponse(teste)