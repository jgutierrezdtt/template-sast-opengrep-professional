# Paso 1. Aplicacion vulnerable base

## Objetivo de aprendizaje

Entender por qué el laboratorio arranca sobre una aplicación deliberadamente vulnerable y con una regla mínima. Antes de hablar de calidad de hallazgos, excepciones o gates, necesitas un punto de partida que haga visible cómo se define una señal SAST básica.

## Que vas a cambiar y por que

Vas a tocar `rules/security-rules.yml` para dejar creada una primera regla reconocible. El objetivo no es detectar ya el caso más importante del repositorio, sino aprender qué aspecto tiene el esqueleto mínimo de una regla y cómo se usa para anclar el laboratorio sobre una base vulnerable conocida. Si esta primera pieza no es clara, el resto del tutorial se convierte en una colección de hallazgos sin referencia común.

## Archivo y seccion que debes modificar

- Archivo objetivo: `rules/security-rules.yml`.
- Este paso se centra en declarar la primera regla del repositorio, no en cubrir todavía todos los patrones inseguros.
- Piensa este cambio como la semilla del catálogo de reglas: a partir de aquí vendrán reglas más precisas, hallazgos, excepciones y priorización.

## Cambio base recomendado

No copies este bloque como si fuese una política final. Úsalo para entender qué piezas mínimas necesita una regla antes de empezar a sofisticarla.

```yaml
rules:
  - id: demo-rule
    severity: WARNING
```

## Que enseña esta regla minima

- `rules:` deja claro que trabajas sobre un conjunto de reglas y no sobre una comprobación aislada pegada a mano.
- `id: demo-rule` crea un nombre estable para identificar la detección cuando empieces a ver resultados, documentación o excepciones.
- `severity: WARNING` mantiene la primera señal en un nivel manejable para aprender el flujo sin convertir todavía el laboratorio en una política bloqueante.

## Como adaptarlo correctamente

- No intentes detectar demasiadas cosas a la vez; en este paso importa más entender la forma de la regla que su cobertura.
- Usa un `id` simple para que luego puedas reconocer con facilidad qué hallazgos pertenecen a esta primera iteración.
- Mantén `severity: WARNING` si quieres que la primera lectura del laboratorio enseñe señal básica antes de endurecer criterios.
- El resultado esperado es una base pequeña pero legible sobre la que crecerá el programa SAST.

## Que deberia verse al terminar

- El archivo ya contiene una regla mínima reconocible y fácil de explicar.
- El lector entiende por qué el laboratorio arranca con una señal sencilla en vez de empezar con reglas complejas.
- Queda claro que esta regla no resuelve el problema completo, pero sí crea una base útil para los siguientes pasos.
- Los marcadores esperados del paso siguen presentes de forma natural en la configuración.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-01.py` comprueba este paso contra el archivo configurado.
- El workflow busca `rules:` dentro de `rules/security-rules.yml`.
- El workflow busca `id: demo-rule` dentro de `rules/security-rules.yml`.
- El workflow busca `severity: WARNING` dentro de `rules/security-rules.yml`.

## Criterio de finalizacion

El paso 1 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 2.
