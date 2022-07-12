from django.contrib import admin
from .models import Artista, Album, Musica

# Register your models here.
admin.site.register(Artista)
admin.site.register(Album)
admin.site.register(Musica)