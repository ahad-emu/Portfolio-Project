from django.urls import path
from PortfolioAPP import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("portfolio/", views.portfolio, name="portfolio"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
