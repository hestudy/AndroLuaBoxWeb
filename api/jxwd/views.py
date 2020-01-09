from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import jxwd_fenlei,jxwd_context
# Create your views here.
def fenlei(request):
    data = jxwd_fenlei.objects.all()
    json = serializers.serialize('json',data)
    return HttpResponse(json)

def context(request):
    fl = request.GET['fenlei']
    data = jxwd_context.objects.filter(fenlei=fl)
    json = serializers.serialize('json',data)
    return HttpResponse(json)