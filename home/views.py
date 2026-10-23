from django.shortcuts import render
from .models import Amir

def home(request):
    amirs = Amir.objects.all()
    context = {
        'amirs': amirs,
        'name': 'amirali niko',
    }
    return render(request, 'home/landing.html', context=context)