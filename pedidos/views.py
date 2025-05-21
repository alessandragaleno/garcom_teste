# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def pedidos(request):
    return HttpResponse('ola pedidos')

