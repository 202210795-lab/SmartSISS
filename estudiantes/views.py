from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def login_smart(request):

    if request.method == "POST":

        codigo = request.POST.get("codigo")
        password = request.POST.get("password")


        if codigo == "20260001" and password == "123456":

            usuario, creado = User.objects.get_or_create(
                username="20260001"
            )

            if creado:
                usuario.set_password("123456")
                usuario.save()


            login(request, usuario)

            return redirect("/")


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