
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.home, name="home"),
    path('reglamento', views.reglamento, name="reglamento"),
    path('precios', views.precios, name="precios"),
    path('fotos', views.fotos, name="fotos"),
    path('comollegar', views.comollegar, name="comollegar"),
    path('preguntasfrecuentes', views.preguntasfrecuentes, name="preguntasfrecuentes"),
] 

urlpatterns += staticfiles_urlpatterns()