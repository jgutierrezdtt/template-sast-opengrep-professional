# Paso 4. Reglas por defecto

## Objetivo de aprendizaje

Entender qué te aporta una regla por defecto y qué no. Este paso enseña a reconocer la estructura mínima de una regla SAST útil antes de entrar en personalizaciones más finas o necesidades específicas de la organización.

## Que vas a cambiar y por que

Vas a consolidar en `rules/security-rules.yml` una regla más completa que la del arranque. La finalidad es aprender a leer una regla por defecto como una pieza operativa: tiene un identificador estable, un mensaje para el desarrollador, una severidad y un patrón que define qué comportamiento se considera inseguro. Este paso es importante porque muchas organizaciones usan reglas por defecto sin entender realmente qué señal están introduciendo en sus pipelines.

## Archivo y seccion que debes modificar

- Archivo objetivo: `rules/security-rules.yml`.
- Este paso se centra en una regla realista y reconocible, no solo en un identificador de ejemplo.
- Piensa la edición como la transición entre una señal de arranque y una detección que ya podría formar parte de una política SAST básica.

## Cambio base recomendado

No copies este bloque como una solución cerrada. Úsalo para entender qué elementos convierten una regla en algo legible, revisable y ejecutable.

```yaml
rules:
  - id: insecure-eval
    message: Detecta uso inseguro de eval
    severity: ERROR
    pattern: eval($X)
```

## Que te esta enseñando esta regla

- `id: insecure-eval` da un nombre estable al control y permite referenciarlo más adelante en análisis, excepciones o reporting.
- `message:` traduce el hallazgo técnico a una explicación legible para quien recibe la alerta.
- `severity: ERROR` marca que el patrón se considera serio desde el principio y no como simple observación.
- `pattern: eval($X)` concreta qué forma de código está buscando OpenGrep.

## Como adaptarlo correctamente

- No conviertas la regla en algo críptico; si un revisor no entiende qué detecta leyendo cuatro líneas, la regla ya nace mal.
- Haz que `message:` explique el riesgo real y no solo renombre el `id`.
- Usa este paso para entender el valor de una regla por defecto: acelerar detección conocida, no resolver todos los casos del repositorio.
- El aprendizaje central aquí es distinguir entre tener una regla usable y tener una regla ya afinada.

## Que deberia verse al terminar

- El archivo contiene una regla que ya se puede leer y discutir como control SAST real.
- El lector entiende el papel de `id`, `message`, `severity` y `pattern` dentro de una regla por defecto.
- Queda claro que esta base todavía necesitará afinación posterior, pero ya no es solo una señal de arranque.
- Los marcadores esperados del paso siguen presentes de forma natural en la configuración.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-04.py` comprueba este paso contra el archivo configurado.
- El workflow busca `rules:` dentro de `rules/security-rules.yml`.
- El workflow busca `id: insecure-eval` dentro de `rules/security-rules.yml`.
- El workflow busca `message:` dentro de `rules/security-rules.yml`.
- El workflow busca `severity: ERROR` dentro de `rules/security-rules.yml`.
- El workflow busca `pattern: eval($X)` dentro de `rules/security-rules.yml`.

## Criterio de finalizacion

El paso 4 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 5.
