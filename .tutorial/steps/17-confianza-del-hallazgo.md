# Paso 17. Confianza del hallazgo

## Objetivo de aprendizaje

Este paso introduce la confianza del hallazgo y debe dejar un cambio comprensible en `docs/sast-analysis.md`.

## Que vas a cambiar y por que

Actualiza `docs/sast-analysis.md` para que la confianza del hallazgo quede explícita y revisable. Este paso sirve para recordar que no toda coincidencia encontrada por una regla merece la misma credibilidad: la confianza influye en la validación manual, en la urgencia y en la forma de comunicar el hallazgo.

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
- Usa `## Confianza` para reflejar si el match es sólido, probable o todavía ambiguo.
- Haz que `## Decision` cambie en función de esa confianza: validar, investigar, remediar o ajustar la regla.
- Mantén visibles `## Hallazgo` y `## Regla o fuente` para que la confianza pueda relacionarse con el origen concreto del match.
- Evita añadir configuración que no esté relacionada con el objetivo del paso.

## Que deberia verse al terminar

- La intención del cambio se entiende leyendo el archivo.
- El archivo muestra el control sin depender de comentarios ambiguos.
- Los marcadores esperados del paso aparecen de forma natural en la configuración.
- El lector entiende cómo la confianza altera la respuesta operativa al hallazgo.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-17.py` comprueba este paso contra el archivo configurado.
- El workflow busca `## Hallazgo` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Regla o fuente` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Severidad` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Confianza` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Decision` dentro de `docs/sast-analysis.md`.

## Criterio de finalizacion

El paso 17 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 18.
