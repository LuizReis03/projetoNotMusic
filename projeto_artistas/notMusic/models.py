from django.db import models

# Create your models here.

class Musica(models.Model):
    tituloMusica = models.CharField(max_length=50)
    duracao = models.CharField(max_length=10)
    compositor = models.CharField(max_length=80)
    linkMusica = models.CharField(max_length=200, default= "null")
    fotoMusica = models.CharField(max_length=200, default= "null")

    def __str__(self):
        return self.tituloMusica

class Album(models.Model):
    nomeAlbum = models.CharField(max_length=50)
    anoLanc = models.CharField(max_length=4)
    musicas = models.ManyToManyField(Musica)
    upVotes = models.IntegerField(default=0)
    downVotes = models.IntegerField(default=0)
    linkImg = models.CharField(max_length=200, default= "null")

    def __str__(self):
        return self.nomeAlbum

class Artista(models.Model):
    nomeArtista = models.CharField(max_length=200)
    genero = models.CharField(max_length=50)
    anoEstreia = models.CharField(max_length=4)
    albuns = models.ManyToManyField(Album)
    fotoArtista = models.CharField(max_length=200, default= "null")

    def __str__(self):
        return self.nomeArtista
