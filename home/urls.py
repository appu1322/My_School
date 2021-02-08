# home routing here

from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('handlelogin/', views.handleLogin, name='handlelogin'),
    path('handlelogout/', views.handleLogout, name='handleLogout'),
]
