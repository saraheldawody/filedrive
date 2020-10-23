from django.urls import path
from . import  views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('register/', views.register, name='register'),
    path('signout/', views.signout, name='signout'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('files/', views.files, name='files'),
    path('done/', views.regdone, name='done'),
    path('upload/', views.upload, name='upload'),
    path('profile/', views.profile, name='profile'),
    

]