from django.shortcuts import render, get_object_or_404
from .models import Artista, Album, Musica
from django.views import generic

# Create your views here.

class IndexView(generic.ListView): 
    template_name = 'notMusic/index.html'
    context_object_name = 'lista_de_artistas'

    def get_queryset(self):
        return Artista.objects.all()

class TodosAlbunsView(generic.ListView): 
    template_name = 'notMusic/todosAlbuns.html'
    context_object_name = 'lista_de_albuns'

    def get_queryset(self):
        return Album.objects.all()

class AlbumView(generic.DetailView):
    model = Artista
    template_name = 'notMusic/albuns.html'

class ResultadoMusicaView(generic.DetailView):
    model = Album
    template_name = "notMusic/musicas.html"

class TodasMusicasView(generic.ListView): 
    template_name = 'notMusic/todasMusicas.html'
    context_object_name = 'lista_de_musicas'

    def get_queryset(self):
        return Musica.objects.all()