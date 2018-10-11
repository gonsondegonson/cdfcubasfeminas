from django.db import models
from django.utils import timezone


class Noticias(models.Model):
	titulo				= models.CharField(max_length=200)
	resumen				= models.CharField(max_length=400)
	texto				= models.TextField()
	preferente			= models.BooleanField(default=False)
	author				= models.ForeignKey('auth.User', on_delete=models.PROTECT)
	fecha_creacion		= models.DateTimeField(default=timezone.now)
	fecha_publicacion	= models.DateTimeField(blank=True, null=True)

	def publicar(self):
		self.fecha_publicacion = timezone.now()
		self.save()

	def __str__(self):
		return self.titulo

class Contactos(models.Model):
	telefono			= models.CharField(max_length=20)
	email				= models.CharField(max_length=100)
	mensaje				= models.TextField()
	fecha_peticion		= models.DateTimeField(default=timezone.now)
	fecha_respuesta		= models.DateTimeField(blank=True, null=True)

	def respondido(self):
		self.fecha_respuesta = timezone.now()
		self.save()

	def __str__(self):
		return self.mensaje
		
class Equipos(models.Model):
	nombre			    = models.CharField(max_length=50)

	def __str__(self):
		return self.nombre
		
