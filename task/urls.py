from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('add/', add, name='add'),
    path('search/<str:name>/', search, name='search'),
    path('search//', home, name='search_empty'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('detail/<int:id>/', detail, name='detail'),
]