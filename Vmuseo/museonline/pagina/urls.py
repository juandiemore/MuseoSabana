from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.inicio),
	url(r'^cuadros',views.cuadro, name='cuadros'),
	url(r'^esculturas',views.escultura, name='escul'),
	url(r'^obra/(?P<pk>[0-9]+)$',views.obra_detail, name='obra_detail'),
	url(r'^product/new', views.new_obra, name='new_obra'),
	url(r'^historia', views.history, name = 'history'),
	url(r'^juego', views.juego , name="juego"),
		
]