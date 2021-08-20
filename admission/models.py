from django.db import models

# Create your models here.
class Student(models.Model):
	firstname = models.CharField(max_length=40)
	lastname = models.CharField(max_length=40)
	email = models.CharField(max_length=40)
	contacts = models.IntegerField()
	school = models.CharField(max_length=30)
	course = models.CharField(max_length=30)
	studentphoto = models.ImageField(upload_to = 'static')
	result_slip = models.ImageField(upload_to = 'static')
	birthcertificate = models.ImageField(upload_to = 'static')


	def __str__(self):
		return self.firstname
