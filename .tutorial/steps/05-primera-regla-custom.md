# Paso 5. Primera regla custom

## Objetivo de aprendizaje

Las reglas por defecto rara vez cubren los patrones inseguros propios de la organización. Aquí empiezas a escribir una regla útil y mantenible dentro de `rules/security-rules.yml`.

## Que vas a cambiar y por que

Refuerza en `rules/security-rules.yml` una regla explícita que detecte un patrón inseguro reconocible, con identificador, mensaje y severidad. El valor del paso está en tratar la regla ya como una pieza custom del programa y no solo como un ejemplo de arranque.

## Archivo y seccion que debes modificar

- Archivo objetivo: `rules/security-rules.yml`.
- Aplícalo en la parte del archivo que corresponde al título del paso.
- Si el archivo aún no existe, créalo con este contenido inicial y luego evoluciona desde ahí en los siguientes pasos.

## Cambio base recomendado

Este bloque no es para pegar a ciegas: úsalo como punto de partida y ajústalo al contexto del repositorio.

```yaml
rules:
  - id: insecure-eval
    message: Evita eval con input controlado por usuario
    severity: ERROR
    languages: [javascript]
    pattern: eval($X)
```

## Como adaptarlo correctamente

- Elige un patrón sencillo y fácilmente demostrable, como `eval($X)` o un `exec` inseguro.
- Haz que el mensaje diga qué está mal y no solo que hubo un match.
- Mantén `id: insecure-eval` como ejemplo de una convención de naming estable para reglas reutilizables.
- Usa `severity: ERROR` cuando quieras que la regla represente una señal clara de riesgo y no una mera observación.
- Si el repositorio no es JavaScript, cambia `languages` y `pattern` al lenguaje real del ejemplo.

## Que deberia verse al terminar

- La regla tiene `id`, `message`, `severity` y `pattern`.
- Cualquier revisor entiende el riesgo leyendo la regla.
- El patrón no es tan amplio que convierta todo en falsos positivos.
- El lector entiende que ya existe una regla propia que el equipo puede evolucionar.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-05.py` comprueba este paso contra el archivo configurado.
- El workflow busca `rules:` dentro de `rules/security-rules.yml`.
- El workflow busca `id: insecure-eval` dentro de `rules/security-rules.yml`.
- El workflow busca `message:` dentro de `rules/security-rules.yml`.
- El workflow busca `severity: ERROR` dentro de `rules/security-rules.yml`.
- El workflow busca `pattern: eval($X)` dentro de `rules/security-rules.yml`.

## Criterio de finalizacion

El paso 5 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 6.
