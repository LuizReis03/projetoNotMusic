from django.urls import path
from . import views

app_name = "notMusic"
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('todosAlbuns/',views.TodosAlbunsView.as_view(),name='todosAlbuns'),
    path('albuns/<int:pk>/',views.AlbumView.as_view(),name='albuns'),
    path('todasMusicas/',views.TodasMusicasView.as_view(), name='todasMusicas'),
    path('musicas/<int:pk>/',views.ResultadoMusicaView.as_view(), name='musicas')
]