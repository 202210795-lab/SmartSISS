-- Consulta del horario del estudiante

SELECT

    e.cod_sis_est AS codigo_sis,

    e.nombres_est || ' ' || e.apellidos_est AS estudiante,

    m.nombre AS materia,

    d.nombre AS docente,

    h.dia,

    h.hora_inicio,

    h.hora_fin


FROM ESTUDIANTE e


INNER JOIN INSCRIPCION i
ON e.id_estudiante = i.estudiante_id


INNER JOIN GRUPO g
ON i.grupo_id = g.id_grupos


INNER JOIN MATERIA m
ON g.materia_id = m.id_materia


INNER JOIN DOCENTE d
ON g.docente_id = d.id_docente


INNER JOIN HORARIO h
ON g.id_grupo = h.grupo_id


WHERE e.cod_sis_est = '20260001';