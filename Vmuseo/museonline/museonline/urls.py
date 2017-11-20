from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from pagina.views import inicio

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('pagina.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
