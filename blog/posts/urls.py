from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('<int:id>/', views.post),
    path('google/', views.google),
]