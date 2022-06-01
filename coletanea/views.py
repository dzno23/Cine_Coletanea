from django.shortcuts import render
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
                item = Item.objects.filter(user=request.user).filter(tipo__in = tipo)
                return render(request, 'minha_coletanea.html', {'item': item})

            elif rating and not tipo and not categoria:
                item = Item.objects.filter(user=request.user).filter(rating__in = rating)
                return render(request, 'minha_coletanea.html', {'item': item})

            elif categoria and not tipo and not rating:
                item = Item.objects.filter(user=request.user).filter(categoria__in = categoria)
                return render(request, 'minha_coletanea.html', {'item': item})

            elif tipo and rating and not categoria:
                item = Item.objects.filter(user=request.user).filter(tipo__in = tipo).filter(rating__in = rating)
                return render(request, 'minha_coletanea.html', {'item': item})

            elif tipo and categoria and not rating:
                item = Item.objects.filter(user = request.user).filter(tipo__in = tipo).filter(categoria__in = categoria)
                return render(request, 'minha_coletanea.html', {'item': item})

            elif rating and categoria and not tipo:
                item = Item.objects.filter(user=request.user).filter(rating__in = rating).filter(categoria__in = categoria)
                return render(request, 'minha_coletanea.html', {'item': item})



            # if tipo or rating or categoria:
            #     if not tipo:
            #         tipo = ''
                
            #     if not rating:
            #         rating = ''
                
            #     if not categoria:
            #         categoria = ''
                
            #     item = Item.objects.filter(user=request.user)\
            #         .filter(tipo__in = tipo)\
            #         .filter(categoria__in=categoria)\
            #         .filter(rating__in = rating)
                
            #     return render(request, 'minha_coletanea.html', {'item': item})

            # else:
            #     item = Item.objects.filter(user=request.user)
            #     return render(request, 'minha_coletanea.html', {'item': item})
    
    else:
        return render(request, 'logar.html')


# def item(request):
#     if request.user.is_authenticated:
#         if request.method == "POST":

#             id = request.POST.get('id')
#             item = Item.objects.filter(id=id)

#             return render(request, 'item.html', {'item': item})
    

#     else:
#         return render(request, '/auth/logar.html')