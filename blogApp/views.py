from django.shortcuts import render
from .models import PythonBlog, DjangoBlog

# Create your views here.
def firstpage(request):
    return render(request, "firstpage.html")

def pythonblog(request):
    item = PythonBlog.objects.all()
    return render(request, "pythonblog.html", {'items': item})

def djangoblog(request):
    item = DjangoBlog.objects.all()
    return render(request, "djangoblog.html", {'items': item})


def details_python(request, PythonBlog_python_title):
    items = PythonBlog.objects.all()
    item = PythonBlog.objects.get(python_title = PythonBlog_python_title)
    return render(request, "pythondetails.html", {'item': item, 'items': items})

def details_django(request, DjangoBlog_django_title):
    items = DjangoBlog.objects.all()
    item = DjangoBlog.objects.get(django_title = DjangoBlog_django_title)
    return render(request, "djangodetails.html", {'item': item, 'items': items})
