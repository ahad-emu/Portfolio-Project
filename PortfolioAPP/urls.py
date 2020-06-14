from django.urls import path
from PortfolioAPP import views

urlpatterns = [
    path("", views.index, name="index"),
]
