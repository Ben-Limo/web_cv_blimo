from django.db import models

# Create your models here.
class UserData(models.Model):
	name 			= models.CharField(max_length=120)
	company			= models.CharField(max_length=120)
	email			= models.EmailField(unique=True)
	comment			= models.TextField(max_length=250, null=True, blank=True)
	timestamp		= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

