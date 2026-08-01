-- Consulta de materias disponibles para inscripción

SELECT
    g.id_grupo,
    g.nombre_grupo AS grupo,
    m.nombre AS materia,
    d.nombre AS docente,
    m.creditos,
    g.cupo

FROM GRUPO g

INNER JOIN MATERIA m
ON g.materia_id = m.id_materia

INNER JOIN DOCENTE d
ON g.docente_id = d.id_docente;