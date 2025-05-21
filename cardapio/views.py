from django.shortcuts import render

# Create your views here.

def cardapio(request):
    return render(request, 'index.html')

