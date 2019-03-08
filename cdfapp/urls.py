from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home),
	url(r'^noticias/$', views.news, name='news'),
	url(r'^contacto/$', views.contact, name='contact'),
	url(r'^equipo/$', views.team, name='team'),
	url(r'^club/instalaciones/$', views.installations, name='installations'),
	url(r'^club/equipacion/$', views.equipement, name='equipement'),
	url(r'^equipo/miembros/$', views.members, name='members'),
	url(r'^equipo/miembro/$', views.member, name='member'),
	url(r'^galeria/fotos/$', views.photogallery, name='photogallery'),
	url(r'^galeria/videos/$', views.videogallery, name='videogallery'),
]
