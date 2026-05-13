# Paso 22. Quality gate no bloqueante

## Objetivo de aprendizaje

Entender por que el primer quality gate SAST debe ser no bloqueante y como configurarlo para que informe sin frenar el pipeline. El quality gate no bloqueante es la forma de activar visibilidad de seguridad en un equipo sin disruptir su flujo de desarrollo.

## Por que importa esto

Activar un quality gate bloqueante desde el primer dia en un repositorio con deuda tecnica acumulada paraliza el desarrollo. El equipo reacciona desactivando el scanner o añadiendo excepciones masivas para poder seguir trabajando. El resultado es peor que no tener SAST.

El quality gate no bloqueante permite que el equipo vea los hallazgos, los entienda y construya el proceso de resolucion antes de que el gate empiece a bloquear. Es la estrategia de incorporacion que hace que los programas SAST sobrevivan mas de un sprint.

## Que vas a cambiar y por que

Actualiza `.github/workflows/sast.yml` para que el paso de escaneo no falle el pipeline cuando hay hallazgos. El scanner ejecuta, reporta, genera el SARIF, y el workflow termina con exito independientemente de los resultados.

## Archivo y seccion que debes modificar

- Archivo objetivo: `.github/workflows/sast.yml`.
- Asegurate de que el paso principal de escaneo tiene `continue-on-error: true` o que el comando de escaneo no retorna exit code no-cero.

## Cambio base recomendado

```yaml
      - name: Run OpenGrep
        continue-on-error: true
        run: |
          pip install opengrep-cli
          opengrep scan --config rules/security-rules.yml src/
```

## Que te esta enseñando este cambio

- `continue-on-error: true` en el paso de escaneo hace que el workflow no falle cuando OpenGrep detecta hallazgos. Los hallazgos son visibles en el log pero no bloquean el merge.
- Este comportamiento es una decision temporal, no una decision permanente. El plan es pasar al quality gate bloqueante del paso 23 una vez que el equipo haya resuelto la deuda heredada.
- La diferencia entre este paso y ignorar el SAST es que los hallazgos son visibles, contados y documentados. El equipo sabe que hay problemas; solo eligio no bloquear todavia.
- La transicion del quality gate no bloqueante al bloqueante es un hito importante del programa: marca que el equipo ya gestiona la deuda activamente y puede comprometerse a no introducir nueva deuda.

## Como adaptarlo correctamente

- Usa `continue-on-error: true` en el paso de escaneo, no en el de subida del artefacto. El artefacto debe subirse siempre.
- Documenta en `docs/sast-analysis.md` cuando se planea activar el quality gate bloqueante. Sin esa fecha, el gate no bloqueante se convierte en permanente.
- Un quality gate no bloqueante sigue teniendo valor si el equipo revisa los hallazgos activamente. Sin ese proceso, es ruido que nadie lee.
- Considera un threshold intermedio: el gate no bloquea por WARNINGs pero si bloquea si aparecen nuevos ERRORs no documentados. Ese es el paso 23.

## Que deberia verse al terminar

- El workflow ejecuta el scanner en cada push y pull_request y termina con exito aunque haya hallazgos.
- Los hallazgos son visibles en el log del workflow y en el artefacto SARIF.
- El equipo tiene documentado en que momento pasara al quality gate bloqueante.
- Los markers esperados del paso aparecen de forma natural en el workflow.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-22.py` comprueba este paso contra el archivo configurado.
- El workflow busca `name: SAST` dentro de `.github/workflows/sast.yml`.
- El workflow busca `pull_request:` dentro de `.github/workflows/sast.yml`.
- El workflow busca `push:` dentro de `.github/workflows/sast.yml`.
- El workflow busca `Run OpenGrep` dentro de `.github/workflows/sast.yml`.
- El workflow busca `rules/security-rules.yml` dentro de `.github/workflows/sast.yml`.

## Criterio de finalizacion

El paso 22 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 23.
