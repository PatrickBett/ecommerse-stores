from django.db import models


# Create your models here.
class user(models.Model):
	firstname=models.CharField(max_length=30)
	lastname=models.CharField(max_length=30)
	username=models.CharField(max_length=30)
	email=models.CharField(max_length=30)
	password1=models.CharField(max_length=30)
	password2=models.CharField(max_length=30)

	def __str__(self):
		return self.firstname