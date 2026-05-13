# Paso 23. Quality gate bloqueante por criticidad

## Objetivo de aprendizaje

Activar el quality gate que bloquea merges cuando aparecen hallazgos de severidad critica y entender como calibrar el threshold para que el bloqueo sea util y no contraproducente.

## Por que importa esto

Un quality gate que bloquea todo para cualquier hallazgo genera rechazo inmediato del equipo de desarrollo: cada PR se convierte en un debate sobre si el hallazgo es relevante o no. Un quality gate que no bloquea nada no es un control de seguridad.

El punto de equilibrio es bloquear solo los hallazgos que el equipo ya decidio que son inaceptables: los de severidad ERROR sin excepcion documentada. Los de severidad WARNING no bloquean pero son visibles. Los que tienen excepcion activa no bloquean porque ya tienen una decision tomada.

## Que vas a cambiar y por que

Actualiza `.github/workflows/sast.yml` para que el paso de escaneo falle cuando detecta hallazgos de severidad ERROR. Retira el `continue-on-error: true` del paso principal y usa el flag de threshold de OpenGrep para controlar el comportamiento exacto.

## Archivo y seccion que debes modificar

- Archivo objetivo: `.github/workflows/sast.yml`.
- Elimina `continue-on-error: true` del paso de escaneo y añade el flag de threshold para que solo falle con ERRORs.

## Cambio base recomendado

```yaml
      - name: Run OpenGrep
        run: |
          pip install opengrep-cli
          opengrep scan --config rules/security-rules.yml src/ --error
```

## Que te esta enseñando este cambio

- `--error` hace que OpenGrep retorne exit code 1 solo cuando detecta hallazgos de severidad ERROR. Los WARNINGs no bloquean pero si aparecen en el log y en el SARIF.
- Retirar `continue-on-error: true` del paso de escaneo convierte el pipeline en un control efectivo: si hay un nuevo ERROR sin excepcion, el PR no puede fusionarse hasta que se resuelva.
- Este threshold asume que el equipo ya resolvio o excepcionó los ERRORs heredados (pasos 8-12). Si todavia hay ERRORs sin tratar en la baseline, este cambio bloqueara el pipeline para todos los PRs.
- La combinacion de quality gate bloqueante (ERRORs) y no bloqueante (WARNINGs) es el modelo mas comun en programas SAST maduros: cero tolerancia a riesgo critico nuevo, visibilidad en riesgo medio.

## Como adaptarlo correctamente

- Antes de activar el quality gate bloqueante, verifica que todos los ERRORs existentes en la baseline tienen excepcion documentada o han sido corregidos.
- Si el repositorio tiene hallazgos criticos en la baseline sin excepcion, el gate bloqueante los detectara en cada PR aunque no sean nuevos. Eso es ruido que el equipo ignorara.
- Comunica el cambio al equipo de desarrollo antes de activarlo: el primer PR que falla por el gate bloqueante sin previo aviso genera resistencia innecesaria.
- Considera añadir un step de pre-check que liste los ERRORs antes de fallar, para que el desarrollador vea exactamente que tiene que corregir.

## Que deberia verse al terminar

- El pipeline falla cuando OpenGrep detecta hallazgos de severidad ERROR en el codigo escaneado.
- El equipo puede hacer merge de PRs que solo tienen WARNINGs.
- Los hallazgos que tienen excepcion documentada no bloquean el pipeline.
- Los markers esperados del paso aparecen de forma natural en el workflow.

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
