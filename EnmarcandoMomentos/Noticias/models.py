from django.db import models

# Create your models here.

class Noticia(models.Model):
    Title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    sector = models.CharField(max_length=50)

    def __str__(self):
        return self.Title
    