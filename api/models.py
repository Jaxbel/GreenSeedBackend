from django.db import models

# Create your models here.

class Planta(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    ilumination = models.TextField()
    irrigation = models.TextField()
    irrigation_p1 = models.CharField(max_length=100)
    irrigation_p2 = models.CharField(max_length=100)
    irrigation_p3 = models.CharField(max_length=100)
    substratum = models.TextField()
    substratum_p1 = models.CharField(max_length=100)
    substratum_p2 = models.CharField(max_length=100)
    substratum_p3 = models.CharField(max_length=100)
    substratum_p4 = models.CharField(max_length=100)
    substratum_p5 = models.CharField(max_length=100)
    temperature = models.TextField()
    reproduction = models.TextField()
    reproduction_leaf = models.TextField()
    reproduction_sprout = models.TextField()
    reproduction_seeds = models.TextField()
    image = models.URLField(blank=True, null=True)

class PlantaData(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE, related_name='planta_data')