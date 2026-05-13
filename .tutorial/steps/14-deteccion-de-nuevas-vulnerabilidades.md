# Paso 14. Deteccion de nuevas vulnerabilidades

## Objetivo de aprendizaje

Este paso introduce la detección de nuevas vulnerabilidades y debe dejar un cambio comprensible en `docs/sast-analysis.md`.

## Que vas a cambiar y por que

Actualiza `docs/sast-analysis.md` para que el análisis ayude a distinguir hallazgos nuevos frente a deuda ya conocida. En este paso la clave está en que `## Decision` y el resto de secciones permitan comparar el resultado actual con el baseline y detectar cuándo aparece un problema que antes no estaba registrado.

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
- Usa `## Hallazgo` y `## Regla o fuente` con precisión suficiente para comparar contra ejecuciones previas.
- Usa `## Confianza` para distinguir una señal nueva sólida de un match que todavía requiere revisión.
- Haz que `## Decision` deje claro si el hallazgo es nuevo, regresivo o ya conocido.
- Evita añadir configuración que no esté relacionada con el objetivo del paso.

## Que deberia verse al terminar

- La intención del cambio se entiende leyendo el archivo.
- El archivo muestra el control sin depender de comentarios ambiguos.
- Los marcadores esperados del paso aparecen de forma natural en la configuración.
- El documento ya puede utilizarse para separar vulnerabilidades nuevas de hallazgos heredados.

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
