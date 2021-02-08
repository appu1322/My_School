# Videos routing here

from django.urls import path
from tut11 import views

urlpatterns = [
    path('', views.tut11Home, name='tut11Home'),

    # physic tut and comment
    path('physic-<str:slug>/', views.physic, name='physic'),
    path('physicComment/', views.physicComment, name='/physicComment'),
    
    # chemistry tut and comment
    path('chemistry-<str:slug>/', views.chemistry, name='chemistry'),
    path('chemistryComment/', views.chemistryComment, name='chemistryComment'),

    # maths tut and comment
    path('math-<str:slug>/', views.math, name='math'),
    path('mathComment/', views.mathComment, name='mathComment'),


    #error
    # path('<str:slug>', views.errorfunc, name='errorfunc')
]
