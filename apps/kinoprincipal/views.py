from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import UploadFileForm
from .models import Archivosxl, Kinodb, Rekinodb, Chanchitodb, Combodb, Chao1db, Chao2db, Chao3db
from .excel import Importar_datos
from django.apps import apps
# Refrigerador.objects.latest('fecha_registro')


def index(request):

    resultados_kino = Kinodb.objects.order_by("-fecha")[:5].values()
    resultados_rekino = Rekinodb.objects.order_by("-fecha")[:5].values()
    resultados_chanchito = Chanchitodb.objects.order_by("-fecha")[:5].values()
    resultados_combo = Combodb.objects.order_by("-fecha")[:5].values()
    resultados_chao1 = Chao1db.objects.order_by("-fecha")[:5].values()
    resultados_chao2 = Chao2db.objects.order_by("-fecha")[:5].values()
    resultados_chao3 = Chao3db.objects.order_by("-fecha")[:5].values()
    context = {'Resultados_kino': resultados_kino,
               'Resultados_rekino': resultados_rekino,
               'Resultados_chanchito': resultados_chanchito,
               'Resultados_combo': resultados_combo,
               'Resultados_chao1': resultados_chao1,
               'Resultados_chao2': resultados_chao2,
               'Resultados_chao3': resultados_chao3}

    return render(request, 'index.html', context)


def resultado_kino(request):
    resultado = Kinodb.objects.all
    context = {'RESULTADO': resultado, 'database': Kinodb.__name__}
    return render(request, 'ver_bd.html', context)


def resultado_rekino(request):

    resultado = Rekinodb.objects.all
    context = {'RESULTADO': resultado, 'database': Rekinodb.__name__}
    return render(request, 'ver_bd.html', context)


def resultado_chanchito(request):

    resultado = Chanchitodb.objects.all
    context = {'RESULTADO': resultado, 'database': Chanchitodb.__name__}
    return render(request, 'ver_bd.html', context)


def resultado_combo(request):

    resultado = Combodb.objects.all
    context = {'RESULTADO': resultado, 'database': Combodb.__name__}
    return render(request, 'ver_bd.html', context)


def resultado_chao1(request):

    resultado = Chao1db.objects.all
    context = {'RESULTADO': resultado, 'database': Chao1db.__name__}
    return render(request, 'ver_bd.html', context)


def resultado_chao2(request):

    resultado = Chao2db.objects.all
    context = {'RESULTADO': resultado, 'database': Chao2db.__name__}
    return render(request, 'ver_bd.html', context)


def resultado_chao3(request):

    resultado = Chao3db.objects.all
    context = {'RESULTADO': resultado, 'database': Chao3db.__name__}
    return render(request, 'ver_bd.html', context)


def upload_file(request):
    lista_excel = Archivosxl.objects.all
    if request.method == 'POST':
        print('request', request)
        form = UploadFileForm(request.POST, request.FILES)
        file = request.FILES['file']
        file_to_db = Archivosxl.objects.create(file=file)
        return render(request, 'upload.html', {'form': form, 'lista_excel': lista_excel, 'database': Archivosxl.__name__})
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form, 'lista_excel': lista_excel, 'database': Archivosxl.__name__})


def comparar_bd_con_excel(request):
    pass


def delete_file(request, model_name, pk):
    archivo = get_object_or_404(apps.get_model(
        'kinoprincipal', model_name), pk=pk)
    archivo.delete()
    return redirect('archivos_index')


def agregar_a_db(request, pk):
    archivo = get_object_or_404(Archivosxl, pk=pk)
    Importar_datos(archivo.file)
    return redirect('archivos_index')


def delete_row(request, model_name, pk):
    row = get_object_or_404(apps.get_model('kinoprincipal', model_name), pk=pk)
    row.delete()
    print("URL: ", model_name.lower()[:-2] + "_index")
    url = model_name.lower()[:-2] + "_index"
    return redirect(url)
