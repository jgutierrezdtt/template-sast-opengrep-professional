# Paso 13. Baseline inicial

## Objetivo de aprendizaje

Crear el primer registro formal de hallazgos en `docs/sast-analysis.md`. Este documento es la linea base contra la que se mediran todos los hallazgos futuros: sin el, no hay forma de saber si el programa SAST esta mejorando o acumulando deuda.

## Por que importa esto

Cuando un equipo activa SAST por primera vez en un repositorio existente, normalmente aparecen decenas de hallazgos. La reaccion habitual es intentar corregirlos todos a la vez o ignorarlos colectivamente. Las dos son malas opciones.

El enfoque profesional es crear una baseline: registrar el estado inicial de forma estructurada, priorizar cuales merecen atencion inmediata y tratar el resto como deuda conocida que se ira reduciendo con cada sprint.

Sin una baseline, el equipo no puede distinguir entre un hallazgo nuevo y uno que llevaba meses en el codigo.

## Que vas a cambiar y por que

Crea la primera entrada en `docs/sast-analysis.md` con el formato de analisis: hallazgo, regla o fuente, severidad, confianza y decision. Aunque sea un solo hallazgo, este documento establece el patron que usaras para todos los demas.

La decision tomada en cada entrada es tan importante como el hallazgo mismo: documenta si vas a corregirlo, si es una excepcion justificada o si se acepta como riesgo conocido.

## Archivo y seccion que debes modificar

- Archivo objetivo: `docs/sast-analysis.md`.
- Si el archivo no existe, créalo con la primera entrada de analisis.
- Usa el formato de cabeceras `## Hallazgo`, `## Regla o fuente`, `## Severidad`, `## Confianza`, `## Decision` para que el proceso de validacion automatica lo reconozca.

## Cambio base recomendado

```markdown
## Hallazgo

Uso inseguro de eval en src/app.js linea 47.

## Regla o fuente

insecure-eval (rules/security-rules.yml)

## Severidad

ERROR

## Confianza

Alta — el argumento proviene directamente de req.query.

## Decision

Corregir: reemplazar eval por una funcion especifica que procese solo los valores esperados.
```

## Que te esta enseñando este cambio

- `## Hallazgo` describe el problema concreto: archivo, linea, contexto. No es un resumen de la regla sino del codigo real.
- `## Regla o fuente` vincula el hallazgo al control que lo detecto. Si la regla cambia o se retira, sabes que entradas del analisis quedan sin cobertura.
- `## Severidad` hereda la severidad de la regla pero puede ajustarse por contexto. Un ERROR en un servicio interno puede tener distinta urgencia que en una API publica.
- `## Confianza` es el campo que mas valor aporta despues de la severidad: indica si el hallazgo es un caso real, un posible falso positivo o una deteccion probable pero no confirmada. Sin este campo, todos los hallazgos parecen iguales.
- `## Decision` es el compromiso del equipo con ese hallazgo especifico: corregir, excepcionar con justificacion, o aceptar como riesgo conocido con fecha de revision.

## Como adaptarlo correctamente

- No registres solo los hallazgos criticos en la baseline. Los de severidad media son los que mas se acumulan con el tiempo.
- Un hallazgo sin decision pendiente no pertenece a la baseline: o se corrige o se documenta la excepcion.
- La confianza no es una opinion subjetiva: se basa en el analisis del flujo de datos entre la entrada del hallazgo y la fuente del riesgo.
- Este documento evolucionara con cada sprint. Diseñalo para que sea legible en seis meses, no solo hoy.

## Que deberia verse al terminar

- `docs/sast-analysis.md` existe y tiene al menos una entrada completa con los cinco campos.
- La entrada describe un hallazgo real o realista del repositorio, no solo un ejemplo de plantilla.
- La decision tomada es especifica: no "pendiente" sin contexto sino una accion concreta o una aceptacion justificada.
- El documento puede servir como punto de partida para medir la reduccion de hallazgos en sprints futuros.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-13.py` comprueba este paso contra el archivo configurado.
- El workflow busca `## Hallazgo` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Regla o fuente` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Severidad` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Confianza` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Decision` dentro de `docs/sast-analysis.md`.

## Criterio de finalizacion

El paso 13 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 14.
