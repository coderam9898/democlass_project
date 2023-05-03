from django.urls import path
from . import views,viewstwo
urlpatterns = [
    path('', views.index, name='index'),
    path('index2/', viewstwo.indextwo, name='indextwo'),
    path('home/', views.home, name='home'),
    path('add', views.create, name='add'),
    # path('delete', views.delete, name='delete'),
    path('<int:id>/delete', views.delete, name='delete'),
    path('useradmin/',views.useradmin , name='useradmin'),
    path('newuser',views.newreg,name='newreg'),
    path('users',views.users,name='users')

   
]