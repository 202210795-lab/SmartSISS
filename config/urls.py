"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from estudiantes.views import (
    inicio,
    login_smart,
    kardex_estudiante,
    inscripcion,
    mis_inscripciones,
    perfil_estudiante,
    gestion_academica,
    seleccion_materias,
    confirmacion_inscripcion,
    inscripcion_completada,
    validacion_periodo,
    plan_academico,
    validacion_requisitos,
    seleccion_grupo,
    horario_aula,
    pago_matricula,
    resumen_inscripcion,
    cerrar_sesion,
)


urlpatterns = [

    path('admin/', admin.site.urls),

    # Inicio
    path(
        '',
        inicio,
        name='inicio'
    ),

    # Login estudiante
    path(
        'login/',
        login_smart,
        name='login'
    ),

    # Perfil estudiante
    path(
        'perfil/',
        perfil_estudiante,
        name='perfil_estudiante'
    ),

    # Gestión Académica
    path(
        'gestion/',
        gestion_academica,
        name='gestion_academica'
    ),

    # Selección de Materias
    path(
        'seleccion-materias/',
        seleccion_materias,
        name='seleccion_materias'
    ),
    # Confirmacion Inscripcion
    path(
    'confirmacion/',
    confirmacion_inscripcion,
    name='confirmacion_inscripcion'
    ),
    # Inscripcion Completada
    path(
    'inscripcion-completada/',
    inscripcion_completada,
    name='inscripcion_completada'
    ),
    # Inscripción de materias
    path(
        'inscripcion/',
        inscripcion,
        name='inscripcion'
    ),

    # Materias inscritas
    path(
        'mis-inscripciones/',
        mis_inscripciones,
        name='mis_inscripciones'
    ),

    # Kardex académico
    path(
        'kardex/',
        kardex_estudiante,
        name='kardex'
    ),
    path(
    'validacion-periodo/',
    validacion_periodo,
    name='validacion_periodo'
    ),

    path(
    'plan-academico/',
    plan_academico,
    name='plan_academico'
     ),

    path(
    'validacion-requisitos/',
    validacion_requisitos,
    name='validacion_requisitos'
    ),

path(
    'seleccion-grupo/',
    seleccion_grupo,
    name='seleccion_grupo'
),

path(
    'horario-aula/',
    horario_aula,
    name='horario_aula'
),

path(
    'pago-matricula/',
    pago_matricula,
    name='pago_matricula'
),

path(
    'resumen-inscripcion/',
    resumen_inscripcion,

    name='resumen_inscripcion'
),
path(
    'cerrar-sesion/',
    cerrar_sesion,
    name='cerrar_sesion'
),

]