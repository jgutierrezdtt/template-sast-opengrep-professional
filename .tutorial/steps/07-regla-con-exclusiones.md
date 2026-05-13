# Paso 7. Regla con exclusiones

## Objetivo de aprendizaje

Aprender a reducir falsos positivos sin desactivar la detección principal. En OpenGrep, una exclusión no existe para esconder alertas molestas, sino para sacar del alcance rutas o contextos que no deben tratarse igual que el código real de producción.

## Que vas a cambiar y por que

Vas a volver sobre la regla `insecure-eval` en `rules/security-rules.yml`. Hasta ahora te servía para detectar cualquier uso de `eval(...)`; en este paso debes empezar a pensar qué partes del repositorio sí quieres inspeccionar y cuáles conviene dejar fuera porque generarían ruido. El validador mantiene la misma base de la regla porque el aprendizaje no está en inventar otro patrón, sino en entender cómo se refina una detección existente sin romper su intención.

## Archivo y seccion que debes modificar

- Archivo objetivo: `rules/security-rules.yml`.
- Este paso se centra en la regla `insecure-eval`, no en crear una segunda regla distinta.
- Piensa la edición como una decisión de alcance: primero dejas claro qué riesgo sigues detectando y después decides qué contextos pueden quedar excluidos con justificación.

## Cambio base recomendado

No copies este bloque como solución final. Úsalo como núcleo de una regla que sigue detectando el riesgo principal antes de que empieces a afinar exclusiones concretas.

```yaml
rules:
  - id: insecure-eval
    message: Detecta uso inseguro de eval
    severity: ERROR
    pattern: eval($X)
```

## Que significa cada parte de la regla en este paso

- `id: insecure-eval` da nombre estable al control que luego podrás afinar, documentar o excepcionar.
- `message:` debe seguir explicando el riesgo al desarrollador aunque más adelante excluyas rutas legítimas.
- `severity: ERROR` recuerda que estás afinando un hallazgo serio, no rebajándolo por comodidad.
- `pattern: eval($X)` mantiene el comportamiento base; las exclusiones recortan el alcance alrededor de ese patrón, no lo sustituyen.

## Como pensar las exclusiones correctamente

- Excluye solo contextos que puedas defender técnicamente, por ejemplo tests preparados para demostrar vulnerabilidades, fixtures o código generado que no representa lógica de negocio.
- No excluyas directorios solo porque producen muchos hallazgos; primero entiende por qué aparecen y si realmente no son relevantes.
- Conserva `pattern: eval($X)` como núcleo de la regla para que la detección siga siendo reconocible y mantenible.
- Haz que `message:` siga teniendo sentido para quien reciba la alerta después de aplicar exclusiones.
- El objetivo del paso es reducir ruido sin perder cobertura útil.

## Que deberia verse al terminar

- La regla sigue expresando con claridad que `eval` es un uso peligroso.
- El lector entiende que el siguiente refinamiento natural es acotar rutas o contextos concretos, no cambiar el patrón principal.
- Queda claro que una exclusión bien hecha mejora precisión, pero una exclusión mala puede esconder hallazgos reales.
- Los marcadores esperados del paso siguen presentes de forma natural en la configuración.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-07.py` comprueba este paso contra el archivo configurado.
- El workflow busca `rules:` dentro de `rules/security-rules.yml`.
- El workflow busca `id: insecure-eval` dentro de `rules/security-rules.yml`.
- El workflow busca `message:` dentro de `rules/security-rules.yml`.
- El workflow busca `severity: ERROR` dentro de `rules/security-rules.yml`.
- El workflow busca `pattern: eval($X)` dentro de `rules/security-rules.yml`.

## Criterio de finalizacion

El paso 7 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 8.
