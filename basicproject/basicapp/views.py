from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def welcome(request):
    x=['saki',4j,3,True]
    return render(request,'basicapp/basic.html',{'data':x})
