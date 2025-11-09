from django.shortcuts import render

# Create your views here.

def bananahome(request):
    return render(request, 'banana/home.html')
