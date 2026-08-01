from django.db import models


class Facultad(models.Model):
    id_facultad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    class Meta:
        db_table = "FACULTAD"

    def __str__(self):
        return self.nombre


class Carrera(models.Model):
    id_carrera = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    facultad = models.ForeignKey(
        Facultad,
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = "CARRERA"

    def __str__(self):
        return self.nombre


class Estudiante(models.Model):
    cod_sis_est = models.CharField(
        max_length=20,
        primary_key=True
    )

    nombres_est = models.CharField(max_length=100)

    apellidos_est = models.CharField(max_length=100)

    carrera = models.ForeignKey(
        Carrera,
        on_delete=models.CASCADE
    )

    estado = models.CharField(
        max_length=20,
        default="Activo"
    )

    class Meta:
        db_table = "ESTUDIANTE"

    def __str__(self):
        return self.nombres_est + " " + self.apellidos_est


class Docente(models.Model):
    id_docente = models.AutoField(primary_key=True)

    nombres_doc = models.CharField(max_length=100)

    apellidos_doc = models.CharField(max_length=100)

    correo = models.EmailField()

    class Meta:
        db_table = "DOCENTE"

    def __str__(self):
        return self.nombres_doc + " " + self.apellidos_doc

class Materia(models.Model):
    id_materia = models.AutoField(primary_key=True)

    nombre = models.CharField(max_length=100)

    creditos = models.IntegerField()

    docente = models.ForeignKey(
        Docente,
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = "MATERIA"

    def __str__(self):
        return self.nombre

class Grupo(models.Model):

    id_grupo = models.AutoField(primary_key=True)

    nombre_grupo = models.CharField(max_length=10)

    materia = models.ForeignKey(
        Materia,
        on_delete=models.CASCADE
    )

    docente = models.ForeignKey(
        Docente,
        on_delete=models.CASCADE
    )

    cupo = models.IntegerField(default=40)

    class Meta:
        db_table = "GRUPO"

    def __str__(self):
        return self.nombre_grupo

class Horario(models.Model):

    id_horario = models.AutoField(primary_key=True)

    grupo = models.ForeignKey(
        Grupo,
        on_delete=models.CASCADE
    )

    dia = models.CharField(max_length=20)

    hora_inicio = models.TimeField()

    hora_fin = models.TimeField()

    aula = models.CharField(max_length=20)

    class Meta:
        db_table = "HORARIO"

    def __str__(self):
        return self.dia

class Inscripcion(models.Model):

    id_inscripcion = models.AutoField(primary_key=True)

    estudiante = models.ForeignKey(
        Estudiante,
        on_delete=models.CASCADE
    )

    grupo = models.ForeignKey(
        Grupo,
        on_delete=models.CASCADE
    )

    fecha_inscripcion = models.DateField(
        auto_now_add=True
    )

    estado = models.CharField(
        max_length=20,
        default="Activo"
    )

    class Meta:
        db_table = "INSCRIPCION"

    def __str__(self):
        return str(self.estudiante)

class Kardex(models.Model):

    id_kardex = models.AutoField(primary_key=True)

    inscripcion = models.ForeignKey(
        Inscripcion,
        on_delete=models.CASCADE
    )

    gestion = models.IntegerField()

    periodo = models.CharField(
        max_length=10
    )

    nota_final = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    class Meta:
        db_table = "KARDEX"

    def __str__(self):
        return str(self.inscripcion)