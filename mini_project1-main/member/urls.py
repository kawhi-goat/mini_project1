from xml.etree.ElementInclude import include
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.signin, name='user_login'),
    path('signup/', views.signup, name='user_signup'),
] 