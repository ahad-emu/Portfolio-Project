from django.urls import path
from blogApp import views


urlpatterns = [
    path("", views.firstpage, name="firstpage"),
    path("pythonblog/", views.pythonblog, name="pythonblog"),
    path("djangoblog/", views.djangoblog, name="djangoblog"),
    path("python/<PythonBlog_python_title>", views.details_python, name="details_python"),
    path("django/<DjangoBlog_django_title>", views.details_django, name="details_django"),
]
