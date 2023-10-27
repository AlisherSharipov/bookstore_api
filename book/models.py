from django.db import models

class Book(models.Model):
	title = models.CharField(max_length = 250)
	subtitle = models.CharField(max_length=110)
	author = models.CharField(max_length=150)
	isbn = models.CharField(max_length=10)

	def __str__(self):
		return self.title