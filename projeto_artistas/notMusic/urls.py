from django.urls import path
from . import views

app_name = "notMusic"
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('albuns/<int:pk>/',views.AlbumView.as_view(),name='albuns'),
    path('musicas/<int:pk>/',views.ResultadoMusicaView.as_view(), name='musicas')
]