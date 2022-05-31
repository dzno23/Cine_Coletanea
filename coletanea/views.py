from django.shortcuts import render
from .models import Item
from django.contrib.auth.models import User


def minha_coletanea(request):
    if request.user.is_authenticated:
        if request.method == "GET":
       
            tipo = request.GET.get('tipo')
            rating = request.GET.get('rating')
            categoria = request.GET.get('categoria')
            
            if tipo or rating or categoria:
                if not tipo:
                    tipo = ''
                
                if not rating:
                    rating = 5
                
                if not categoria:
                    categoria = ''
                
                item = Item.objects.filter(user=request.user)\
                    .filter(tipo__in = tipo)\
                    .filter(categoria__in=categoria)\
                    .filter(rating__in = rating)
                
                return render(request, 'minha_coletanea.html', {'item': item})

            else:
                item = Item.objects.filter(user=request.user)
                return render(request, 'minha_coletanea.html', {'item': item})
    
    else:
        return render(request, 'logar.html')
