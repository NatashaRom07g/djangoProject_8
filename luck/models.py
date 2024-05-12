from django.db import models

# Create your models here.
class ModelRomanova(models.Model):
    name = models.TextField()
    password = models.TextField()
