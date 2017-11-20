	# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.template import loader
from .models import historia
from .models import obra
from .form import ObraForm
# Create your views here.

def inicio(request):
	obraa = obra.objects.order_by('id')
	template = loader.get_template('inicio.html')
	context = {
	'obraa': obraa
	}
	return HttpResponse(template.render(context,request))

def cuadro(request):
	obraa = obra.objects.order_by('id')
	template = loader.get_template('cuadro.html')
	context = {
	'obraa': obraa
	}
	return HttpResponse(template.render(context,request))


def escultura(request):
	obraa = obra.objects.order_by('id')
	template = loader.get_template('escultura.html')
	context = {
	'obraa': obraa
	}
	return HttpResponse(template.render(context,request))

def obra_detail(request, pk):
	obraa = get_object_or_404(obra, pk =pk )
	template = loader.get_template('detail.html')
	context= {
	'obraa': obraa
	}
	return HttpResponse(template.render(context, request))
	
def new_obra(request):
	if request.method == 'POST':
		form = ObraForm(request.POST, request.FILES)
		if form.is_valid():
			obra = form.save(commit=False)
			obra.save()
			return HttpResponseRedirect('/')
	else:
		form = ObraForm()
		template = loader.get_template('new_obra.html')
		context = {
		'form': form 
		}
		return HttpResponse(template.render(context,request))

def history(request):
	historiaa = historia.objects.order_by('id')
	template = loader.get_template('historia.html')
	context = {
	'historiaa': historiaa
	}
	return HttpResponse(template.render(context, request))

def juego(request):
	
	template = loader.get_template('index.html')
	contex = {
	
	}
	return HttpResponse(template.render(contex, request))

	