# Paso 19. Escaneo organizativo simulado

## Objetivo de aprendizaje

Simular como se veria el estado SAST de una cartera de repositorios y entender que decisiones de gobierno emergen cuando tienes visibilidad agregada en lugar de solo por repositorio.

## Por que importa esto

Cuando tienes SAST en un solo repositorio ves los hallazgos de ese repositorio. Cuando tienes SAST en veinte repositorios, la pregunta ya no es "cuantos hallazgos hay" sino "en que repositorios se concentra el riesgo real", "cuales tienen mas hallazgos criticos sin resolver", "cuales no han ejecutado el scanner en los ultimos 30 dias".

La diferencia entre gestionar un repositorio y gestionar un programa es que el programa necesita visibilidad agregada para tomar decisiones de priorizacion a escala.

## Que vas a cambiar y por que

Añade en `docs/sast-analysis.md` entradas que representen hallazgos de multiples repositorios simulados. El objetivo es que el documento empiece a reflejar como se ve un analisis organizativo, no solo el analisis de un repositorio aislado.

## Archivo y seccion que debes modificar

- Archivo objetivo: `docs/sast-analysis.md`.
- Añade entradas que representen repositorios distintos con hallazgos distintos.
- Usa el campo `## Hallazgo` para identificar el repositorio de origen.

## Cambio base recomendado

```markdown
## Hallazgo

Repositorio payments-service: inyeccion SQL en src/db/queries.js linea 88. Servicio de pagos en produccion con acceso a base de datos de transacciones.

## Regla o fuente

sql-injection (rules/security-rules.yml)

## Severidad

ERROR

## Confianza

Alta — input desde req.body.amount directamente interpolado en query SQL sin parametrizacion.

## Decision

Prioridad critica: payments-service maneja datos financieros en produccion. Correccion bloqueante para el proximo release. Se crea ticket de seguridad P1 y se asigna al equipo de payments.
```

## Que te esta enseñando este cambio

- Identificar el repositorio de origen en el campo `## Hallazgo` es lo que convierte un hallazgo aislado en un dato de un programa organizativo. Sin ese contexto, no sabes si el hallazgo es critico o menor.
- La combinacion "servicio de pagos en produccion con acceso a datos financieros" en el hallazgo es el contexto que justifica la prioridad critica aunque la regla y el patron sean los mismos que en otros repositorios.
- Una decision de "bloqueante para el proximo release" es operativamente especifica: no es "corregir algun dia", es un criterio de aceptacion para el siguiente deploy.
- Este tipo de entrada es la base del dashboard del paso 25 y del reporting ejecutivo del paso 27.

## Como adaptarlo correctamente

- Para cada repositorio simulado, usa un contexto de negocio diferente: esto es lo que hace que el escaneo organizativo sea util, no repetir el mismo hallazgo con distintos nombres.
- El campo `## Decision` en un escaneo organizativo debe incluir a quien se asigna la resolucion: el programa SAST necesita que las decisiones lleguen al equipo que puede actuar.
- Simula al menos un repositorio con baja criticidad donde el mismo tipo de hallazgo tiene menor urgencia: eso ilustra como el contexto organizativo cambia las prioridades.
- Este paso es la preparacion para los pasos de quality gate (20-23) donde tendras que decidir a que nivel bloquear el pipeline.

## Que deberia verse al terminar

- `docs/sast-analysis.md` tiene entradas que representan al menos dos repositorios distintos con contextos de negocio diferentes.
- Las decisiones reflejan la diferencia de prioridad segun el contexto organizativo de cada repositorio.
- El documento empieza a mostrar un patron de como un programa SAST prioriza a escala organizativa.
- Los marcadores esperados del paso siguen presentes de forma natural en la configuracion.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-19.py` comprueba este paso contra el archivo configurado.
- El workflow busca `## Hallazgo` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Regla o fuente` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Severidad` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Confianza` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Decision` dentro de `docs/sast-analysis.md`.

## Criterio de finalizacion

El paso 19 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 20.
