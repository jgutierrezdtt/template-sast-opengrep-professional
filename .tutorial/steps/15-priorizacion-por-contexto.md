# Paso 15. Priorizacion por contexto

## Objetivo de aprendizaje

Este paso introduce la priorización por contexto y debe dejar un cambio comprensible en `docs/sast-analysis.md`.

## Que vas a cambiar y por que

Actualiza `docs/sast-analysis.md` para que la priorización no dependa solo de la coincidencia técnica. En este paso debes usar el contexto del repositorio, la función del código afectado y la exposición del flujo para decidir qué hallazgos requieren atención antes que otros.

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
- Usa `## Regla o fuente` y `## Hallazgo` para describir la señal técnica, pero reserva `## Decision` para la prioridad contextual.
- Usa `## Severidad` y `## Confianza` como apoyo, no como único criterio de decisión.
- Haz que `## Decision` refleje por qué el hallazgo importa más o menos en ese repositorio concreto.
- Evita añadir configuración que no esté relacionada con el objetivo del paso.

## Que deberia verse al terminar

- La intención del cambio se entiende leyendo el archivo.
- El archivo muestra el control sin depender de comentarios ambiguos.
- Los marcadores esperados del paso aparecen de forma natural en la configuración.
- El documento ya ayuda a ordenar hallazgos con criterio de negocio y arquitectura local.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-15.py` comprueba este paso contra el archivo configurado.
- El workflow busca `## Hallazgo` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Regla o fuente` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Severidad` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Confianza` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Decision` dentro de `docs/sast-analysis.md`.

## Criterio de finalizacion

El paso 15 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 16.
