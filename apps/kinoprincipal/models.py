from django.db import models


class Kinodb(models.Model):
    id_sorteo = models.IntegerField()
    fecha = models.DateField()
    number1 = models.PositiveSmallIntegerField()
    number2 = models.PositiveSmallIntegerField()
    number3 = models.PositiveSmallIntegerField()
    number4 = models.PositiveSmallIntegerField()
    number5 = models.PositiveSmallIntegerField()
    number6 = models.PositiveSmallIntegerField()
    number7 = models.PositiveSmallIntegerField()
    number8 = models.PositiveSmallIntegerField()
    number9 = models.PositiveSmallIntegerField()
    number10 = models.PositiveSmallIntegerField()
    number11 = models.PositiveSmallIntegerField()
    number12 = models.PositiveSmallIntegerField()
    number13 = models.PositiveSmallIntegerField()
    number14 = models.PositiveSmallIntegerField()
    num_ganadores = models.PositiveSmallIntegerField(null=True, blank=True)
    tipo_ingreso = models.CharField(default=" ", max_length=10)

    def __str__(self):
        return f"KINODB ID: {self.id_sorteo} FECHA: {self.fecha} NUMEROS: {self.number1} {self.number2} {self.number3} {self.number4} {self.number5} {self.number6} {self.number7} {self.number8} {self.number9} {self.number10} {self.number11} {self.number12} {self.number13} {self.number14} GANADOR {self.num_ganadores}"


class Rekinodb(models.Model):
    id_sorteo = models.IntegerField()
    fecha = models.DateField()
    number1 = models.PositiveSmallIntegerField()
    number2 = models.PositiveSmallIntegerField()
    number3 = models.PositiveSmallIntegerField()
    number4 = models.PositiveSmallIntegerField()
    number5 = models.PositiveSmallIntegerField()
    number6 = models.PositiveSmallIntegerField()
    number7 = models.PositiveSmallIntegerField()
    number8 = models.PositiveSmallIntegerField()
    number9 = models.PositiveSmallIntegerField()
    number10 = models.PositiveSmallIntegerField()
    number11 = models.PositiveSmallIntegerField()
    number12 = models.PositiveSmallIntegerField()
    number13 = models.PositiveSmallIntegerField()
    number14 = models.PositiveSmallIntegerField()
    num_ganadores = models.PositiveSmallIntegerField(null=True, blank=True)
    tipo_ingreso = models.CharField(default=" ", max_length=10)

    def __str__(self):
        return f"REKINODB ID: {self.id_sorteo} FECHA: {self.fecha} NUMEROS: {self.number1} {self.number2} {self.number3} {self.number4} {self.number5} {self.number6} {self.number7} {self.number8} {self.number9} {self.number10} {self.number11} {self.number12} {self.number13} {self.number14} GANADOR {self.num_ganadores}"


class Chanchitodb(models.Model):
    id_sorteo = models.IntegerField()
    fecha = models.DateField()
    number1 = models.PositiveSmallIntegerField()
    number2 = models.PositiveSmallIntegerField()
    number3 = models.PositiveSmallIntegerField()
    number4 = models.PositiveSmallIntegerField()
    number5 = models.PositiveSmallIntegerField()
    number6 = models.PositiveSmallIntegerField()
    number7 = models.PositiveSmallIntegerField()
    number8 = models.PositiveSmallIntegerField()
    number9 = models.PositiveSmallIntegerField()
    number10 = models.PositiveSmallIntegerField()
    number11 = models.PositiveSmallIntegerField()
    number12 = models.PositiveSmallIntegerField()
    number13 = models.PositiveSmallIntegerField()
    number14 = models.PositiveSmallIntegerField()
    num_ganadores = models.PositiveSmallIntegerField(null=True, blank=True)
    tipo_ingreso = models.CharField(default=" ", max_length=10)

    def __str__(self):
        return f"CHANCHITODB ID: {self.id_sorteo} FECHA: {self.fecha} NUMEROS: {self.number1} {self.number2} {self.number3} {self.number4} {self.number5} {self.number6} {self.number7} {self.number8} {self.number9} {self.number10} {self.number11} {self.number12} {self.number13} {self.number14} GANADOR {self.num_ganadores}"


class Combodb(models.Model):
    id_sorteo = models.IntegerField()
    fecha = models.DateField()
    number1 = models.PositiveSmallIntegerField()
    number2 = models.PositiveSmallIntegerField()
    number3 = models.PositiveSmallIntegerField()
    number4 = models.PositiveSmallIntegerField()
    number5 = models.PositiveSmallIntegerField()
    number6 = models.PositiveSmallIntegerField()
    number7 = models.PositiveSmallIntegerField()
    number8 = models.PositiveSmallIntegerField()
    number9 = models.PositiveSmallIntegerField()
    number10 = models.PositiveSmallIntegerField()
    number11 = models.PositiveSmallIntegerField()
    number12 = models.PositiveSmallIntegerField()
    number13 = models.PositiveSmallIntegerField()
    number14 = models.PositiveSmallIntegerField()
    num_ganadores = models.PositiveSmallIntegerField(null=True, blank=True)
    tipo_ingreso = models.CharField(default=" ", max_length=10)

    def __str__(self):
        return f"COMBODB ID: {self.id_sorteo} FECHA: {self.fecha} NUMEROS: {self.number1} {self.number2} {self.number3} {self.number4} {self.number5} {self.number6} {self.number7} {self.number8} {self.number9} {self.number10} {self.number11} {self.number12} {self.number13} {self.number14} GANADOR {self.num_ganadores}"


