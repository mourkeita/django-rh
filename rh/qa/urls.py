from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^texte', views.texte, name='texte'),
    url(r'^login', views.login, name='login'),
    url(r'^listUsers', views.listUsers, name='listUsers'),
    url(r'^new', views.newuser, name='newuser'),
    url(r'^userdetails', views.userdetails, name='userdetails'),
]
