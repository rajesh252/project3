from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def func_1(request):
    return HttpResponse('this is firtst funtion')