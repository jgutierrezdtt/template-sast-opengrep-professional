# Paso 6. Regla con metavariables

## Objetivo de aprendizaje

Entender por que una regla con metavariable detecta mas que una regla con literal fijo, y cuándo esa generalización es un activo y cuándo introduce ruido.

## Por que importa esto

Una regla que solo detecta `eval("codigo-concreto")` no sirve en produccion. El codigo real pasa variables, concatenaciones y expresiones. Si el patron no captura eso, el 90% de los casos reales escapan al analisis.

Las metavariables son el mecanismo que convierte una deteccion de laboratorio en una deteccion de produccion.

## Que vas a cambiar y por que

Actualiza `rules/security-rules.yml` para que la regla de `eval` use `$X` como metavariable explicita. El cambio no es solo tecnico: es la primera vez que documentas intencionalmente que la regla captura cualquier expresion pasada a `eval`, no solo un literal concreto.

Esto afecta al alcance de la deteccion y a la tasa de falsos positivos. Entenderlo ahora evita sorpresas cuando la regla entre en el pipeline.

## Archivo y seccion que debes modificar

- Archivo objetivo: `rules/security-rules.yml`.
- Actualiza la regla existente de `insecure-eval` para que `$X` sea explicito en el `pattern`.
- No añadas una segunda regla: refina la que ya tienes.

## Cambio base recomendado

Usa este bloque para entender como una metavariable cambia el alcance del patron respecto a un literal fijo.

```yaml
rules:
  - id: insecure-eval
    message: Detecta uso inseguro de eval con entrada variable
    severity: ERROR
    pattern: eval($X)
```

## Que te esta enseñando este cambio

- `$X` es una metavariable: representa cualquier expresion valida en el lenguaje. OpenGrep la resuelve en tiempo de analisis, no en tiempo de escritura de la regla.
- La diferencia entre `eval("literal")` y `eval($X)` es la diferencia entre detectar un caso concreto y detectar toda la familia de usos inseguros.
- `$X` puede capturar una variable, una concatenacion, el resultado de una funcion o cualquier expresion. Por eso el patron es mas potente y tambien mas facil de afinar mal.
- Un mensaje como "con entrada variable" es mas informativo que "uso de eval" porque explica por que la metavariable hace que el riesgo sea mas amplio.

## Como adaptarlo correctamente

- Usa metavariables cuando el patron tenga partes que cambian en cada ocurrencia del codigo real.
- Evita crear metavariables para partes que son siempre literales: eso solo añade generalidad innecesaria.
- Si tras aplicar la regla ves que dispara en archivos de test donde `eval` es seguro, el siguiente paso (exclusiones) es la herramienta correcta, no eliminar la metavariable.
- Una regla con una sola metavariable es el minimo viable. Aprenderás a combinar multiples en pasos avanzados.

## Que deberia verse al terminar

- La regla contiene `pattern: eval($X)` de forma explicita.
- El equipo puede explicar en una frase por que `$X` amplia la deteccion respecto a un literal.
- Queda claro que la metavariable es una decision deliberada, no un comportamiento por defecto no entendido.
- Los marcadores esperados del paso siguen presentes de forma natural en la configuracion.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-06.py` comprueba este paso contra el archivo configurado.
- El workflow busca `rules:` dentro de `rules/security-rules.yml`.
- El workflow busca `id: insecure-eval` dentro de `rules/security-rules.yml`.
- El workflow busca `message:` dentro de `rules/security-rules.yml`.
- El workflow busca `severity: ERROR` dentro de `rules/security-rules.yml`.
- El workflow busca `pattern: eval($X)` dentro de `rules/security-rules.yml`.

## Criterio de finalizacion

El paso 6 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 7.
