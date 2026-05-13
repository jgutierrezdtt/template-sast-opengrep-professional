# Paso 20. Github actions

## Objetivo de aprendizaje

Este paso introduce la integración de SAST en GitHub Actions y debe dejar un cambio comprensible en `.github/workflows/sast.yml`.

## Que vas a cambiar y por que

Actualiza `.github/workflows/sast.yml` para que el análisis SAST quede integrado de forma visible en la automatización del repositorio. El foco aquí es que el workflow tenga identidad clara, se dispare en los eventos adecuados y ejecute OpenGrep contra `rules/security-rules.yml` como parte normal del ciclo de cambios.

## Archivo y seccion que debes modificar

- Archivo objetivo: `.github/workflows/sast.yml`.
- Aplícalo en la parte del archivo que corresponde al título del paso.
- Si el archivo aún no existe, créalo con este contenido inicial y luego evoluciona desde ahí en los siguientes pasos.

## Cambio base recomendado

Este bloque no es para pegar a ciegas: úsalo como punto de partida y ajústalo al contexto del repositorio.

```yaml
name: SAST
on:
  pull_request:
  push:
jobs:
  sast:
    steps:
      - name: Run OpenGrep
        run: opengrep --config rules/security-rules.yml .
```

## Como adaptarlo correctamente

- Mantén el cambio pequeño y centrado en una sola idea por paso.
- Usa `name: SAST` para que el workflow sea fácil de identificar en la plataforma.
- Mantén `pull_request:` y `push:` como disparadores visibles del control.
- Haz que `Run OpenGrep` y `rules/security-rules.yml` expliquen claramente qué ejecuta el job y con qué reglas.
- Evita añadir configuración que no esté relacionada con el objetivo del paso.

## Que deberia verse al terminar

- La intención del cambio se entiende leyendo el archivo.
- El archivo muestra el control sin depender de comentarios ambiguos.
- Los marcadores esperados del paso aparecen de forma natural en la configuración.
- Se entiende cómo el análisis estático entra en la automatización del repositorio.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-20.py` comprueba este paso contra el archivo configurado.
- El workflow busca `name: SAST` dentro de `.github/workflows/sast.yml`.
- El workflow busca `pull_request:` dentro de `.github/workflows/sast.yml`.
- El workflow busca `push:` dentro de `.github/workflows/sast.yml`.
- El workflow busca `Run OpenGrep` dentro de `.github/workflows/sast.yml`.
- El workflow busca `rules/security-rules.yml` dentro de `.github/workflows/sast.yml`.

## Criterio de finalizacion

El paso 20 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 21.
