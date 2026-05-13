# Paso 14. Deteccion de nuevas vulnerabilidades

## Objetivo de aprendizaje

Usar la baseline del paso anterior para distinguir entre un hallazgo que ya existia y uno que acaba de aparecer. Sin esta distincion, el equipo no puede saber si un PR introdujo un problema nuevo o si lo que ve el scanner siempre estuvo ahi.

## Por que importa esto

Una de las fricciones mas comunes al activar SAST es que el equipo ve cientos de alertas heredadas y no sabe cuales son nuevas. Esto lleva a uno de dos comportamientos: ignorar todo porque "siempre esta rojo" o bloquear el desarrollo porque "hay demasiado que corregir".

La solucion profesional es separar la deuda heredada de los hallazgos nuevos. La baseline define el estado conocido. Todo lo que aparece encima de la baseline en un PR es nuevo y debe revisarse.

## Que vas a cambiar y por que

Añade una segunda entrada en `docs/sast-analysis.md` que represente un hallazgo nuevo: uno que no existia en la baseline inicial. La diferencia entre esta entrada y la del paso 13 debe ser visible: este hallazgo aparecio en un cambio de codigo especifico y su decision debe tomarse en ese contexto.

## Archivo y seccion que debes modificar

- Archivo objetivo: `docs/sast-analysis.md`.
- Añade una nueva entrada con los cinco campos del formato establecido.
- Identifica en el hallazgo si aparecio en un commit o PR especifico. Esa informacion da contexto para la decision.

## Cambio base recomendado

```markdown
## Hallazgo

Inyeccion de comando en src/utils.js linea 23: child_process.exec recibe input de req.body sin sanitizar.

## Regla o fuente

command-injection (rules/security-rules.yml)

## Severidad

ERROR

## Confianza

Alta — trazado desde req.body hasta exec sin validacion intermedia.

## Decision

Corregir en el PR actual: reemplazar exec por execFile con argumentos separados y validacion de allowlist.
```

## Que te esta enseñando este cambio

- Registrar el hallazgo en el contexto del PR donde aparecio (`Corregir en el PR actual`) conecta la deteccion con la oportunidad de corregir antes de fusionar.
- La trazabilidad del flujo en `## Confianza` ("trazado desde req.body hasta exec sin validacion intermedia") justifica la confianza alta. No es una opinion: es el resultado de seguir el flujo de datos.
- La distincion entre hallazgos heredados (paso 13) y hallazgos nuevos (este paso) es lo que hace que el quality gate tenga sentido: solo bloquea lo nuevo, no lo que ya existia.
- Documentar la decision en el momento del hallazgo, no semanas despues, es lo que evita que los hallazgos de severidad alta queden pendientes indefinidamente.

## Como adaptarlo correctamente

- Si el hallazgo nuevo es similar a uno de la baseline, justifica por que merece una decision distinta.
- No documentes un hallazgo como "nuevo" si ya aparecia en la baseline. Eso distorsiona las metricas del programa.
- La decision puede ser la misma que en la baseline para un tipo similar de hallazgo, pero debe escribirse de forma especifica para este contexto.
- Usa el campo `## Confianza` para indicar si el trazado del flujo fue completo o si hay incertidumbre.

## Que deberia verse al terminar

- `docs/sast-analysis.md` tiene al menos dos entradas: la baseline del paso 13 y el hallazgo nuevo de este paso.
- La nueva entrada esta claramente vinculada a un cambio de codigo, no a una deteccion heredada.
- La decision en la nueva entrada es accionable en el contexto del PR o del sprint actual.
- El documento ya separa visualmente deuda heredada de hallazgos accionables.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-14.py` comprueba este paso contra el archivo configurado.
- El workflow busca `## Hallazgo` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Regla o fuente` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Severidad` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Confianza` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Decision` dentro de `docs/sast-analysis.md`.

## Criterio de finalizacion

El paso 14 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 15.
