from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    # path('<int:id>/', views.post, name='post'),
    # path('search/', views.search, name='search'),
    path('', views.HomeView.as_view(), name='home'),
    path('<int:pk>/', views.PostView.as_view(), name='post'),
    path('tags/<int:id>/', views.tags, name='tag'),
    path('search/', views.SearchView.as_view(), name='search'),
]