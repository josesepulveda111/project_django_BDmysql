"""
URL configuration for DJcompany project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from DJcompany.views import home,insertarartista,listadoartista,listadoartistasactivos,listadoartistasinactivos,activarartistas,desactivarartistas,actualizarartistas,insertartour,listadotour,actualizartour,listadotourcan, listadotourcur,completartour,cancelartour,encursotour,insertaralbum,albumsdestacados,albumsnodestacados,destacaralbum,nodestacaralbum,actualizaralbum

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('artistas/insertar',insertarartista),
    path('artistas/listado',listadoartista),
    path('artistas/listadoi',listadoartistasinactivos),
    path('artistas/desactivar/<int:idartistas>',desactivarartistas),
    path('artistas/activar/<int:idartistas>',activarartistas),
    path('artistas/actualizar/<int:idartistas>',actualizarartistas),
    path('albums/insertar',insertaralbum),
    path('albums/listado',albumsdestacados),
    path('albums/listadoi',albumsnodestacados),
    path('albums/destacar/<int:idalbum>',destacaralbum),
    path('albums/nodestacar/<int:idalbum>',nodestacaralbum),
    path('albums/actualizar/<int:idalbum>',actualizaralbum),
    path('tours/insertar',insertartour),
    path('tours/listado',listadotour),
    path('tours/listadocan',listadotourcan),
    path('tours/listadocur',listadotourcur),
    path('tours/actualizar/<int:id>',actualizartour),
    path('tours/completar/<int:idtour>',completartour),
    path('tours/cancelar/<int:idtour>',cancelartour),
    path('tours/encurso/<int:idtour>',encursotour),
]
