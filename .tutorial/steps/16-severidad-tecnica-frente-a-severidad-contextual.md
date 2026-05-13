# Paso 16. Severidad tecnica frente a severidad contextual

## Objetivo de aprendizaje

Este paso introduce la diferencia entre severidad técnica y severidad contextual y debe dejar un cambio comprensible en `docs/sast-analysis.md`.

## Que vas a cambiar y por que

Actualiza `docs/sast-analysis.md` para que el análisis no trate la severidad técnica como verdad absoluta. En este paso la idea es usar `## Severidad`, `## Confianza` y `## Decision` para mostrar que un hallazgo puede ser técnicamente grave, pero necesitar matices según exposición real, controles compensatorios o criticidad del componente afectado.

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
- Usa `## Severidad` para reflejar la gravedad técnica detectada por la regla o el análisis.
- Usa `## Decision` para explicar cómo cambia la prioridad cuando se introduce el contexto real del sistema.
- Mantén `## Confianza` visible porque una severidad alta con baja confianza requiere una lectura diferente.
- Evita añadir configuración que no esté relacionada con el objetivo del paso.

## Que deberia verse al terminar

- La intención del cambio se entiende leyendo el archivo.
- El archivo muestra el control sin depender de comentarios ambiguos.
- Los marcadores esperados del paso aparecen de forma natural en la configuración.
- El lector entiende por qué la respuesta final no depende solo de una etiqueta de severidad técnica.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-16.py` comprueba este paso contra el archivo configurado.
- El workflow busca `## Hallazgo` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Regla o fuente` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Severidad` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Confianza` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Decision` dentro de `docs/sast-analysis.md`.

## Criterio de finalizacion

El paso 16 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 17.
