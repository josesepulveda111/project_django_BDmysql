from  django.db import models

class Artistas(models.Model):
    nombre = models.CharField(max_length=225)
    edad = models.CharField(max_length=20)
    nacionalidad = models.CharField(max_length=255)
    celular = models.CharField(max_length=255)
    correo = models.CharField(max_length=255)
    premios = models.CharField(max_length=255)
    fecha_firma = models.DateField()
    foto = models.CharField(max_length=255)
    genero_musical = models.CharField(max_length=255)
    estado_contrato = models.CharField(max_length=255)
    class Meta:
        db_table = 'artistas'

class Albums(models.Model):
    nombrea = models.CharField(max_length=255)
    duraciona = models.CharField(max_length=255)
    cantidad_canciones = models.CharField(max_length=255)
    idioma = models.CharField(max_length=255)
    genero_musical = models.CharField(max_length=255)
    ventas = models.CharField(max_length=255)
    fecha_lanzamiento = models.DateField()
    foto = models.CharField(max_length=255)
    colaboraciones = models.CharField(max_length=255)
    artistas = models.ForeignKey(Artistas, on_delete=models.CASCADE)
    class Meta:
        db_table = 'album'

class Tours(models.Model):
    nombret = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    pais_visitar = models.CharField(max_length=255)
    ciudades_visitar = models.CharField(max_length=255)
    ventas_boletas = models.CharField(max_length=255)
    gananciast = models.CharField(max_length=255)
    patrocinadorest = models.CharField(max_length=255)
    estado_tour = models.CharField(max_length=255)
    artistas = models.ForeignKey(Artistas, on_delete=models.CASCADE)
    class Meta:
        db_table = 'tours'