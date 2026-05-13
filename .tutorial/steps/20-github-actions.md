# Paso 20. GitHub Actions

## Objetivo de aprendizaje

Conectar el programa SAST al pipeline de CI/CD mediante un workflow de GitHub Actions. A partir de este paso, cada push y cada pull request ejecutan el scanner automaticamente y el equipo deja de depender de ejecuciones manuales.

## Por que importa esto

Un scanner que se ejecuta solo cuando alguien lo recuerda no es un control de seguridad: es una herramienta de auditoria ocasional. El valor del SAST esta en la ejecucion sistematica en cada cambio de codigo, antes de que llegue a la rama principal.

La diferencia entre ejecutar SAST manualmente y tenerlo en el pipeline es la diferencia entre detectar vulnerabilidades antes de produccion y detectarlas despues.

## Que vas a cambiar y por que

Crea `.github/workflows/sast.yml` con la configuracion minima para que OpenGrep ejecute en cada push y pull request usando las reglas del repositorio. El workflow debe ser lo suficientemente simple para que el equipo lo mantenga, y lo suficientemente completo para que sea un control real.

## Archivo y seccion que debes modificar

- Archivo objetivo: `.github/workflows/sast.yml`.
- Si el archivo no existe, créalo. Este es el workflow que activara todos los quality gates de los pasos siguientes.

## Cambio base recomendado

```yaml
name: SAST

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

permissions:
  contents: read

jobs:
  opengrep:
    name: Run OpenGrep
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Run OpenGrep
        run: |
          pip install opengrep-cli
          opengrep scan --config rules/security-rules.yml src/
```

## Que te esta enseñando este cambio

- `on: push` y `on: pull_request` son los dos triggers esenciales. Sin `pull_request`, el scanner no bloquea antes de fusionar. Sin `push`, no hay cobertura en merges directos a la rama principal.
- `permissions: contents: read` es el principio de minimo privilegio aplicado al workflow. Si el scanner no necesita escribir en el repositorio, no debe tener ese permiso.
- `opengrep scan --config rules/security-rules.yml` usa las reglas del repositorio, no las reglas genericas de la herramienta. Eso es lo que conecta el trabajo de los pasos 5-7 con el pipeline automatico.
- La accion de checkout pineada a `@v4` es una buena practica base. En el paso 7 del tutorial SLSA aprenderas por que los SHA son preferibles a los tags en entornos de alta seguridad.

## Como adaptarlo correctamente

- Ajusta el path de `src/` al directorio real del codigo fuente del repositorio.
- Si el repositorio tiene multiples lenguajes, añade `--lang` para que el scan sea especifico.
- No añadas mas permisos de los necesarios. Este workflow no necesita escribir artefactos todavia: eso viene en el paso 21 (exportacion SARIF).
- El workflow fallara si hay hallazgos de severidad ERROR con el comportamiento por defecto de OpenGrep. Eso es lo esperado: en el paso 22 aprenderás a controlar ese comportamiento.

## Que deberia verse al terminar

- `.github/workflows/sast.yml` existe y tiene los triggers de push y pull_request.
- El workflow usa las reglas del repositorio y no depende de reglas externas.
- El equipo puede explicar por que cada campo del workflow es necesario.
- Los markers esperados del paso aparecen de forma natural en el workflow.

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
