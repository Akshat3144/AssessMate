from django.db import models


# Create your models here.

class Features(models.Model):
    details = models.CharField(max_length=350)

class UploadedFile(models.Model):
    name = models.CharField(max_length=50)
    file = models.FileField()


