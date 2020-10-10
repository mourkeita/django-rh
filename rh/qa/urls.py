from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static


from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login', views.login, name='login'),
    url(r'^index', views.index, name='index'),
    url(r'^users', views.users, name='users'),
    url(r'^newuser', views.newuser, name='newuser'),
   # url(r'^delete', views.delete, name='delete'),
    url(r'^userdetails', views.userdetails, name='userdetails'),
    url(r'^displayuser', views.displayuser, name='displayuser'),
    url(r'^update', views.update, name='update'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^welcome', views.welcome, name='welcome'),
    url(r'^articles', views.articles, name='articles'),
    url(r'^api/users', views.get_all, name='get_all'),
    url(r'^companies', views.companies, name='companies'),
    url(r'^display_company', views.display_company, name='display_company'),
    url(r'^delete_company', views.delete_company, name='delete_company'),
    url(r'^oauth/', include('social.apps.django_app.urls')),  # <--
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)