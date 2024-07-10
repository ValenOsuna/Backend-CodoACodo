from django.db import models

# Create your models here.

class Causa(models.Model):
    tittle = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="Causas/")
    