from django.http.response import HttpResponse
from django.shortcuts import render
from apps.kinoprincipal.models import Kinodb
from .forms import UploadFileForm
from .models import Archivosxl
# Refrigerador.objects.latest('fecha_registro')


def index(request):

    resultado = Kinodb.objects.filter(number1=4)

    context = {'RESULTADO': resultado}
    print(context)
    if request.htmx:
        return HttpResponse(''.join([f'<li>{p.number1}-{p.number2}-{p.number3}-{p.number4}-{p.number5}-{p.number6}-{p.number7}-{p.number8}-{p.number9}-{p.number10}-{p.number11}-{p.number12}-{p.number13}-{p.number14}</li>' for p in resultado]))
    return render(request, 'index.html', context)


def upload_file(request):
    lista_excel = Archivosxl.objects.all
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        file = request.FILES['file']
        file_to_db = Archivosxl.objects.create(file=file)
        return HttpResponse("The name of uploaded file is " + str(file))

    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form, 'lista_excel': lista_excel})


def comparar_bd_con_excel(request):
    pass
