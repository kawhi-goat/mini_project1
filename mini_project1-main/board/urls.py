from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('post/', views.post, name='post'),
    path('post/<int:id>', views.detail, name='detail')
]