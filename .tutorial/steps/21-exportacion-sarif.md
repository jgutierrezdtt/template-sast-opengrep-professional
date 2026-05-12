# Paso 21. Exportacion sarif

## Objetivo de aprendizaje

Publicar hallazgos en un formato estándar consumible por plataformas de código y seguridad.

## Archivo y seccion que debes modificar

- Archivo objetivo: `.github/workflows/sast.yml`.
- Seccion donde aplicar el cambio: pasos de exportación de resultados.
- Resultado esperado: el repositorio incorpora el control de este paso de forma legible y revisable.

## Cambio que debes introducir

Copia este bloque como base y adáptalo al contexto real del repositorio:

```yaml
- name: Export SARIF
  run: opengrep --config rules/security-rules.yml --sarif --output results.sarif .
```

## Como adaptarlo correctamente

- Asegura que el archivo de salida tenga un nombre estable.
- Mantén la ruta del config alineada con las reglas del tutorial.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-21.py` comprueba el archivo y los marcadores esperados de este paso.
- Debe encontrar el marcador `Export SARIF` en `.github/workflows/sast.yml`.
- Debe encontrar el marcador `--sarif` en `.github/workflows/sast.yml`.
- Debe encontrar el marcador `results.sarif` en `.github/workflows/sast.yml`.

## Criterio de finalizacion

El paso 21 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 22.
