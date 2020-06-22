from django.urls import path
from blogApp import views


urlpatterns = [
    path("", views.firstpage, name="firstpage"),
    path("item/", views.item, name="item"),
]
