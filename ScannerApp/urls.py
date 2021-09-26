from django.conf.urls import url
from ScannerApp import views
from django.conf.urls.static import static

urlpatterns = [
  url(r'^reserva$', views.reservaApi),
  url(r'^reserva/([0-9]+)$', views.reservaApi),

  url(r'^trabajador$', views.trabajadorApi),
  url(r'^trabajador/([0-9]+)$', views.trabajadorApi)
  
]