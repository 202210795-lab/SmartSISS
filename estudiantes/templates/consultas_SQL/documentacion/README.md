# SmartSISS
## Sistema Inteligente de Servicios de Información del Sistema Superior

---

# 1. Descripción del Sistema

SmartSISS es un sistema web académico desarrollado para gestionar procesos universitarios relacionados con estudiantes, materias, inscripción y consulta del historial académico.

El sistema permite a los estudiantes consultar la oferta académica disponible, realizar la inscripción de materias y generar su Kardex académico.

---

# 2. Objetivo del Proyecto

Desarrollar una aplicación web que permita automatizar procesos académicos mediante una base de datos relacional y una interfaz sencilla para estudiantes y administradores.

---

# 3. Tecnologías utilizadas

- Python
- Django
- SQLite
- HTML
- CSS
- Django Templates

---

# 4. Módulos implementados

## 4.1 Gestión de estudiantes

Permite almacenar la información principal del estudiante:

- Código SIS
- Nombres
- Apellidos
- Carrera

---

## 4.2 Inscripción de materias

El estudiante puede visualizar materias disponibles e inscribirse.

Información mostrada:

- Grupo
- Materia
- Docente
- Créditos
- Cupo

El sistema valida que un estudiante no pueda registrarse dos veces en la misma materia.

---

## 4.3 Mis materias inscritas

Permite consultar las asignaturas registradas por el estudiante.

Muestra:

- Grupo
- Materia
- Docente
- Créditos
- Estado de inscripción

---

## 4.4 Kardex académico

Permite consultar el historial académico del estudiante.

Información mostrada:

- Código SIS
- Estudiante
- Materia
- Créditos
- Gestión
- Periodo
- Nota final

---

# 5. Base de Datos

Las principales entidades utilizadas son:

- ESTUDIANTE
- DOCENTE
- MATERIA
- GRUPO
- HORARIO
- INSCRIPCION
- KARDEX

---

# 6. Consultas SQL

El proyecto contiene consultas SQL para:

- Consulta de materias disponibles para inscripción.
- Consulta de Kardex académico.
- Consulta de horarios del estudiante.

---

# 7. Resultado Final

SmartSISS permite gestionar de manera integrada los procesos académicos principales:

1. Visualización de oferta académica.
2. Inscripción de materias.
3. Consulta de materias inscritas.
4. Generación de Kardex académico.

---

# 8. Conclusión

El desarrollo de SmartSISS permitió implementar un sistema académico funcional utilizando Django y una base de datos relacional, aplicando relaciones entre entidades y consultas SQL para la gestión de información universitaria.