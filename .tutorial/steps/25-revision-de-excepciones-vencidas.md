# Paso 25. Revision de excepciones vencidas

## Objetivo de aprendizaje

Este paso introduce la revisión de excepciones vencidas y debe dejar un cambio comprensible en `docs/sast-exceptions.yml`.

## Que vas a cambiar y por que

Actualiza `docs/sast-exceptions.yml` para que las excepciones vencidas no queden olvidadas. En este paso, `expires_on:` debe leerse como disparador de revisión: cuando la fecha se alcanza, el equipo debe confirmar si corrige, renueva justificadamente o elimina la excepción.

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
    reason: Revision pendiente por caducidad
    owner: appsec-team
    expires_on: 2026-12-31
```

## Como adaptarlo correctamente

- Mantén el cambio pequeño y centrado en una sola idea por paso.
- Usa `expires_on:` como fecha de control real y no como metadato decorativo.
- Haz que `reason:` explique por qué la excepción sigue abierta y qué debe revisarse al vencer.
- Mantén `owner:` para que la revisión tenga un responsable claro.
- Evita añadir configuración que no esté relacionada con el objetivo del paso.

## Que deberia verse al terminar

- La intención del cambio se entiende leyendo el archivo.
- El archivo muestra el control sin depender de comentarios ambiguos.
- Los marcadores esperados del paso aparecen de forma natural en la configuración.
- El lector entiende que las excepciones tienen ciclo de vida y no se acumulan sin control.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-25.py` comprueba este paso contra el archivo configurado.
- El workflow busca `exceptions:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `rule_id:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `path:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `reason:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `owner:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `expires_on:` dentro de `docs/sast-exceptions.yml`.

## Criterio de finalizacion

El paso 25 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 26.
