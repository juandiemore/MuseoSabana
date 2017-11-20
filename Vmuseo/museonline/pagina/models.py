# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class obra(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length = 255)
    rectores = 'rectores'
    hace30 = 'hace30'
    cancilleres = 'cancilleres'
    arte = 'arte'
    objetos = 'objetos'
    emblemas = 'emblemas'
    promotores = 'promotores'
    flora = 'flora'
    fauna = 'fauna'
    TIPO = ((rectores , 'rectores'),
    (hace30 ,'hace30'),
    (cancilleres, 'cancilleres'),
    (arte, 'arte'),
    (objetos ,'objetos'),
    (emblemas ,'emblemas'),
    (promotores, 'promotores'),
    (flora, 'flora'),
    (fauna, 'fauna'),)
    tipo = models.CharField(max_length=255,choices=TIPO,
    default= rectores,)
    image = models.ImageField(blank=True)

    def __str__(self):
		return self.nombre
		class Meta:
			ordering = ('id',)

class historia(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    image = models.ImageField(blank= True)
    image2 = models.ImageField(blank = True)

 