from django.db import connection
from django.shortcuts import render, redirect
from DJcompany.models import Albums, Artistas, Tours
from django.core.files.storage import FileSystemStorage


def home(request):
    return render(request,"home/home.html")


#region artistas

def insertarartista(request):
    if request.method=="POST":
        if request.POST.get("nombre") and request.POST.get("edad") and request.POST.get("nacionalidad") and request.POST.get("celular") and request.POST.get("correo") and request.POST.get("premios") and request.POST.get("fecha_firma") and request.FILES["foto"] and request.POST.get("genero_musical"):
            artistas = Artistas()
            artistas.nombre =request.POST.get("nombre")
            artistas.edad =request.POST.get("edad")
            artistas.nacionalidad =request.POST.get("nacionalidad")
            artistas.celular =request.POST.get("celular")
            artistas.correo =request.POST.get("correo")
            artistas.premios =request.POST.get("premios")
            artistas.fecha_firma =request.POST.get("fecha_firma")
            artistas.foto =request.FILES["foto"]
            artistas.genero_musical =request.POST.get("genero_musical")
            imagen = FileSystemStorage()
            imagen.save(artistas.foto.name,artistas.foto)
            insertar = connection.cursor()
            insertar.execute("call insertarartista('"+artistas.nombre+"','"+artistas.edad+"','"+artistas.nacionalidad+"','"+artistas.celular+"','"+artistas.correo+"','"+artistas.premios+"','"+artistas.fecha_firma+"','"+artistas.foto.name+"','"+artistas.genero_musical+"')")
            return redirect("/artistas/listado")
    else: 
        return render(request,"artistas/insertar.html")
    
def listadoartista(request):
    artistas = connection.cursor()
    artistas.execute("call listadoartista ()")
    return render(request, "artistas/listado.html",{'artistas':artistas})

def listadoartistasinactivos(request):
    artistas = connection.cursor()
    artistas.execute("call listadoartistasinactivos ()")
    return render(request, "artistas/listadoi.html",{'artistas':artistas})

def listadoartistasactivos(request):
    artistas = connection.cursor()
    artistas.execute("call listadoartistasactivos ()")
    return render(request, "artistas/listado.html",{'artistas':artistas})

def desactivarartistas(request, idartistas):
    artistas = connection.cursor()
    artistas.execute("call desactivarartistas ('"+str(idartistas)+"')")
    return redirect("/artistas/listado")

def activarartistas(request, idartistas):
    artistas = connection.cursor()
    artistas.execute("call activarartistas ('"+str(idartistas)+"')")
    return redirect("/artistas/listadoi")

def actualizarartistas(request,idartistas):
    if request.method=="POST":
        if request.POST.get("nombre") and request.POST.get("edad") and request.POST.get("nacionalidad") and request.POST.get("celular") and request.POST.get("correo") and request.POST.get("premios") and request.POST.get("fecha_firma") and request.POST.get("genero_musical"):
            artistas = Artistas()
            artistas.nombre =request.POST.get("nombre")
            artistas.edad =request.POST.get("edad")
            artistas.nacionalidad =request.POST.get("nacionalidad")
            artistas.celular =request.POST.get("celular")
            artistas.correo =request.POST.get("correo")
            artistas.premios =request.POST.get("premios")
            artistas.fecha_firma =request.POST.get("fecha_firma")
            artistas.genero_musical =request.POST.get("genero_musical")
            insertar = connection.cursor()
            try:

             if request.FILES["foto"]:
                 artistas.foto =request.FILES['foto']
                 unartista = Artistas.objects.get(id=idartistas)
                 fs = FileSystemStorage()
                 fs.delete(unartista.foto)
                 artistas.foto =request.FILES['foto']
                 fs.save(artistas.foto.name,artistas.foto)
                 insertar.execute("call actualizarartistas('"+str(idartistas)+"','"+artistas.nombre+"','"+artistas.edad+"','"+artistas.nacionalidad+"','"+artistas.celular+"','"+artistas.correo+"','"+artistas.premios+"','"+artistas.fecha_firma+"','"+artistas.foto.name+"','"+artistas.genero_musical+"')")
            except:
                insertar.execute("call actualizarartistas('"+str(idartistas)+"','"+artistas.nombre+"','"+artistas.edad+"','"+artistas.nacionalidad+"','"+artistas.celular+"','"+artistas.correo+"','"+artistas.premios+"','"+artistas.fecha_firma+"','"+request.POST.get("fotovieja")+"','"+artistas.genero_musical+"')")
            return redirect("/artistas/listado")
    else:
        artistas = Artistas.objects.filter(id=idartistas)
        return render(request,"artistas/actualizar.html",{'artistas':artistas})
        
