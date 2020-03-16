from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'page/home.html')
def event(request):
    return render(request, 'page/event.html')    
def training(request):
    return render(request, 'page/training.html')    