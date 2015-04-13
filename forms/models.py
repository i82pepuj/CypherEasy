from django.db import models
from django.contrib.auth.models import User

class ClaveMochila(models.Model):
    nombre = models.CharField(max_length=50)
    user = models.ForeignKey(User)
    w = models.PositiveIntegerField()
    m = models.PositiveIntegerField()
    mochila = models.CharField(max_length=250)
    publica = models.CharField(max_length=250)

    def __unicode__ (self):
	       return self.nombre

class ClaveRSA(models.Model):
    nombre = models.CharField(max_length=50)
    user = models.ForeignKey(User)
    n = models.PositiveIntegerField()
    e = models.PositiveIntegerField()
    d = models.PositiveIntegerField()

    def __unicode__ (self):
	       return self.nombre
