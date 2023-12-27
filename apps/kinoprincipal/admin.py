from django.contrib import admin
from .models import Kinodb,Rekinodb,Chanchitodb,Combodb,Chao1db,Chao2db,Chao3db,Archivosxl
# Register your models here.

class SorteoAdmin(admin.ModelAdmin):
    list_display = ['id_sorteo','number1','number2','number3','number4','number5','number6','number7','number8','number9','number10','number11','number12','number13','number14']



admin.site.register(Kinodb,SorteoAdmin)
admin.site.register(Rekinodb,SorteoAdmin)
admin.site.register(Chanchitodb,SorteoAdmin)
admin.site.register(Combodb,SorteoAdmin)
admin.site.register(Chao1db,SorteoAdmin)
admin.site.register(Chao2db,SorteoAdmin)
admin.site.register(Chao3db,SorteoAdmin)
admin.site.register(Archivosxl)