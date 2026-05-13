# Paso 6. Regla con metavariables

## Objetivo de aprendizaje

Este paso introduce una regla con metavariables y debe dejar un cambio comprensible en `rules/security-rules.yml`.

## Que vas a cambiar y por que

Actualiza `rules/security-rules.yml` para que el uso de metavariables quede explícito y revisable. En este caso, `pattern: eval($X)` es la clave del paso porque `$X` representa el valor variable capturado por la regla y explica cómo OpenGrep generaliza el match sin limitarse a un literal fijo.

## Archivo y seccion que debes modificar

- Archivo objetivo: `rules/security-rules.yml`.
- Aplícalo en la parte del archivo que corresponde al título del paso.
- Si el archivo aún no existe, créalo con este contenido inicial y luego evoluciona desde ahí en los siguientes pasos.

## Cambio base recomendado

Este bloque no es para pegar a ciegas: úsalo como punto de partida y ajústalo al contexto del repositorio.

```yaml
rules:
  - id: insecure-eval
    message: Detecta uso inseguro de eval con entrada variable
    severity: ERROR
    pattern: eval($X)
```

## Como adaptarlo correctamente

- Mantén el cambio pequeño y centrado en una sola idea por paso.
- Usa `pattern: eval($X)` para mostrar que `$X` captura el argumento sin importar su nombre concreto.
- Haz que `message:` explique el riesgo de usar `eval` con entrada variable o controlada externamente.
- Mantén `severity: ERROR` si la organización trata ese patrón como hallazgo serio por defecto.
- Evita añadir configuración que no esté relacionada con el objetivo del paso.

## Que deberia verse al terminar

- La intención del cambio se entiende leyendo el archivo.
- El archivo muestra el control sin depender de comentarios ambiguos.
- Los marcadores esperados del paso aparecen de forma natural en la configuración.
- El lector entiende qué aporta una metavariable en la detección del patrón.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-06.py` comprueba este paso contra el archivo configurado.
- El workflow busca `rules:` dentro de `rules/security-rules.yml`.
- El workflow busca `id: insecure-eval` dentro de `rules/security-rules.yml`.
- El workflow busca `message:` dentro de `rules/security-rules.yml`.
- El workflow busca `severity: ERROR` dentro de `rules/security-rules.yml`.
- El workflow busca `pattern: eval($X)` dentro de `rules/security-rules.yml`.

## Criterio de finalizacion

El paso 6 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 7.
