from django.contrib import admin
from .models import (
    Facultad,
    Carrera,
    Estudiante,
    Docente,
    Materia,
    Grupo,
    Horario,
    Inscripcion,
    Kardex
)


@admin.register(Facultad)
class FacultadAdmin(admin.ModelAdmin):
    list_display = ("id_facultad", "nombre")


@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
    list_display = ("id_carrera", "nombre", "facultad")


@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = (
        "cod_sis_est",
        "nombres_est",
        "apellidos_est",
        "carrera",
        "estado"
    )


@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = (
        "id_docente",
        "nombres_doc",
        "apellidos_doc",
        "correo"
    )


@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = (
        "id_materia",
        "nombre",
        "creditos",
        "docente"
    )


@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = (
        "id_grupo",
        "nombre_grupo",
        "materia",
        "docente",
        "cupo"
    )


@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = (
        "id_horario",
        "grupo",
        "dia",
        "hora_inicio",
        "hora_fin",
        "aula"
    )


@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = (
        "id_inscripcion",
        "estudiante",
        "grupo",
        "fecha_inscripcion",
        "estado"
    )


@admin.register(Kardex)
class KardexAdmin(admin.ModelAdmin):
    list_display = (
        "id_kardex",
        "inscripcion",
        "gestion",
        "periodo",
        "nota_final"
    )