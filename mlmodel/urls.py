from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('upload/', views.uploadImage, name="submit"),
    path('results/', views.showResults, name="results"),
    path('paint/', views.paint, name="paint")
]