from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^texte', views.texte, name='texte'),
    url(r'^login', views.login, name='login'),
    url(r'^listUsers', views.listUsers, name='listUsers'),
    url(r'^newuser', views.newuser, name='newuser'),
    url(r'^delete', views.delete, name='delete'),
    url(r'^userdetails', views.userdetails, name='userdetails'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^welcome', views.welcome, name='welcome'),
    url(r'^delete', views.delete, name='delete'),
    url(r'^api', views.api, name='api'),
]