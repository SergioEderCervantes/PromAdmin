from django.contrib import admin 
from django.db.models import Sum
from django.utils.html import format_html 
from tickets.models import Alumno, Pago
from unfold.admin import ModelAdmin, TabularInline 

def get_image_html(image_url):
    """Generates an HTML img tag with click-to-zoom functionality."""
    if not image_url:
        return "No Imagen"
    
    style_normal = "height: 50px; width: auto; cursor: zoom-in; transition: transform 0.2s;"
    style_zoomed = "position: fixed; top: 0; left: 0; width: 100%; height: 100%; object-fit: contain; background: rgba(0,0,0,0.8); z-index: 9999; cursor: zoom-out;"
    
    return format_html(
        '''
        <img src="{}" style="{}" onclick="
            if (this.classList.contains('enlarged')) {{
                this.classList.remove('enlarged');
                this.style.cssText = '{}';
            }} else {{
                this.classList.add('enlarged');
                this.style.cssText = '{}';
            }}
        " />
        ''',
        image_url,
        style_normal,
        style_normal,
        style_zoomed
    )

class PagoInline(TabularInline):
    model = Pago
    extra = 0
    readonly_fields = ('comprobante_preview',)

    def comprobante_preview(self, obj):
        if obj.comprobante:
            return get_image_html(obj.comprobante.url)
        return "No Imagen"
    comprobante_preview.short_description = "Vista Previa"

@admin.register(Alumno) 
class AlumnoAdmin(ModelAdmin):
    inlines = [PagoInline]
    list_display = ('nombre', 'estado', 'estado_color', 'invitados_min', 'invitados_max', 'boletos_pagados', 'ultimo_comprobante') 
    list_filter = ('estado',)
    search_fields = ('nombre',)

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

    def ultimo_comprobante(self, obj):
        ultimo_pago = obj.pagos.last()
        if ultimo_pago and ultimo_pago.comprobante:
            return get_image_html(ultimo_pago.comprobante.url)
        return "-"
    ultimo_comprobante.short_description = "Último Pago"

@admin.register(Pago)
class PagoAdmin(ModelAdmin):
    list_display = ('alumno', 'cantidad_boletos', 'fecha_subida', 'comprobante_preview')
    list_filter = ('alumno__nombre',)
    readonly_fields = ('comprobante_preview',)

    def comprobante_preview(self, obj):
        if obj.comprobante:
            return get_image_html(obj.comprobante.url)
        return "No Imagen"
    
    comprobante_preview.short_description = "Comprobante"