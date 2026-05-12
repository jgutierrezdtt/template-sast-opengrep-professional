# Paso 29. Afinacion de reglas

## Objetivo de aprendizaje

Definir reglas de detección que sean útiles, mantenibles y comprensibles por el equipo.

## Archivo y seccion que debes modificar

- Archivo objetivo: `rules/security-rules.yml`.
- Seccion donde aplicar el cambio: lista rules del motor SAST.
- Resultado esperado: el repositorio incorpora el control de este paso de forma legible y revisable.

## Cambio que debes introducir

Copia este bloque como base y adáptalo al contexto real del repositorio:

```yaml
rules:
  - id: insecure-eval
    message: Evita eval con input controlado por usuario
    severity: ERROR
    languages: [javascript]
    pattern: eval($X)
```

## Como adaptarlo correctamente

- Cambia el patrón solo si tienes un caso real del lenguaje del repositorio.
- Mantén un mensaje que explique claramente el riesgo y la remediación.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-29.py` comprueba el archivo y los marcadores esperados de este paso.
- Debe encontrar el marcador `rules:` en `rules/security-rules.yml`.
- Debe encontrar el marcador `id: insecure-eval` en `rules/security-rules.yml`.
- Debe encontrar el marcador `message:` en `rules/security-rules.yml`.
- Debe encontrar el marcador `severity: ERROR` en `rules/security-rules.yml`.
- Debe encontrar el marcador `pattern: eval($X)` en `rules/security-rules.yml`.

## Criterio de finalizacion

El paso 29 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 30.
