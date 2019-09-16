from django.shortcuts import render
from django.http import HttpResponse
import datetime

def home(request):
    now = datetime.datetime.now()
    html = '<html><title>DateTime</title><body>Agora é %s.</body></html>' % now
    return HttpResponse(html)