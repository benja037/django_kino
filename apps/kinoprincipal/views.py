from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import UploadFileForm
from .models import Archivosxl, Kinodb, Rekinodb, Chanchitodb, Combodb, Chao1db, Chao2db, Chao3db
from .excel import Importar_datos
from django.apps import apps
from statistics import mode
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


def resultados(request):
    path = request.path
    modelo = find_modelo(path)
    resultado = modelo.objects.all
    context = {'RESULTADO': resultado, 'database': modelo}
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
        #print(request.path)
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

def estadisticas(request):
    path = request.path
    modelo = find_modelo(str(path))

    #Resultados Todos
    labels = []
    cantidades = [] 
    resultado_todos = modelo.objects.values_list("number1","number2","number3","number4","number5","number6","number7","number8","number9","number10","number11","number12","number13","number14")
    lista_duplicados = []
    num_rep_duplicados = []
    lista_elementos_unicos = [] #Es decir que aunque este duplicado en esta lista solo saldra una vez
    lista = list(resultado_todos)
    
    flat_list = []
    for row in lista:
        flat_list.extend(row)
    for i in range(1,26):
        labels.append(i)
        cantidades.append(flat_list.count(i))
    context = {'labels': labels, 'data': cantidades}
    #print(cantidades) 
    #Resultados por posicion
    
    for i in range(1,15):
        number = "number" + str(i)
        resultado_i = list(modelo.objects.values_list(number,flat= True))     
        #print(resultado_i) 
        str_data_i = "data" + str(i)
        lista_cantidades_i = []
        for n in range(1,26):            
            lista_cantidades_i.append(resultado_i.count(n))
            
        context[str_data_i]=lista_cantidades_i




    #Resultados de conjuntos
    #Mostrar probabilidad de ganar el sorteo (grafico podria ser)
    #Probabilidad de ganar el sorte es 1 / comibinatoria de 25 sobre 14 = 1/4457400
    #Pasar directo al html
    #Crear tabla de los conjuntos que más salieron ganadores, seria mas facil con pandas y mas rapido que este for
    for i in lista:
        if i not in lista_elementos_unicos:
            lista_elementos_unicos.append(i)
        else:            
            if i in lista_duplicados:
                i_index = lista_duplicados.index(i)
                
                aux_num_dupl = num_rep_duplicados[i_index]
                num_rep_duplicados[i_index] = aux_num_dupl + 1

                i_index = lista_duplicados.index(i)

                
            else:
                lista_duplicados.append(i)
                num_rep_duplicados.append(2)
    print(lista_duplicados)
    print(num_rep_duplicados)
    #Mostrar grafico que separe en dos (conjuntos que salieron al menos una vez, conjuntos que nunca salieron)
    #print(lista_duplicados)
    model_exactos = Combodb.objects.filter(number1 =2,number2=4,number3=5,number4=7,number5=8,number6=12,number7=13,number8=14,number9=16,number10=17,number11=18,number12=19,number13=23,number14=24)
    print(list(model_exactos.values()))#Funciona pero sujeto a los cambios en la base de datos que no son del kino propiamente
    return render(request, 'estadisticas.html', context)


def find_modelo(path):
    lista_path_modelos = [["/estadisticas-kino/",Kinodb],["/estadisticas-rekino/",Rekinodb],["/estadisticas-chanchito/",Chanchitodb],
                          ["/estadisticas-combo/",Combodb],["/estadisticas-chao1/",Chao1db],["/estadisticas-chao2/",Chao2db],["/estadisticas-chao3/",Chao3db],
                          ["/kino/",Kinodb],["/rekino/",Rekinodb],["/chanchito/",Chanchitodb],["/combo/",Combodb],["/chao1/",Chao1db], ["/chao2/",Chao2db],["/chao3/",Chao3db]                   
                          ]
    for elemento in lista_path_modelos:
        if path in elemento[0]:
            return elemento[1]