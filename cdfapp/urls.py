from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home),
	url(r'^noticias/$', views.news, name='news'),
	url(r'^contacto/$', views.contact, name='contact'),
	url(r'^galeria/fotos/$', views.photogallery, name='photogallery'),
	url(r'^galeria/videos/$', views.videogallery, name='videogallery'),
]
