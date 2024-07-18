from django.db import models

class Label(models.Model):
    name = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=900)
    completion_status = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    labels = models.ManyToManyField(Label)
