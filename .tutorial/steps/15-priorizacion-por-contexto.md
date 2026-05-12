# Paso 15. Priorizacion por contexto

## Que hace este paso automaticamente

Este paso se valida de forma automatica en el pipeline de SAST. No requiere ejecucion manual de comandos por parte del usuario.

## Como se ejecuta

- El workflow `validate-steps.yml` se dispara por evento `push`, `pull_request` y `workflow_dispatch`.
- El validador `scripts/validate-step-15.py` comprueba el estado esperado para este paso.
- Si la validacion pasa, el estado del tutorial se refleja en `.tutorial/state.json`.

## Evidencia tecnica evaluada por el sistema

- Artefacto principal esperado: `rules/security-rules.yml`.
- Estado del paso en evidencia automatica: `.tutorial/evidence/step-15.json`.
- Coherencia de progresion en: `.tutorial/state.json`.

## Criterio de finalizacion automatica

El paso 15 queda completado cuando el workflow reporta exito para `validate-step-15.py` en GitHub Actions.

Siguiente paso automatico: Paso 16.
