from django.shortcuts import render
from django.http import HttpResponse
import newrelic.agent

def home(request):
    return render(request, 'index.html')

def ping(request):
    newrelic.agent.ignore_transaction()
    return HttpResponse("pong")
