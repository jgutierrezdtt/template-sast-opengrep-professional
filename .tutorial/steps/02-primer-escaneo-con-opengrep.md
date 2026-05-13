# Paso 2. Primer escaneo con opengrep

## Objetivo de aprendizaje

Este paso introduce el primer escaneo con OpenGrep y debe dejar un cambio comprensible en `rules/security-rules.yml`.

## Que vas a cambiar y por que

Actualiza `rules/security-rules.yml` para que el primer escaneo con OpenGrep quede anclado a una regla comprensible. En esta fase el objetivo no es la sofisticación, sino disponer de una regla mínima y visible que permita validar el flujo de análisis y empezar a observar resultados con criterio.

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
- Mantén `id: demo-rule` como identificador simple para reconocer fácilmente qué regla dispara el primer escaneo.
- Usa `severity: WARNING` como señal de arranque que permita ver resultados sin endurecer todavía el programa.
- Piensa este paso como una comprobación de flujo: regla, ejecución y lectura básica de hallazgos.
- Evita añadir configuración que no esté relacionada con el objetivo del paso.

## Que deberia verse al terminar

- La intención del cambio se entiende leyendo el archivo.
- El archivo muestra el control sin depender de comentarios ambiguos.
- Los marcadores esperados del paso aparecen de forma natural en la configuración.
- El lector entiende cómo arranca el primer escaneo estático del laboratorio.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-02.py` comprueba este paso contra el archivo configurado.
- El workflow busca `rules:` dentro de `rules/security-rules.yml`.
- El workflow busca `id: demo-rule` dentro de `rules/security-rules.yml`.
- El workflow busca `severity: WARNING` dentro de `rules/security-rules.yml`.

## Criterio de finalizacion

El paso 2 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 3.
