from django.shortcuts import render

def index(request):
    return render(request, 'menu/index.html')

def menu(request):
    return render(request, 'menu/menu.html')

def reservation(request):
    return render(request, 'menu/reservation.html')

def reservation(request):
    return render(request, 'menu/team.html')

def reservation(request):
    return render(request, 'menu/special-dishes.html')

def reservation(request):
    return render(request, 'menu/about.html')
