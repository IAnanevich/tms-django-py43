from django.shortcuts import render


# Create your views here.

def read_post(request):
    return render(request, 'index.html')
