from django.urls import path, include
from .views import CategoryViewset, ProductViewset
from rest_framework.routers import DefaultRouter

r  = DefaultRouter()

r.register(r"category", CategoryViewset, basename="category")
r.register(r"product", ProductViewset, basename="product")


urlpatterns = [
    path('', include(r.urls)),
]