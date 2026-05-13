# Paso 24. Reglas prohibidas por organizacion

## Objetivo de aprendizaje

Este paso introduce las reglas prohibidas por organización y debe dejar un cambio comprensible en `rules/security-rules.yml`.

## Que vas a cambiar y por que

Actualiza `rules/security-rules.yml` para que una prohibición organizativa quede explícita y revisable. En este paso la regla `insecure-eval` deja de verse solo como patrón técnico y pasa a representar una norma corporativa: ciertos usos no están permitidos en ningún repositorio salvo justificación y revisión formal.

## Archivo y seccion que debes modificar

- Archivo objetivo: `rules/security-rules.yml`.
- Aplícalo en la parte del archivo que corresponde al título del paso.
- Si el archivo aún no existe, créalo con este contenido inicial y luego evoluciona desde ahí en los siguientes pasos.

## Cambio base recomendado

Este bloque no es para pegar a ciegas: úsalo como punto de partida y ajústalo al contexto del repositorio.

```yaml
rules:
  - id: insecure-eval
    message: Eval no permitido por politica organizativa
    severity: ERROR
    pattern: eval($X)
```

## Como adaptarlo correctamente

- Mantén el cambio pequeño y centrado en una sola idea por paso.
- Usa `message:` para dejar claro que la regla responde a una política y no solo a una observación técnica.
- Mantén `severity: ERROR` si la organización trata ese patrón como incumplimiento directo.
- Usa `pattern: eval($X)` como ejemplo simple de una práctica explícitamente no permitida.
- Evita añadir configuración que no esté relacionada con el objetivo del paso.

## Que deberia verse al terminar

- La intención del cambio se entiende leyendo el archivo.
- El archivo muestra el control sin depender de comentarios ambiguos.
- Los marcadores esperados del paso aparecen de forma natural en la configuración.
- El lector entiende que la regla ya actúa como estándar organizativo y no solo como detector técnico.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-24.py` comprueba este paso contra el archivo configurado.
- El workflow busca `rules:` dentro de `rules/security-rules.yml`.
- El workflow busca `id: insecure-eval` dentro de `rules/security-rules.yml`.
- El workflow busca `message:` dentro de `rules/security-rules.yml`.
- El workflow busca `severity: ERROR` dentro de `rules/security-rules.yml`.
- El workflow busca `pattern: eval($X)` dentro de `rules/security-rules.yml`.

## Criterio de finalizacion

El paso 24 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 25.
