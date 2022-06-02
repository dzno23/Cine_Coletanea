from django.shortcuts import get_object_or_404, render
from .models import Item
from django.contrib.auth.models import User


def minha_coletanea(request):
    if request.user.is_authenticated:
        if request.method == "GET":
       
            tipo = request.GET.get('tipo')
            rating = request.GET.get('rating')
            categoria = request.GET.get('categoria')

            
            if not tipo and not rating and not categoria:
                item = Item.objects.filter(user=request.user)
                return render(request, 'minha_coletanea.html', {'item': item})
            
            elif tipo and not rating and not categoria:
                item = Item.objects.filter(user=request.user).filter(tipo = tipo)
                return render(request, 'minha_coletanea.html', {'item': item})

            elif rating and not tipo and not categoria:
                item = Item.objects.filter(user=request.user).filter(rating = rating)
                return render(request, 'minha_coletanea.html', {'item': item})

            elif categoria and not tipo and not rating:
                item = Item.objects.filter(user=request.user).filter(categoria = categoria)
                return render(request, 'minha_coletanea.html', {'item': item})

            elif tipo and rating and not categoria:
                item = Item.objects.filter(user=request.user).filter(tipo = tipo).filter(rating = rating)
                return render(request, 'minha_coletanea.html', {'item': item})

            elif tipo and categoria and not rating:
                item = Item.objects.filter(user = request.user).filter(tipo = tipo).filter(categoria = categoria)
                return render(request, 'minha_coletanea.html', {'item': item})

            elif rating and categoria and not tipo:
                item = Item.objects.filter(user=request.user).filter(rating = rating).filter(categoria = categoria)
                return render(request, 'minha_coletanea.html', {'item': item})

            elif tipo and rating and categoria:
                item = Item.objects.filter(user=request.user).filter(tipo = tipo).filter(rating = rating).filter(categoria = categoria)
                return render(request, 'minha_coletanea.html', {'item': item})
  
    else:
        return render(request, 'logar.html')


def item(request, id):
    if request.user.is_authenticated:
        if request.method == "GET":
            item = get_object_or_404(Item, id=id)
            return render(request, 'item.html', {'item': item})
   
    else:
        return render(request, '/auth/logar.html')