from django.shortcuts import render
from .models import PythonBlog, DjangoBlog

# Create your views here.
def firstpage(request):
    return render(request, "firstpage.html")

def pythonblog(request):
    item = PythonBlog.objects.all()
    return render(request, "pythonblog.html", {'items': item})

def djangoblog(request):
    return render(request, "djangoblog.html")


def details_python(request, PythonBlog_python_title):
    item = PythonBlog.objects.get(python_title = PythonBlog_python_title)
    return render(request, "pythondetails.html", {'item': item})

def details_django(request, DjangoBlog_django_title):
    item = DjangoBlog.objects.get(django_title = DjangoBlog_django_title)
    return render(request, "djangodetails.html", {'item': item})
