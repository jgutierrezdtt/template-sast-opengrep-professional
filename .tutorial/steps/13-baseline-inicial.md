# Paso 13. Baseline inicial

## Objetivo de aprendizaje

Este paso introduce el baseline inicial y debe dejar un cambio comprensible en `docs/sast-analysis.md`.

## Que vas a cambiar y por que

Actualiza `docs/sast-analysis.md` para que el análisis sirva como línea base. En este paso no solo registras un hallazgo, sino una referencia desde la que luego podrás comparar nuevas ejecuciones, distinguir deuda existente de hallazgos nuevos y sostener decisiones de priorización.

## Archivo y seccion que debes modificar

- Archivo objetivo: `docs/sast-analysis.md`.
- Aplícalo en la parte del archivo que corresponde al título del paso.
- Si el archivo aún no existe, créalo con este contenido inicial y luego evoluciona desde ahí en los siguientes pasos.

## Cambio base recomendado

Este bloque no es para pegar a ciegas: úsalo como punto de partida y ajústalo al contexto del repositorio.

```markdown
## Hallazgo
## Regla o fuente
## Severidad
## Confianza
## Decision
```

## Como adaptarlo correctamente

- Mantén el cambio pequeño y centrado en una sola idea por paso.
- Usa `## Hallazgo` y `## Regla o fuente` para describir de forma estable qué se detectó y qué lo originó.
- Usa `## Severidad` y `## Confianza` para que futuras comparaciones mantengan el mismo marco de lectura.
- Haz que `## Decision` indique si el hallazgo forma parte de la línea base aceptada, pendiente o priorizada.
- Evita añadir configuración que no esté relacionada con el objetivo del paso.

## Que deberia verse al terminar

- La intención del cambio se entiende leyendo el archivo.
- El archivo muestra el control sin depender de comentarios ambiguos.
- Los marcadores esperados del paso aparecen de forma natural en la configuración.
- El documento ya puede servir como referencia para medir evolución del programa SAST.

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
