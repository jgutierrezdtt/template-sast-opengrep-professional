# Paso 18. Inventario de repositorios

## Objetivo de aprendizaje

Este paso introduce el inventario de repositorios y debe dejar un cambio comprensible en `docs/sast-analysis.md`.

## Que vas a cambiar y por que

Actualiza `docs/sast-analysis.md` para que el análisis pueda escalar a varios repositorios. En este paso la idea es que `## Regla o fuente`, `## Severidad`, `## Confianza` y `## Decision` se lean ya como parte de un inventario donde distintas señales SAST deben compararse, agruparse y gestionarse a nivel de cartera.

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
- Usa `## Regla o fuente` para que el inventario permita comparar qué reglas aportan más valor o más ruido.
- Mantén `## Hallazgo` y `## Decision` con suficiente consistencia para poder ordenar resultados entre repositorios.
- Usa `## Severidad` y `## Confianza` como atributos comparables dentro del inventario.
- Evita añadir configuración que no esté relacionada con el objetivo del paso.

## Que deberia verse al terminar

- La intención del cambio se entiende leyendo el archivo.
- El archivo muestra el control sin depender de comentarios ambiguos.
- Los marcadores esperados del paso aparecen de forma natural en la configuración.
- El documento ya puede apoyar una vista agregada de hallazgos entre repositorios.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-18.py` comprueba este paso contra el archivo configurado.
- El workflow busca `## Hallazgo` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Regla o fuente` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Severidad` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Confianza` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Decision` dentro de `docs/sast-analysis.md`.

## Criterio de finalizacion

El paso 18 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 19.
