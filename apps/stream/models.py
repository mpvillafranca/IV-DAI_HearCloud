from django.db import models
import datetime

# Create your models here.
class AudioFile(models.Model):
    # Titulo: string. No nulo
    # Link permanente: string. No nulo
    # Modo de compartir (publico/privado): String
    # URL de la imagen: string
    # Descripcion: string
    # Duracion: int
    # Genero: string
    # Descargable: bool
    # Fecha creacion: datetime. No nulo.
    # Fecha actualizacion: datetime. No nulo.
    # Usuario al que pertenece
    
    name = models.CharField(max_length=100, unique=True)
    audio_file = models.FileField(upload_to='uploads', null=False)
    genre = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    upload_date = models.DateTimeField(default=datetime.datetime.now)
