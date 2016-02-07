from django.db import models
import datetime

# Create your models here.
class AudioFile(models.Model):
    # Titulo: string. No nulo
    # Link permanente: string. No nulo
    # Modo de compartir (público/privado): String
    # URL de la imagen: string
    # Descripcion: string
    # Duracion: int
    # Genero: string
    # Descargable: bool
    # Fecha creacion: datetime. No nulo.
    # Fecha actualizacion: datetime. No nulo.
    # Usuario al que pertenece
