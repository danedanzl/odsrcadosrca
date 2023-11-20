from django.db import models

# Create your models here.

class Task(models.Model):
	name = models.CharField(max_length = 50)
	max_points = models.IntegerField()
	category = models.CharField(max_length=3, choices=[("nnz", "Nič ne znam"), ("obv", "obvladam")])

class Attempt(models.Model):
	date = models.DateField()
	points = models.IntegerField()
	task = models.ForeignKey(Task, on_delete=models.CASCADE)
	user = models.ForeignKey('konzola.User', on_delete=models.CASCADE)


