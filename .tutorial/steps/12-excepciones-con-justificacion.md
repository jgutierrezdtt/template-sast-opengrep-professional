# Paso 12. Excepciones con justificacion

## Objetivo de aprendizaje

Este paso introduce excepciones con justificación y debe dejar un cambio comprensible en `docs/sast-exceptions.yml`.

## Que vas a cambiar y por que

Actualiza `docs/sast-exceptions.yml` para que cada excepción tenga una justificación defendible. En este paso `reason:` es la pieza clave: debe explicar por qué el hallazgo se acepta temporalmente, qué análisis lo respalda y por qué no se trata de una omisión arbitraria.

## Archivo y seccion que debes modificar

- Archivo objetivo: `docs/sast-exceptions.yml`.
- Aplícalo en la parte del archivo que corresponde al título del paso.
- Si el archivo aún no existe, créalo con este contenido inicial y luego evoluciona desde ahí en los siguientes pasos.

## Cambio base recomendado

Este bloque no es para pegar a ciegas: úsalo como punto de partida y ajústalo al contexto del repositorio.

```yaml
exceptions:
  - rule_id: insecure-eval
    path: src/safe-eval.js
    reason: Caso revisado y acotado con compensacion documentada
    owner: appsec-team
    expires_on: 2026-12-31
```

## Como adaptarlo correctamente

- Mantén el cambio pequeño y centrado en una sola idea por paso.
- Haz que `reason:` describa el contexto y la base de la aceptación, no una frase vacía como "aprobado".
- Mantén `rule_id:` y `path:` para que la justificación quede unida al hallazgo concreto.
- Conserva `owner:` y `expires_on:` porque una buena justificación sigue necesitando responsable y revisión futura.
- Evita añadir configuración que no esté relacionada con el objetivo del paso.

## Que deberia verse al terminar

- La intención del cambio se entiende leyendo el archivo.
- El archivo muestra el control sin depender de comentarios ambiguos.
- Los marcadores esperados del paso aparecen de forma natural en la configuración.
- El lector entiende por qué la excepción existe y qué análisis la sostiene.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-12.py` comprueba este paso contra el archivo configurado.
- El workflow busca `exceptions:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `rule_id:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `path:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `reason:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `owner:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `expires_on:` dentro de `docs/sast-exceptions.yml`.

## Criterio de finalizacion

El paso 12 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 13.
