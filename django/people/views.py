# Core Django imports
from django.shortcuts import render


def about(request):
    context = {'bodymessage': "About this project"}
    return render(request, 'people/about.html', context)