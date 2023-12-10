from django.urls import path
from . import views
from .models import Kinodb, Rekinodb, Chanchitodb, Combodb, Chao1db, Chao2db, Chao3db


urlpatterns = [
    path('', views.index, name='index'),  # Aca despues el menú
    path('kino/', views.resultado_kino, name='kino_index'),
    path('rekino/', views.resultado_rekino, name='rekino_index'),
    path('chanchito/', views.resultado_chanchito, name='chanchito_index'),
    path('combo/', views.resultado_combo, name='combo_index'),
    path('chao1/', views.resultado_chao1, name='chao1_index'),
    path('chao2/', views.resultado_chao2, name='chao2_index'),
    path('chao3/', views.resultado_chao3, name='chao3_index'),
    path('archivos/', views.upload_file, name='archivos_index'),


    #Url de botones
    path('delete/<str:model_name>/<int:pk>/',
         views.delete_file, name='delete-file'),
    path('todatabase/<int:pk>/', views.agregar_a_db, name='agregar-a-db'),
    path('delete-row/<str:model_name>/<int:pk>/',
         views.delete_row, name='delete-row'),

]
