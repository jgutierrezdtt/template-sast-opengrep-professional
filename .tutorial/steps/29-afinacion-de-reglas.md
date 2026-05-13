# Paso 29. Afinacion de reglas

## Objetivo de aprendizaje

Este paso introduce la afinación de reglas y debe dejar un cambio comprensible en `rules/security-rules.yml`.

## Que vas a cambiar y por que

Actualiza `rules/security-rules.yml` para que la afinación de reglas quede explícita y revisable. En esta fase la regla `insecure-eval` ya no es solo un detector inicial: es una regla madura que debe equilibrar cobertura, claridad del mensaje y reducción de ruido sin perder la intención de control.

## Archivo y seccion que debes modificar

- Archivo objetivo: `rules/security-rules.yml`.
- Aplícalo en la parte del archivo que corresponde al título del paso.
- Si el archivo aún no existe, créalo con este contenido inicial y luego evoluciona desde ahí en los siguientes pasos.

## Cambio base recomendado

Este bloque no es para pegar a ciegas: úsalo como punto de partida y ajústalo al contexto del repositorio.

```yaml
rules:
  - id: insecure-eval
    message: Detecta uso inseguro de eval con criterio afinado
    severity: ERROR
    pattern: eval($X)
```

## Como adaptarlo correctamente

- Mantén el cambio pequeño y centrado en una sola idea por paso.
- Usa `message:` para reflejar mejor el criterio final de la regla y no un texto genérico.
- Mantén `pattern: eval($X)` como núcleo del control mientras afinas precisión y contexto alrededor de la regla.
- Piensa este paso como el cierre del ciclo de mejora de reglas: menos ruido, mejor señal y misma intención de protección.
- Evita añadir configuración que no esté relacionada con el objetivo del paso.

## Que deberia verse al terminar

- La intención del cambio se entiende leyendo el archivo.
- El archivo muestra el control sin depender de comentarios ambiguos.
- Los marcadores esperados del paso aparecen de forma natural en la configuración.
- El lector entiende que la regla ya está afinada para un uso más maduro dentro del programa SAST.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-29.py` comprueba este paso contra el archivo configurado.
- El workflow busca `rules:` dentro de `rules/security-rules.yml`.
- El workflow busca `id: insecure-eval` dentro de `rules/security-rules.yml`.
- El workflow busca `message:` dentro de `rules/security-rules.yml`.
- El workflow busca `severity: ERROR` dentro de `rules/security-rules.yml`.
- El workflow busca `pattern: eval($X)` dentro de `rules/security-rules.yml`.

## Criterio de finalizacion

El paso 29 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 30.
