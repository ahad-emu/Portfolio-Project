from django.shortcuts import render
from .models import Portfolio
# Create your views here.
def index(request):
    return render(request, "index.html",)

def portfolio(request):
    items = Portfolio.objects.all()
    return render(request, "portfolio.html" , {"items" : items})

def blog(request):
    return render(request, "blog.html" ,)