#endregion
    
#region albums
    
def insertaralbum(request):
    if request.method=="POST":
        if request.POST.get("nombrea") and request.POST.get("duraciona") and request.POST.get("cantidad_canciones") and request.POST.get("idioma") and request.POST.get("genero_musical") and request.POST.get("ventas") and request.POST.get("fecha_lanzamiento") and request.FILES["foto"] and request.POST.get("colaboraciones") and request.POST.get("artistas"):
            albums = Albums()
            albums.nombrea =request.POST.get("nombrea")
            albums.duraciona =request.POST.get("duraciona")
            albums.cantidad_canciones =request.POST.get("cantidad_canciones")
            albums.idioma =request.POST.get("idioma")
            albums.genero_musical =request.POST.get("genero_musical")
            albums.ventas =request.POST.get("ventas")
            albums.fecha_lanzamiento =request.POST.get("fecha_lanzamiento")
            albums.foto =request.FILES["foto"]
            albums.colaboraciones =request.POST.get("colaboraciones")
            albums.artistas = Artistas.objects.get(id=request.POST.get("artistas"))
            imagen = FileSystemStorage()
            imagen.save(albums.foto.name,albums.foto)
            insertar = connection.cursor()
            insertar.execute("call insertaralbum('"+albums.nombrea+"','"+albums.duraciona+"','"+albums.cantidad_canciones+"','"+albums.idioma+"','"+albums.genero_musical+"','"+albums.ventas+"','"+albums.fecha_lanzamiento+"','"+albums.foto.name+"','"+albums.colaboraciones+"','"+request.POST.get("artistas")+"')")
            return redirect("/albums/listado")
    else: 
        artistas = Artistas.objects.filter(estado_contrato='Vigente')
        return render(request,"albums/insertar.html",{'artistas':artistas})  

def albumsnodestacados(request):
    albums = connection.cursor()
    albums.execute("call albumsnodestacados ()")
    artistas = Artistas.objects.all()
    return render(request, "albums/listadoi.html",{'albums':albums,'artistas':artistas})

def albumsdestacados(request):
    albums = connection.cursor()
    albums.execute("call albumsdestacados ()")
    return render(request, "albums/listado.html",{'albums':albums})

def nodestacaralbum(request, idalbum):
    albums = connection.cursor()
    albums.execute("call nodestacaralbum ('"+str(idalbum)+"')")
    return redirect("/albums/listado")

def destacaralbum(request, idalbum):
    albums = connection.cursor()
    albums.execute("call destacaralbum ('"+str(idalbum)+"')")
    return redirect("/albums/listadoi") 

def actualizaralbum(request,idalbum):
    if request.method=="POST":
        if request.POST.get("nombrea") and request.POST.get("duraciona") and request.POST.get("cantidad_canciones") and request.POST.get("idioma") and request.POST.get("genero_musical") and request.POST.get("ventas") and request.POST.get("fecha_lanzamiento") and request.POST.get("colaboraciones") and request.POST.get("artistas"):
            albums = Albums()
            albums.nombrea =request.POST.get("nombrea")
            albums.duraciona =request.POST.get("duraciona")
            albums.cantidad_canciones =request.POST.get("cantidad_canciones")
            albums.idioma =request.POST.get("idioma")
            albums.genero_musical =request.POST.get("genero_musical")
            albums.ventas =request.POST.get("ventas")
            albums.fecha_lanzamiento =request.POST.get("fecha_lanzamiento")
            albums.colaboraciones =request.POST.get("colaboraciones")
            albums.artistas = Artistas.objects.get(id=request.POST.get("artistas"))
            insertar = connection.cursor()
            try:

             if request.FILES["foto"]:
                 albums.foto =request.FILES['foto']
                 unalbum = Artistas.objects.get(id=idalbum)
                 fs = FileSystemStorage()
                 fs.delete(unalbum.foto)
                 albums.foto =request.FILES['foto']
                 fs.save(albums.foto.name,albums.foto)
                 insertar.execute("call actualizaralbum('"+str(idalbum)+"','"+albums.nombrea+"','"+albums.duraciona+"','"+albums.cantidad_canciones+"','"+albums.idioma+"','"+albums.genero_musical+"','"+albums.ventas+"','"+albums.fecha_lanzamiento+"','"+albums.foto.name+"','"+albums.colaboraciones+"','"+request.POST.get("artistas")+"')")
            except:
                insertar.execute("call actualizaralbum('"+str(idalbum)+"','"+albums.nombrea+"','"+albums.duraciona+"','"+albums.cantidad_canciones+"','"+albums.idioma+"','"+albums.genero_musical+"','"+albums.ventas+"','"+albums.fecha_lanzamiento+"','"+request.POST.get("fotovieja")+"','"+albums.colaboraciones+"','"+request.POST.get("artistas")+"')")
            return redirect("/albums/listado")
    else:
        artistas = Artistas.objects.filter(estado_contrato='Vigente')
        albums = Albums.objects.filter(id=idalbum)
        return render(request,"albums/actualizar.html",{'albums':albums,'artistas':artistas}) 

