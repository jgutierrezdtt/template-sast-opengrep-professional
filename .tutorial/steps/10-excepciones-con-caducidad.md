# Paso 10. Excepciones con caducidad

## Objetivo de aprendizaje

Este paso introduce excepciones con caducidad y debe dejar un cambio comprensible en `docs/sast-exceptions.yml`.

## Que vas a cambiar y por que

Actualiza `docs/sast-exceptions.yml` para que las excepciones no queden abiertas indefinidamente. La idea central del paso es que `expires_on:` funcione como fecha real de revisión y fuerce a confirmar si la excepción sigue justificada o debe retirarse.

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
    reason: Mitigacion temporal pendiente de cierre
    owner: appsec-team
    expires_on: 2026-12-31
```

## Como adaptarlo correctamente

- Mantén el cambio pequeño y centrado en una sola idea por paso.
- Usa `expires_on:` con una fecha concreta y verificable, no con un texto abierto.
- Haz que `reason:` explique por qué la excepción es temporal y qué debería ocurrir antes de vencer.
- Mantén `owner:` para que la revisión de caducidad tenga un responsable visible.
- Evita añadir configuración que no esté relacionada con el objetivo del paso.

## Que deberia verse al terminar

- La intención del cambio se entiende leyendo el archivo.
- El archivo muestra el control sin depender de comentarios ambiguos.
- Los marcadores esperados del paso aparecen de forma natural en la configuración.
- El lector entiende que la excepción obliga a revisión futura y no a aceptación permanente.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-10.py` comprueba este paso contra el archivo configurado.
- El workflow busca `exceptions:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `rule_id:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `path:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `reason:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `owner:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `expires_on:` dentro de `docs/sast-exceptions.yml`.

## Criterio de finalizacion

El paso 10 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 11.
