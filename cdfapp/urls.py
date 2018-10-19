from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home),
	url(r'^noticias/$', views.noticias, name='noticias'),
	url(r'^contacto/$', views.contacto, name='contacto'),
]