#endregion
    
    
#region tours

def insertartour(request):
    if request.method=="POST":
        if request.POST.get("nombret") and request.POST.get("fecha_inicio") and request.POST.get("fecha_fin") and request.POST.get("pais_visitar") and request.POST.get("ciudades_visitar") and request.POST.get("ventas_boletas") and request.POST.get("gananciast") and request.POST.get("patrocinadorest") and request.POST.get("artistas"):
            tour = Tours()
            tour.nombret =request.POST.get("nombret")
            tour.fecha_inicio =request.POST.get("fecha_inicio")
            tour.fecha_fin =request.POST.get("fecha_fin")
            tour.pais_visitar =request.POST.get("pais_visitar")
            tour.ciudades_visitar =request.POST.get("ciudades_visitar")
            tour.ventas_boletas =request.POST.get("ventas_boletas")
            tour.gananciast =request.POST.get("gananciast")
            tour.patrocinadorest =request.POST.get("patrocinadorest")
            tour.estado_tour="Completado"
            tour.artistas = Artistas.objects.get(id=request.POST.get("artistas"))
            tour.save()
            return redirect("/tours/listado")
    else: 
        artistas = Artistas.objects.filter(estado_contrato='Vigente')
        return render(request,"tours/insertar.html",{'artistas':artistas})

#Listado tours completados    
def listadotour(request):
    tours = connection.cursor()
    tours.execute("call listadotourcom ()")
    return render(request, "tours/listado.html",{'tours':tours})

#Listado Tours en curso
def listadotourcur(request):
    tours = connection.cursor()
    tours.execute("call listadotourcur ()")
    return render(request, "tours/listadocur.html",{'tours':tours})

#Listado Tours cancelado
def listadotourcan(request):
    tours = connection.cursor()
    tours.execute("call listadotourcan ()")
    return render(request, "tours/listadocan.html",{'tours':tours})

#Completar tour
def completartour(request, idtour):
    tours = connection.cursor()
    tours.execute("call completartour ('"+str(idtour)+"')")
    return redirect("/tours/listado")

#En curso tour
def encursotour(request, idtour):
    artistas = connection.cursor()
    artistas.execute("call encursotour ('"+str(idtour)+"')")
    return redirect("/tours/listadocur")

#Cancelar Tour
def cancelartour(request, idtour):
    artistas = connection.cursor()
    artistas.execute("call cancelartour ('"+str(idtour)+"')")
    return redirect("/tours/listadocan")

def actualizartour(request,id):
    if request.method=="POST":
        if request.POST.get("nombret") and request.POST.get("fecha_inicio") and request.POST.get("fecha_fin") and request.POST.get("pais_visitar") and request.POST.get("ciudades_visitar") and request.POST.get("ventas_boletas") and request.POST.get("gananciast") and request.POST.get("patrocinadorest") and request.POST.get("artistas"):
            tour = Tours.objects.get(id=id)
            tour.nombret =request.POST.get("nombret")
            tour.fecha_inicio =request.POST.get("fecha_inicio")
            tour.fecha_fin =request.POST.get("fecha_fin")
            tour.pais_visitar =request.POST.get("pais_visitar")
            tour.ciudades_visitar =request.POST.get("ciudades_visitar")
            tour.ventas_boletas =request.POST.get("ventas_boletas")
            tour.gananciast =request.POST.get("gananciast")
            tour.patrocinadorest =request.POST.get("patrocinadorest")
            tour.artistas = Artistas.objects.get(id=request.POST.get("artistas"))
            tour.save()
            return redirect("/tours/listado")
    else: 
        tour = Tours.objects.filter(id=id)
        artistas = Artistas.objects.filter(estado_contrato='Vigente')
        return render(request,'tours/actualizar.html',{'tour':tour,'artistas':artistas})

#endregion