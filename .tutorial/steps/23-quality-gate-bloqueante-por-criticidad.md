# Paso 23. Quality gate bloqueante por criticidad

## Objetivo de aprendizaje

Ejecutar el análisis SAST automáticamente y decidir si bloquea o no el cambio.

## Archivo y seccion que debes modificar

- Archivo objetivo: `.github/workflows/sast.yml`.
- Seccion donde aplicar el cambio: workflow de análisis y gate.
- Resultado esperado: el repositorio incorpora el control de este paso de forma legible y revisable.

## Cambio que debes introducir

Copia este bloque como base y adáptalo al contexto real del repositorio:

```yaml
name: SAST
on:
  pull_request:
  push:
jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - name: Run OpenGrep
        run: opengrep --config rules/security-rules.yml .
```

## Como adaptarlo correctamente

- Usa gate no bloqueante cuando estás afinando reglas.
- Activa bloqueo solo cuando las reglas críticas estén estabilizadas.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-23.py` comprueba el archivo y los marcadores esperados de este paso.
- Debe encontrar el marcador `name: SAST` en `.github/workflows/sast.yml`.
- Debe encontrar el marcador `pull_request:` en `.github/workflows/sast.yml`.
- Debe encontrar el marcador `push:` en `.github/workflows/sast.yml`.
- Debe encontrar el marcador `Run OpenGrep` en `.github/workflows/sast.yml`.
- Debe encontrar el marcador `rules/security-rules.yml` en `.github/workflows/sast.yml`.

## Criterio de finalizacion

El paso 23 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 24.
