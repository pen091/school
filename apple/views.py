from django.shortcuts import render

# Create your views here.

def applehome(request):
    return render(request, 'apple/home.html')
