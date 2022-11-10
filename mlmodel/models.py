from django.db import models


# Create your models here.

class Images(models.Model):
    name = models.CharField(max_length=80)
    image = models.CharField(max_length=100000)
    predict = models.CharField(max_length=80)

    def __str__(self):
        return self.name

