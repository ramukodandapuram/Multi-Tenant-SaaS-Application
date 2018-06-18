from django.db import models

# Create your models here.


class Employees(models.Model):
	name=models.CharField(max_length=64)
	surnames = models.CharField(max_length=128)
	email=models.EmailField()
	phone_number=models.CharField(max_length=64)