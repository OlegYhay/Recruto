from django.shortcuts import render


def mainview(request):
    return render(request, 'main.html')
