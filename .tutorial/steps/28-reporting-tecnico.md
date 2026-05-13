# Paso 28. Reporting tecnico

## Objetivo de aprendizaje

Producir el reporte tecnico del programa SAST: el documento que usan los equipos de desarrollo para priorizar correcciones, los ingenieros de seguridad para verificar el estado de los controles y los auditores para verificar que el programa funciona como se declara.

## Por que importa esto

El reporte tecnico y el ejecutivo tienen audiencias distintas y responden preguntas distintas. El ejecutivo responde "estamos mejorando el riesgo". El tecnico responde "estos son los hallazgos especificos, estas son las reglas que los detectan, esto es el trazado del flujo de datos y esto es el plan de correccion".

Sin el reporte tecnico, el equipo de desarrollo no tiene la informacion especifica que necesita para corregir. Sin el reporte ejecutivo, el management no tiene la visibilidad que necesita para priorizar.

## Que vas a cambiar y por que

Añade en `docs/sast-analysis.md` una entrada que represente el contenido de un reporte tecnico: hallazgos con localizacion especifica, reglas que los detectaron, severidad y confianza justificadas, y plan de correccion con responsable y fecha.

## Archivo y seccion que debes modificar

- Archivo objetivo: `docs/sast-analysis.md`.
- Añade una entrada con el formato estandar del programa que represente el reporte tecnico de los hallazgos activos.

## Cambio base recomendado

```markdown
## Hallazgo

Reporte tecnico SAST — sprint 2026-05 — hallazgos activos pendientes de correccion.

Hallazgo 1: Inyeccion SQL en payments-service/src/db/queries.js L88.
Regla: sql-injection. Severidad: ERROR. Confianza: Alta (trazado desde req.body.amount hasta query sin parametrizacion).
Plan: parametrizar query con prepared statements. Responsable: equipo payments. Fecha: 2026-05-20.

Hallazgo 2: Hash debil MD5 en auth-service/src/tokens.js L89.
Regla: org-policy-no-md5-passwords. Severidad: ERROR. Confianza: Alta.
Plan: migrar a bcrypt con factor de coste 12. Responsable: equipo auth. Fecha: 2026-05-27.

## Regla o fuente

Programa SAST — resumen tecnico sprint 2026-05

## Severidad

ERROR (ambos hallazgos activos)

## Confianza

Alta en ambos casos — trazado completo disponible.

## Decision

Distribuir al tech lead de cada equipo. Bloquear release hasta que hallazgo 1 este resuelto (payments en produccion). Hallazgo 2 puede ir en el proximo sprint pero no en el siguiente release mayor.
```

## Que te esta enseñando este cambio

- Un reporte tecnico no es una lista de alertas del scanner: es una lista de hallazgos con contexto de localizacion, regla de origen, trazado de confianza y plan de correccion asignado.
- Separar los dos hallazgos con distintas decisiones de urgencia ("bloquear release" vs "proximo sprint") es lo que hace que el reporte sea accionable y no solo informativo.
- El responsable y la fecha en el plan de correccion son los elementos que convierten una observacion de seguridad en un commitment de ingenieria.
- La distincion "hallazgo 1 en produccion critica vs hallazgo 2 en autenticacion con plan de migracion" es exactamente el tipo de contexto que diferencia el reporte tecnico del ejecutivo.

## Como adaptarlo correctamente

- El reporte tecnico debe ser lo suficientemente especifico para que el desarrollador pueda ir directamente al archivo y la linea sin necesitar mas contexto.
- Incluye el trazado del flujo de datos para los hallazgos de confianza alta: es la informacion que mas reduce el tiempo de investigacion del desarrollador.
- Si hay hallazgos con confianza media o baja en el reporte, indica claramente que verificacion adicional se necesita antes de corregir.
- Este reporte es la entrada para el seguimiento del sprint: los hallazgos con fecha y responsable se convierten en tickets de trabajo en el sistema del equipo.

## Que deberia verses al terminar

- `docs/sast-analysis.md` tiene una entrada que representa un reporte tecnico con hallazgos especificos, localizacion, plan y responsable.
- Cada hallazgo tiene suficiente contexto para que el desarrollador asignado pueda actuar sin investigacion adicional.
- Las decisiones de urgencia son distintas entre hallazgos y estan justificadas por el contexto del repositorio.
- Los markers esperados del paso siguen presentes de forma natural en la configuracion.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-28.py` comprueba este paso contra el archivo configurado.
- El workflow busca `## Hallazgo` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Regla o fuente` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Severidad` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Confianza` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Decision` dentro de `docs/sast-analysis.md`.

## Criterio de finalizacion

El paso 28 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 29.
