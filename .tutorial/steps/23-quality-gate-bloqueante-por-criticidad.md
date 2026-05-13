# Paso 23. Quality gate bloqueante por criticidad

## Objetivo de aprendizaje

Este paso introduce un quality gate bloqueante por criticidad y debe dejar un cambio comprensible en `.github/workflows/sast.yml`.

## Que vas a cambiar y por que

Actualiza `.github/workflows/sast.yml` para explicar un gate bloqueante por criticidad. A diferencia del paso anterior, aquí el workflow ya representa una decisión de control de entrega: si OpenGrep detecta hallazgos por encima del umbral aceptado, el pipeline debe frenar el cambio.

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
- Mantén `name: SAST` y `Run OpenGrep` como elementos visibles del control que puede bloquear la entrega.
- Usa `pull_request:` y `push:` para dejar claro dónde aplica el gate.
- Explica en la narrativa del paso que el bloqueo debe responder a criticidad, no a cualquier señal menor.
- Evita añadir configuración que no esté relacionada con el objetivo del paso.

## Que deberia verse al terminar

- La intención del cambio se entiende leyendo el archivo.
- El archivo muestra el control sin depender de comentarios ambiguos.
- Los marcadores esperados del paso aparecen de forma natural en la configuración.
- El lector entiende que el workflow ya actúa como control de liberación y no solo como reporte.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-23.py` comprueba este paso contra el archivo configurado.
- El workflow busca `name: SAST` dentro de `.github/workflows/sast.yml`.
- El workflow busca `pull_request:` dentro de `.github/workflows/sast.yml`.
- El workflow busca `push:` dentro de `.github/workflows/sast.yml`.
- El workflow busca `Run OpenGrep` dentro de `.github/workflows/sast.yml`.
- El workflow busca `rules/security-rules.yml` dentro de `.github/workflows/sast.yml`.

## Criterio de finalizacion

El paso 23 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 24.
