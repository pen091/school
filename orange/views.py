from django.shortcuts import render

# Create your views here.

def orangehome(request):
    return render(request, 'orange/home.html')
