from django.shortcuts import render
from django.http import HttpResponse
from .models import classification,runtut,tutorial
from django.core import serializers
# Create your views here.
def hello(request):
    return HttpResponse('Welcome!')

def fenlei(request):
    data = classification.objects.all()
    return HttpResponse(serializers.serialize('json',data))

def tut(request):
    fenlei = request.GET['fenlei']
    data = tutorial.objects.filter(classification=fenlei).order_by('createtime')
    return HttpResponse(serializers.serialize('json',data))
