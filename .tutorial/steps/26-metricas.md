# Paso 26. Metricas

## Objetivo de aprendizaje

Definir las metricas que miden la salud del programa SAST y saber como calcularlas desde los datos que ya has generado en los pasos anteriores. Las metricas no son un fin en si mismas: son la herramienta que permite detectar tendencias y tomar decisiones basadas en datos.

## Por que importa esto

Sin metricas, el programa SAST solo genera alertas. Con metricas, el programa genera evidencia de si el riesgo esta aumentando, disminuyendo o estancado.

Las metricas correctas permiten responder preguntas reales: "el tiempo medio de resolucion de ERRORs esta mejorando", "el numero de excepciones activas lleva tres sprints creciendo sin resoluciones asociadas", "el porcentaje de hallazgos criticos en el backlog baja cada mes".

Sin esas respuestas, el programa SAST es una caja negra para los responsables de negocio.

## Que vas a cambiar y por que

Añade en `docs/sast-analysis.md` una seccion de metricas que muestre el estado actual del programa con los datos generados en los pasos anteriores. No necesitas calcular metricas en tiempo real: el objetivo es documentar que metricas son relevantes y como se calculan desde los datos disponibles.

## Archivo y seccion que debes modificar

- Archivo objetivo: `docs/sast-analysis.md`.
- Añade una seccion de metricas que calcule los indicadores clave del programa con los datos de hallazgos y excepciones ya documentados.

## Cambio base recomendado

```markdown
## Hallazgo

Metricas del programa SAST — corte Q2 2026.

## Regla o fuente

Agregado de docs/sast-analysis.md y docs/sast-exceptions.yml

## Severidad

Informativo

## Confianza

Alta — calculado desde datos documentados en este repositorio.

## Decision

Publicar como parte del reporting trimestral. Metricas a seguir:
- Total hallazgos activos: 4 (2 ERROR, 2 WARNING)
- Hallazgos resueltos en el sprint: 1
- Tiempo medio de resolucion ERRORs: 8 dias
- Excepciones activas: 1 (vence en 2026-09-30)
- Excepciones vencidas sin renovar: 0
- Cobertura de repositorios con SAST activo: 3 de 5
```

## Que te esta enseñando este cambio

- Las metricas del programa SAST tienen que calcularse desde los datos que el equipo ya mantiene, no desde herramientas externas que requieren integracion adicional. `docs/sast-analysis.md` y `docs/sast-exceptions.yml` son suficientes para las metricas basicas.
- "Excepciones vencidas sin renovar: 0" es una metrica de gobierno, no tecnica. Es la que demuestra que el proceso de revision periodica del paso 25 se esta ejecutando.
- "Cobertura de repositorios con SAST activo" conecta el inventario del paso 18 con las metricas del programa. Sin esta metrica, el programa no sabe si tiene cobertura real o parcial.
- El tiempo medio de resolucion de ERRORs es la metrica que mas interesa a los equipos de negocio: mide la velocidad de respuesta del equipo de desarrollo ante hallazgos criticos.

## Como adaptarlo correctamente

- Define las metricas que usaras antes de necesitarlas para el reporting. Una metrica que no se calcula consistentemente no es util para tendencias.
- Las metricas de cobertura (repositorios con SAST activo) son tan importantes como las de hallazgos: un programa con baja cobertura tiene metricas de hallazgos engañosamente bajas.
- Si el numero de excepciones activas lleva varios sprints creciendo sin resoluciones, eso es una señal de alarma que las metricas deben hacer visible.
- Este documento es la entrada del paso 27 (reporting ejecutivo) y del paso 28 (reporting tecnico). El reporting ejecutivo toma las metricas de impacto de negocio; el tecnico toma las metricas de cobertura y calidad de deteccion.

## Que deberia verse al terminar

- `docs/sast-analysis.md` tiene una seccion de metricas con los indicadores clave calculados.
- Las metricas cubren hallazgos activos, tiempo de resolucion, excepciones activas y cobertura de repositorios.
- El equipo puede actualizar estas metricas con cada sprint sin necesidad de herramientas adicionales.
- Los markers esperados del paso siguen presentes de forma natural en la configuracion.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-26.py` comprueba este paso contra el archivo configurado.
- El workflow busca `## Hallazgo` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Regla o fuente` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Severidad` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Confianza` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Decision` dentro de `docs/sast-analysis.md`.

## Criterio de finalizacion

El paso 26 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 27.
