from django.db import models

# Create your models here.

class Environment(models.Model):
    name = models.CharField()
    description = models.TextField()

class Model(models.Model):
    name = models.CharField()
    description = models.TextField()
    file_name = models.TextField()

class LegoPiece(models.Model):
    name = models.CharField()
    description = models.TextField()
    size_x = models.IntegerField()
    size_y = models.IntegerField()
    size_z = models.IntegerField()