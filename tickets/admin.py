from django.contrib import admin 
from django.db.models import Sum
from django.utils.html import format_html 
from tickets.models import Alumno, Pago
from unfold.admin import ModelAdmin, TabularInline 

class PagoInline(TabularInline):
    model = Pago
    extra = 0

@admin.register(Alumno) 
class AlumnoAdmin(ModelAdmin):
    inlines = [PagoInline]
    list_display = ('nombre', 'estado', 'estado_color', 'invitados_min', 'invitados_max', 'boletos_pagados') 
    list_filter = ('estado',)

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return ('nombre', 'invitados_min', 'invitados_max') 
        return super().get_readonly_fields(request, obj)

    def get_list_editable(self, request):
        if request.user.is_superuser:
            return ('estado',)
        return ('estado',)

    def changelist_view(self, request, extra_context=None):
        self.list_editable = self.get_list_editable(request)
        return super().changelist_view(request, extra_context)

    def boletos_pagados(self, obj):
        total_boletos = obj.pagos.aggregate(Sum('cantidad_boletos'))['cantidad_boletos__sum'] or 0
        return total_boletos
    
    boletos_pagados.short_description = "Boletos Pagados"

    def estado_color(self, obj):
        colors = {
            'al_corriente': 'green',
            'pendiente': 'red',
            'prorroga': 'orange',
        }
        color = colors.get(obj.estado, 'gray')
        
        return format_html(
            '<span style="display:inline-block; width:15px; height:15px; border-radius:50%; background-color:{}; margin-right:5px; vertical-align:middle;"></span>',
            color
        )
    estado_color.short_description = "Estado Visual"
    estado_color.admin_order_field = 'estado' 

@admin.register(Pago)
class PagoAdmin(ModelAdmin):
    list_display = ('alumno', 'cantidad_boletos', 'fecha_subida', 'comprobante')
    list_filter = ('alumno__nombre',)