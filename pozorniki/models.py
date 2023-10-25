from django.db import models


# Create your models here.
class Pozorniki(models.Model):
    name = models.CharField(max_length=256)
    ochki_pozora = models.BigIntegerField()