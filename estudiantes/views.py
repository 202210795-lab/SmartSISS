from django.shortcuts import render, redirect
from .models import Grupo, Inscripcion, Estudiante, Kardex


def kardex_estudiante(request):

    registros = Kardex.objects.select_related(
        "inscripcion__estudiante",
        "inscripcion__grupo__materia"
    )

    estudiante = registros.first().inscripcion.estudiante if registros.exists() else None

    contexto = {
        "kardex": registros,
        "estudiante": estudiante
    }

    return render(
        request,
        "kardex.html",
        contexto
    )



def inscripcion(request):

    grupos = Grupo.objects.all()

    mensaje = ""

    if request.method == "POST":

        print("ENTRO AL POST DE INSCRIPCION")

        grupo_id = request.POST.get("grupo_id")

        grupo = Grupo.objects.get(
            id_grupo=grupo_id
        )

        estudiante = Estudiante.objects.get(
            cod_sis_est="20260001"
        )

        existe = Inscripcion.objects.filter(
            estudiante=estudiante,
            grupo=grupo
        ).exists()


        if existe:
            mensaje = "El estudiante ya está inscrito en esta materia"

        else:
            Inscripcion.objects.create(
                estudiante=estudiante,
                grupo=grupo
            )

            mensaje = "Inscripción realizada correctamente"


    return render(
        request,
        "inscripcion.html",
        {
            "grupos": grupos,
            "mensaje": mensaje
        }
    )

def mis_inscripciones(request):

    estudiante = Estudiante.objects.first()

    registros = Inscripcion.objects.filter(
        estudiante=estudiante
    )

    return render(
        request,
        "mis_inscripciones.html",
        {
            "inscripciones": registros
        }
    )
def inicio(request):

    return render(
        request,
        "inicio.html"
    )
def login_smart(request):

    if request.method == "POST":

        codigo = request.POST.get("codigo")
        password = request.POST.get("password")


        if codigo == "20260001" and password == "123456":

              return redirect(
                   "/"
        )
            


        else:

            return render(
                request,
                "login.html",
                {
                    "mensaje": "Código SIS o contraseña incorrectos"
                }
            )


    return render(
        request,
        "login.html"
    )
def perfil_estudiante(request):

    estudiante = Estudiante.objects.first()

    return render(
        request,
        "perfil_estudiante.html",
        {
            "estudiante": estudiante
        }
    )

def gestion_academica(request):

    return render(
        request,
        "gestion_academica.html"
    )
def seleccion_materias(request):

    grupos = Grupo.objects.all()


    if request.method == "POST":

        seleccionados = request.POST.getlist("grupos")


        request.session["grupos_seleccionados"] = seleccionados


        return redirect(
            "/confirmacion/"
        )


    return render(
        request,
        "seleccion_materias.html",
        {
            "grupos": grupos
        }
    )
def confirmacion_inscripcion(request):

    estudiante = Estudiante.objects.first()


    ids_grupos = request.session.get(
        "grupos_seleccionados",
        []
    )


    grupos = Grupo.objects.filter(
        id_grupo__in=ids_grupos
    )


    if request.method == "POST":

        for grupo in grupos:

            existe = Inscripcion.objects.filter(
                estudiante=estudiante,
                grupo=grupo
            ).exists()


            if not existe:

                Inscripcion.objects.create(
                    estudiante=estudiante,
                    grupo=grupo
                )


        return redirect(
            "/inscripcion-completada/"
        )


    return render(
        request,
        "confirmacion_inscripcion.html",
        {
            "estudiante": estudiante,
            "grupos": grupos
        }
    )
def inscripcion_completada(request):

    estudiante = Estudiante.objects.first()

    grupos = Grupo.objects.all()


    return render(
        request,
        "inscripcion_completada.html",
        {
            "estudiante": estudiante,
            "grupos": grupos
        }
    )
def validacion_periodo(request):

    return render(
        request,
        "validacion_periodo.html"
    )



def plan_academico(request):

    return render(
        request,
        "plan_academico.html"
    )



def validacion_requisitos(request):

    return render(
        request,
        "validacion_requisitos.html"
    )



def seleccion_grupo(request):

    return render(
        request,
        "seleccion_grupo.html"
    )



def horario_aula(request):

    return render(
        request,
        "horario_aula.html"
    )



def pago_matricula(request):

    return render(
        request,
        "pago_matricula.html"
    )



def resumen_inscripcion(request):

    return render(
        request,
        "resumen_inscripcion.html"
    )
from django.contrib.auth import logout

def cerrar_sesion(request):

    logout(request)

    return redirect('/login/')