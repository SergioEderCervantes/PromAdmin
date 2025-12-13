from django.contrib import admin
from django.db.models import Sum
from tickets.models import Alumno, Pago

class PagoInline(admin.TabularInline):
    model = Pago
    extra = 0

class AlumnoAdmin(admin.ModelAdmin):
    inlines = [PagoInline]
    list_display = ('nombre', 'estado', 'invitados_min', 'invitados_max', 'boletos_pagados')
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

admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Pago)