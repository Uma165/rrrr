from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'main/index.html', {'title': 'Главная'})

def about(request):
    return render(request,'main/about.html')