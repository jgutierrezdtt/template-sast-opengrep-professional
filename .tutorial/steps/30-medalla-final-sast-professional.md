# Paso 30. Medalla final sast professional

## Que hace este paso automaticamente

Este paso se valida de forma automatica en el pipeline de SAST. No requiere ejecucion manual de comandos por parte del usuario.

## Como se ejecuta

- El workflow `validate-steps.yml` se dispara por evento `push`, `pull_request` y `workflow_dispatch`.
- El validador `scripts/validate-step-30.py` comprueba el estado esperado para este paso.
- Si la validacion pasa, el estado del tutorial se refleja en `.tutorial/state.json`.

## Evidencia tecnica evaluada por el sistema

- Artefacto principal esperado: `.github/workflows/sast.yml`.
- Estado del paso en evidencia automatica: `.tutorial/evidence/step-30.json`.
- Coherencia de progresion en: `.tutorial/state.json`.

## Criterio de finalizacion automatica

El paso 30 queda completado cuando el workflow reporta exito para `validate-step-30.py` en GitHub Actions.

Este es el ultimo paso; el workflow de completion calcula el estado final automaticamente.
