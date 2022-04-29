from django.shortcuts import render

def minha_coletanea(request):
    if request.user.is_authenticated:
        return render(request, 'minha_coletanea.html')
    
    else:
        return render(request, 'logar.html')
