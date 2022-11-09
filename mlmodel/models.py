from django.db import models


# Create your models here.

class Images(models.Model):
    name = models.CharField(max_length=20)
    image = models.CharField(max_length=40000)
    predict = models.CharField(max_length=20)

    def __str__(self):
        return self.name

