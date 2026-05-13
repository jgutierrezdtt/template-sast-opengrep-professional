# Paso 8. Falso positivo documentado

## Objetivo de aprendizaje

Este paso introduce el falso positivo documentado y debe dejar un cambio comprensible en `docs/sast-exceptions.yml`.

## Que vas a cambiar y por que

Actualiza `docs/sast-exceptions.yml` para que un falso positivo quede explícito, trazable y revisable. En un programa SAST serio no basta con ignorar una alerta: debes dejar qué regla la disparó, en qué ruta ocurrió, por qué se considera falso positivo, quién responde por esa decisión y hasta cuándo se mantiene válida.

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
    reason: Uso controlado y revisado como falso positivo
    owner: appsec-team
    expires_on: 2026-12-31
```

## Como adaptarlo correctamente

- Mantén el cambio pequeño y centrado en una sola idea por paso.
- Usa `rule_id:` para vincular la excepción con la regla concreta que produjo el hallazgo.
- Usa `reason:` para justificar por qué el match no representa riesgo real en ese caso.
- Mantén `owner:` y `expires_on:` para que el falso positivo siga siendo revisable y no quede oculto para siempre.
- Evita añadir configuración que no esté relacionada con el objetivo del paso.

## Que deberia verse al terminar

- La intención del cambio se entiende leyendo el archivo.
- El archivo muestra el control sin depender de comentarios ambiguos.
- Los marcadores esperados del paso aparecen de forma natural en la configuración.
- El lector entiende que la alerta se acepta por análisis, no por simple descarte manual.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-08.py` comprueba este paso contra el archivo configurado.
- El workflow busca `exceptions:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `rule_id:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `path:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `reason:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `owner:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `expires_on:` dentro de `docs/sast-exceptions.yml`.

## Criterio de finalizacion

El paso 8 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 9.
