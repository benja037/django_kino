from openpyxl import load_workbook
from apps.kinoprincipal.models import Kinodb, Rekinodb, Chanchitodb, Combodb, Chao1db, Chao2db, Chao3db, Archivosxl
import datetime


def Importar_datos(archivo):
    # Leer Excel
    wb = load_workbook(filename=archivo)
    ws = wb["Kino_Int"]

    ultima_fila = ws.max_row - 3
    rango_casillas = "A808:Q" + str(ultima_fila)
    lista_total = []
    for row in ws[rango_casillas]:
        sorteo = int(row[0].value)
        fecha = row[1].value
        numero1 = int(row[2].value)
        numero2 = int(row[3].value)
        numero3 = int(row[4].value)
        numero4 = int(row[5].value)
        numero5 = int(row[6].value)
        numero6 = int(row[7].value)
        numero7 = int(row[8].value)
        numero8 = int(row[9].value)
        numero9 = int(row[10].value)
        numero10 = int(row[11].value)
        numero11 = int(row[12].value)
        numero12 = int(row[13].value)
        numero13 = int(row[14].value)
        numero14 = int(row[15].value)
        elemento = Kinodb(id_sorteo=sorteo, fecha=fecha, number1=numero1, number2=numero2, number3=numero3, number4=numero4, number5=numero5, number6=numero6,
                          number7=numero7, number8=numero8, number9=numero9, number10=numero10, number11=numero11, number12=numero12, number13=numero13, number14=numero14)
        lista_total.append(elemento)

    Kinodb.objects.bulk_create(lista_total)

    #
