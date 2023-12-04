from django.urls import path
from . import views
from apps.kinoprincipal.views import upload_file

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', upload_file, name='list'),
]
