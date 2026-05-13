# Paso 1. Aplicacion vulnerable base

## Objetivo de aprendizaje

Este paso introduce la aplicación vulnerable base y debe dejar un cambio comprensible en `rules/security-rules.yml`.

## Que vas a cambiar y por que

Actualiza `rules/security-rules.yml` para que el primer control de SAST quede explícito y revisable. En este paso no estás resolviendo todavía un caso complejo, sino estableciendo una regla base identificable que permita anclar el laboratorio sobre una aplicación vulnerable conocida.

## Archivo y seccion que debes modificar

- Archivo objetivo: `rules/security-rules.yml`.
- Aplícalo en la parte del archivo que corresponde al título del paso.
- Si el archivo aún no existe, créalo con este contenido inicial y luego evoluciona desde ahí en los siguientes pasos.

## Cambio base recomendado

Este bloque no es para pegar a ciegas: úsalo como punto de partida y ajústalo al contexto del repositorio.

```yaml
rules:
  - id: demo-rule
    severity: WARNING
```

## Como adaptarlo correctamente

- Mantén el cambio pequeño y centrado en una sola idea por paso.
- Usa `id: demo-rule` como identificador simple y fácil de reconocer durante el arranque del laboratorio.
- Mantén `severity: WARNING` para que la primera regla represente una señal inicial sin imponer todavía un criterio duro de bloqueo.
- Piensa este paso como la base sobre la que luego evolucionarán reglas, falsos positivos y excepciones.
- Evita añadir configuración que no esté relacionada con el objetivo del paso.

## Que deberia verse al terminar

- La intención del cambio se entiende leyendo el archivo.
- El archivo muestra el control sin depender de comentarios ambiguos.
- Los marcadores esperados del paso aparecen de forma natural en la configuración.
- El lector entiende que ya existe una regla mínima sobre la que crecerá el programa SAST.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-01.py` comprueba este paso contra el archivo configurado.
- El workflow busca `rules:` dentro de `rules/security-rules.yml`.
- El workflow busca `id: demo-rule` dentro de `rules/security-rules.yml`.
- El workflow busca `severity: WARNING` dentro de `rules/security-rules.yml`.

## Criterio de finalizacion

El paso 1 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 2.
