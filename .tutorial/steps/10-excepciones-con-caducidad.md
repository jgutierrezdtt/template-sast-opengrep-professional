# Paso 10. Excepciones con caducidad

## Objetivo de aprendizaje

Distinguir una excepción justificada de una supresión sin control.

## Archivo y seccion que debes modificar

- Archivo objetivo: `docs/sast-exceptions.yml`.
- Seccion donde aplicar el cambio: catálogo de excepciones y falsos positivos.
- Resultado esperado: el repositorio incorpora el control de este paso de forma legible y revisable.

## Cambio que debes introducir

Copia este bloque como base y adáptalo al contexto real del repositorio:

```yaml
exceptions:
  - rule_id: insecure-eval
    path: src/legacy.js
    reason: "caso heredado aislado"
    owner: "team-appsec"
    expires_on: "2026-12-31"
```

## Como adaptarlo correctamente

- Cada excepción debe estar vinculada a una regla y a una ruta concreta.
- No uses excepciones globales si el problema está localizado.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-10.py` comprueba el archivo y los marcadores esperados de este paso.
- Debe encontrar el marcador `exceptions:` en `docs/sast-exceptions.yml`.
- Debe encontrar el marcador `rule_id:` en `docs/sast-exceptions.yml`.
- Debe encontrar el marcador `path:` en `docs/sast-exceptions.yml`.
- Debe encontrar el marcador `reason:` en `docs/sast-exceptions.yml`.
- Debe encontrar el marcador `owner:` en `docs/sast-exceptions.yml`.
- Debe encontrar el marcador `expires_on:` en `docs/sast-exceptions.yml`.

## Criterio de finalizacion

El paso 10 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 11.
