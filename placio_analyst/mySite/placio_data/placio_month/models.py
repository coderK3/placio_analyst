from django.db import models

# Create your models here.

class csvimport(models.Model):
	description = models.CharField(max_length=255, blank=True)
	file = models.FileField(upload_to='documents/%Y-%m-%d/')
	uploaded_at = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.description

class graph_axis(models.Model):
	x_axis = models.CharField(max_length=200)
	hue = models.CharField(max_length=200)
