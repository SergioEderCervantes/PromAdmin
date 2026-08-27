from django.db.models import Sum
from .models import Alumno, Pago


def dashboard_callback(request, context):
    """
    Dashboard profesional para PromAdmin con métricas clave y navegación rápida.
    """
    
    # ===== MÉTRICAS PRINCIPALES =====
    total_alumnos = Alumno.objects.count()
    total_boletos_vendidos = Pago.objects.aggregate(total=Sum('cantidad_boletos'))['total'] or 0
    total_pagos_realizados = Pago.objects.count()
    
    # Conteo por estado
    alumnos_pendientes = Alumno.objects.filter(estado='pendiente').count()
    alumnos_al_corriente = Alumno.objects.filter(estado='al_corriente').count()
    alumnos_prorroga = Alumno.objects.filter(estado='prorroga').count()
    
    # Cálculo de porcentajes
    porcentaje_al_corriente = round((alumnos_al_corriente / total_alumnos * 100), 1) if total_alumnos > 0 else 0
    porcentaje_pendientes = round((alumnos_pendientes / total_alumnos * 100), 1) if total_alumnos > 0 else 0

    # Boletos mínimos/máximos declarados por los alumnos
    boletos_min_totales = Alumno.objects.aggregate(total=Sum('invitados_min'))['total'] or 0
    boletos_max_totales = Alumno.objects.aggregate(total=Sum('invitados_max'))['total'] or 0

    # ===== KPI CARDS =====
    context.update({
        "kpi": [
            {
                "title": "Total de Alumnos",
                "metric": total_alumnos,
                "footer": f"{alumnos_al_corriente} al corriente • {alumnos_pendientes} pendientes",
                "icon": "people",
            },
            {
                "title": "Boletos Vendidos",
                "metric": total_boletos_vendidos,
                "footer": f"{total_pagos_realizados} transacciones realizadas",
                "icon": "confirmation_number",
            },
            {
                "title": "Alumnos al Corriente",
                "metric": f"{porcentaje_al_corriente}%",
                "footer": f"{alumnos_al_corriente} de {total_alumnos} alumnos",
                "icon": "check_circle",
            },
            {
                "title": "Alumnos Pendientes",
                "metric": alumnos_pendientes,
                "footer": f"{porcentaje_pendientes}% del total • ¡Requiere atención!",
                "icon": "warning",
            },
            {
                "title": "Boletos Mínimos Requeridos",
                "metric": boletos_min_totales,
                "footer": f"Suma de invitados mínimos de {total_alumnos} alumnos",
                "icon": "trending_down",
            },
            {
                "title": "Boletos Máximos Requeridos",
                "metric": boletos_max_totales,
                "footer": f"Suma de invitados máximos de {total_alumnos} alumnos",
                "icon": "trending_up",
            },
        ],
        
        # ===== NAVEGACIÓN RÁPIDA =====
        "navigation": [
            {
                "title": "Gestión de Alumnos",
                "items": [
                    {
                        "title": "Todos los Alumnos",
                        "icon": "people",
                        "link": "/admin/tickets/alumno/",
                    },
                    {
                        "title": "Alumnos al Corriente",
                        "icon": "check_circle",
                        "link": "/admin/tickets/alumno/?estado__exact=al_corriente",
                        "badge": alumnos_al_corriente,
                    },
                    {
                        "title": "Alumnos Pendientes",
                        "icon": "warning",
                        "link": "/admin/tickets/alumno/?estado__exact=pendiente",
                        "badge": alumnos_pendientes,
                    },
                    {
                        "title": "Alumnos en Prórroga",
                        "icon": "schedule",
                        "link": "/admin/tickets/alumno/?estado__exact=prorroga",
                        "badge": alumnos_prorroga,
                    },
                ],
            },
            {
                "title": "Gestión de Pagos",
                "items": [
                    {
                        "title": "Todos los Pagos",
                        "icon": "receipt_long",
                        "link": "/admin/tickets/pago/",
                    },
                    {
                        "title": "Registrar Nuevo Pago",
                        "icon": "add_circle",
                        "link": "/admin/tickets/pago/add/",
                    },
                ],
            },
            {
                "title": "Administración",
                "items": [
                    {
                        "title": "Agregar Alumno",
                        "icon": "person_add",
                        "link": "/admin/tickets/alumno/add/",
                    },
                ],
            },
        ],

        # ===== ACTIVIDAD RECIENTE =====
        "recent_payments": Pago.objects.select_related("alumno").order_by("-fecha_subida")[:5],
    })

    return context