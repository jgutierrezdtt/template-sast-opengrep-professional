# Paso 15. Priorizacion por contexto

## Objetivo de aprendizaje

Dejar por escrito cómo se interpreta un hallazgo y qué decisión se toma con él.

## Archivo y seccion que debes modificar

- Archivo objetivo: `docs/sast-analysis.md`.
- Seccion donde aplicar el cambio: documento de análisis del programa SAST.
- Resultado esperado: el repositorio incorpora el control de este paso de forma legible y revisable.

## Cambio que debes introducir

Copia este bloque como base y adáptalo al contexto real del repositorio:

```markdown
## Hallazgo
## Regla o fuente
## Severidad
## Confianza
## Decision
```

## Como adaptarlo correctamente

- Usa ejemplos reales de hallazgos del repositorio.
- Diferencia severidad técnica y prioridad operativa cuando no coincidan.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-15.py` comprueba el archivo y los marcadores esperados de este paso.
- Debe encontrar el marcador `## Hallazgo` en `docs/sast-analysis.md`.
- Debe encontrar el marcador `## Regla o fuente` en `docs/sast-analysis.md`.
- Debe encontrar el marcador `## Severidad` en `docs/sast-analysis.md`.
- Debe encontrar el marcador `## Confianza` en `docs/sast-analysis.md`.
- Debe encontrar el marcador `## Decision` en `docs/sast-analysis.md`.

## Criterio de finalizacion

El paso 15 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 16.
