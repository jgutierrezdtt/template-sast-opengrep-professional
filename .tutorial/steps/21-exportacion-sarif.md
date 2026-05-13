# Paso 21. Exportacion sarif

## Objetivo de aprendizaje

Este paso introduce la exportación SARIF y debe dejar un cambio comprensible en `.github/workflows/sast.yml`.

## Que vas a cambiar y por que

Actualiza `.github/workflows/sast.yml` para que el workflow produzca salida SARIF utilizable por otras herramientas y revisiones. En este paso importan tres marcadores concretos: `Export SARIF`, `--sarif` y `results.sarif`, porque representan la transición desde una ejecución local a una evidencia portable y consumible por la plataforma.

## Archivo y seccion que debes modificar

- Archivo objetivo: `.github/workflows/sast.yml`.
- Aplícalo en la parte del archivo que corresponde al título del paso.
- Si el archivo aún no existe, créalo con este contenido inicial y luego evoluciona desde ahí en los siguientes pasos.

## Cambio base recomendado

Este bloque no es para pegar a ciegas: úsalo como punto de partida y ajústalo al contexto del repositorio.

```yaml
- name: Export SARIF
  run: opengrep --config rules/security-rules.yml --sarif > results.sarif
```

## Como adaptarlo correctamente

- Mantén el cambio pequeño y centrado en una sola idea por paso.
- Usa `Export SARIF` como nombre visible del paso para que la intención quede clara en el workflow.
- Mantén `--sarif` explícito para dejar claro el formato de salida esperado.
- Usa `results.sarif` como artefacto reconocible y fácil de reutilizar en pasos posteriores.
- Evita añadir configuración que no esté relacionada con el objetivo del paso.

## Que deberia verse al terminar

- La intención del cambio se entiende leyendo el archivo.
- El archivo muestra el control sin depender de comentarios ambiguos.
- Los marcadores esperados del paso aparecen de forma natural en la configuración.
- El lector entiende cómo el workflow produce un resultado portable para análisis posterior.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-21.py` comprueba este paso contra el archivo configurado.
- El workflow busca `Export SARIF` dentro de `.github/workflows/sast.yml`.
- El workflow busca `--sarif` dentro de `.github/workflows/sast.yml`.
- El workflow busca `results.sarif` dentro de `.github/workflows/sast.yml`.

## Criterio de finalizacion

El paso 21 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 22.
