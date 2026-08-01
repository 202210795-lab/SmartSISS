-- Consulta del Kardex Académico del estudiante

SELECT

    e.cod_sis_est AS codigo_sis,

    e.nombres_est || ' ' || e.apellidos_est AS estudiante,

    m.nombre AS materia,

    m.creditos,

    k.gestion,

    k.periodo,

    k.nota_final


FROM ESTUDIANTE e


INNER JOIN INSCRIPCION i
ON e.id_estudiante = i.estudiante_id


INNER JOIN GRUPO g
ON i.grupo_id = g.id_grupo


INNER JOIN MATERIA m
ON g.materia_id = m.id_materia


INNER JOIN KARDEX k
ON i.id_inscripcion = k.inscripcion_id


WHERE e.cod_sis_est = '20260001';