# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import obra
from .models import historia
from django.contrib import admin

# Register your models here.

@admin.register(obra)
class Adminobra(admin.ModelAdmin):
	list_display = ('nombre','tipo','descripcion')
	list_filter = ('tipo',) 

@admin.register(historia)
class Adminhistoria(admin.ModelAdmin):
	list_display = ('nombre','descripcion')
	list_filter = ('id',)