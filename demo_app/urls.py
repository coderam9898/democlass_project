from django.urls import path
from . import views,viewstwo
urlpatterns = [
    path('', views.index, name='index'),
    path('index2/', viewstwo.indextwo, name='indextwo'),
    path('home/', views.home, name='home'),
    path('add/', views.create, name='add'),
    path('useradmin/',views.useradmin , name='useradmin')
   
]