class Chao1db(models.Model):
    id_sorteo = models.IntegerField()
    fecha = models.DateField()
    number1 = models.PositiveSmallIntegerField()
    number2 = models.PositiveSmallIntegerField()
    number3 = models.PositiveSmallIntegerField()
    number4 = models.PositiveSmallIntegerField()
    number5 = models.PositiveSmallIntegerField()
    number6 = models.PositiveSmallIntegerField()
    number7 = models.PositiveSmallIntegerField()
    number8 = models.PositiveSmallIntegerField()
    number9 = models.PositiveSmallIntegerField()
    number10 = models.PositiveSmallIntegerField()
    number11 = models.PositiveSmallIntegerField()
    number12 = models.PositiveSmallIntegerField()
    number13 = models.PositiveSmallIntegerField()
    number14 = models.PositiveSmallIntegerField()
    num_ganadores = models.PositiveSmallIntegerField(null=True, blank=True)
    tipo_ingreso = models.CharField(default=" ", max_length=10)

    def __str__(self):
        return f"CHAO1DB ID: {self.id_sorteo} FECHA: {self.fecha} NUMEROS: {self.number1} {self.number2} {self.number3} {self.number4} {self.number5} {self.number6} {self.number7} {self.number8} {self.number9} {self.number10} {self.number11} {self.number12} {self.number13} {self.number14} GANADOR {self.num_ganadores}"


class Chao2db(models.Model):
    id_sorteo = models.IntegerField()
    fecha = models.DateField()
    number1 = models.PositiveSmallIntegerField()
    number2 = models.PositiveSmallIntegerField()
    number3 = models.PositiveSmallIntegerField()
    number4 = models.PositiveSmallIntegerField()
    number5 = models.PositiveSmallIntegerField()
    number6 = models.PositiveSmallIntegerField()
    number7 = models.PositiveSmallIntegerField()
    number8 = models.PositiveSmallIntegerField()
    number9 = models.PositiveSmallIntegerField()
    number10 = models.PositiveSmallIntegerField()
    number11 = models.PositiveSmallIntegerField()
    number12 = models.PositiveSmallIntegerField()
    number13 = models.PositiveSmallIntegerField()
    number14 = models.PositiveSmallIntegerField()
    num_ganadores = models.PositiveSmallIntegerField(null=True, blank=True)
    tipo_ingreso = models.CharField(default=" ", max_length=10)

    def __str__(self):
        return f"CHAO2DB ID: {self.id_sorteo} FECHA: {self.fecha} NUMEROS: {self.number1} {self.number2} {self.number3} {self.number4} {self.number5} {self.number6} {self.number7} {self.number8} {self.number9} {self.number10} {self.number11} {self.number12} {self.number13} {self.number14} GANADOR {self.num_ganadores}"


class Chao3db(models.Model):
    id_sorteo = models.IntegerField()
    fecha = models.DateField()
    number1 = models.PositiveSmallIntegerField()
    number2 = models.PositiveSmallIntegerField()
    number3 = models.PositiveSmallIntegerField()
    number4 = models.PositiveSmallIntegerField()
    number5 = models.PositiveSmallIntegerField()
    number6 = models.PositiveSmallIntegerField()
    number7 = models.PositiveSmallIntegerField()
    number8 = models.PositiveSmallIntegerField()
    number9 = models.PositiveSmallIntegerField()
    number10 = models.PositiveSmallIntegerField()
    number11 = models.PositiveSmallIntegerField()
    number12 = models.PositiveSmallIntegerField()
    number13 = models.PositiveSmallIntegerField()
    number14 = models.PositiveSmallIntegerField()
    num_ganadores = models.PositiveSmallIntegerField(null=True, blank=True)
    tipo_ingreso = models.CharField(default=" ", max_length=10)

    def __str__(self):
        return f"CHAO3DB ID: {self.id_sorteo} FECHA: {self.fecha} NUMEROS: {self.number1} {self.number2} {self.number3} {self.number4} {self.number5} {self.number6} {self.number7} {self.number8} {self.number9} {self.number10} {self.number11} {self.number12} {self.number13} {self.number14} GANADORES: {self.num_ganadores}"


class Archivosxl(models.Model):
    file = models.FileField(upload_to='excels')

    def delete(self):
        self.file.delete()
        super().delete()
