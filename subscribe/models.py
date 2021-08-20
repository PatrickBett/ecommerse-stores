from django.db import models

# Create your models here.
class Product(models.Model):
	product = models.CharField(max_length = 20)
	price = models.IntegerField()
	offer = models.BooleanField(default = False)
	image = models.ImageField(upload_to='images/' ,null = True, blank = True)
	available = models.BooleanField(default = False)
    


	def __str__(self):
		return self.product

#This absolute url has not done any effect to the project so far
	def get_absolute_url(self):
		return reverse('shop',args[str(self.id)])
