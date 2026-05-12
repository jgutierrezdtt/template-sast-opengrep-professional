# Paso 1. Aplicacion vulnerable base

## Objetivo de aprendizaje

Definir la base del análisis SAST para el tutorial.

## Archivo y seccion que debes modificar

- Archivo objetivo: `rules/security-rules.yml`.
- Seccion donde aplicar el cambio: configuración principal de reglas.
- Resultado esperado: el repositorio incorpora el control de este paso de forma legible y revisable.

## Cambio que debes introducir

Copia este bloque como base y adáptalo al contexto real del repositorio:

```yaml
rules:
  - id: demo-rule
    message: Regla base del tutorial
    severity: WARNING
    languages: [javascript]
    pattern: console.log($X)
```

## Como adaptarlo correctamente

- Cambia la regla demo por un caso real del proyecto.
- Usa identificadores estables para poder revisar excepciones y métricas.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-01.py` comprueba el archivo y los marcadores esperados de este paso.
- Debe encontrar el marcador `rules:` en `rules/security-rules.yml`.
- Debe encontrar el marcador `id: demo-rule` en `rules/security-rules.yml`.
- Debe encontrar el marcador `severity: WARNING` en `rules/security-rules.yml`.

## Criterio de finalizacion

El paso 1 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 2.
