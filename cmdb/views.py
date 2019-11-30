from django.shortcuts import render
from decorator.decorator import auto_session

def index(request):
    return render(request, 'index.html')

@auto_session
def result(request):
    return render(request,'result.html')