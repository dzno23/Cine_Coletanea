from django.shortcuts import render
from .models import Item
from django.contrib.auth.models import User


def minha_coletanea(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            item = Item.objects.filter(user=request.user)
            return render(request, 'minha_coletanea.html', {'item': item})
    
    else:
        return render(request, 'logar.html')
