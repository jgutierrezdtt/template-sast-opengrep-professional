# Paso 8. Falso positivo documentado

## Objetivo de aprendizaje

Distinguir entre silenciar una alerta y documentar un falso positivo. El primero es deuda tecnica sin trazabilidad. El segundo es una decision de seguridad auditada.

## Por que importa esto

En la mayoria de equipos, los falsos positivos se "silencian" añadiendo un comentario o flag sin registro. Seis meses despues, nadie sabe si ese silencio sigue siendo valido, quien lo aprobo o si la condicion que lo justificaba ha cambiado.

En una auditoria de seguridad, un silencio sin documentar no es distinto de una vulnerabilidad ignorada. Un falso positivo documentado, en cambio, muestra que el equipo analizo la alerta y tomo una decision informada.

## Que vas a cambiar y por que

Añade la primera entrada en `docs/sast-exceptions.yml` que registre un falso positivo con los datos minimos necesarios para que sea revisable: regla que lo genero, ruta donde ocurre, razon por la que es falso positivo, responsable y fecha de expiracion.

No dejes ninguno de estos campos vacio. Un falso positivo sin owner no tiene responsable. Sin `expires_on` no tiene ciclo de vida. Sin `reason` no tiene analisis.

## Archivo y seccion que debes modificar

- Archivo objetivo: `docs/sast-exceptions.yml`.
- Si el archivo no existe, créalo. Este es el punto de partida del sistema de excepciones del programa SAST.
- El formato de este archivo sera la referencia para todos los falsos positivos y excepciones de los pasos siguientes.

## Cambio base recomendado

Usa esta estructura como plantilla de lo que debe contener un falso positivo documentado correctamente.

```yaml
exceptions:
  - rule_id: insecure-eval
    path: src/safe-eval.js
    reason: Uso controlado y revisado como falso positivo
    owner: appsec-team
    expires_on: 2026-12-31
```

## Que te esta enseñando este cambio

- `rule_id:` vincula la excepcion a una regla concreta del programa SAST. Sin esto, el sistema no puede correlacionar excepciones con reglas activas ni detectar excepciones huerfanas.
- `path:` acota el alcance a una ruta especifica. Una excepcion que cubra todo el repositorio silencia tambien hallazgos reales futuros.
- `reason:` es el campo mas importante del documento. Debe explicar el analisis, no solo renombrar la excepcion. "Uso controlado" sin mas detalle es insuficiente.
- `owner:` convierte la excepcion en una responsabilidad asignada. El owner es quien puede confirmar en el siguiente ciclo de revision si la excepcion sigue siendo valida.
- `expires_on:` obliga a una fecha de revision. Sin esta fecha, la excepcion no tiene ciclo de vida y se convierte en deuda de seguridad silenciosa.

## Como adaptarlo correctamente

- No uses una fecha de expiracion demasiado lejana para evitar la revision. Una excepcion con expiracion en 2030 hoy probablemente nunca sera revisada.
- El `reason` debe ser especifico: "Sanitizacion validada en linea 42 de safe-eval.js mediante allowlist auditada" es mejor que "controlado".
- Si el owner es un equipo, asegurate de que el equipo existe y de que tiene un proceso para revisar estas excepciones.
- Este archivo sera la fuente de verdad del paso 25 (revision de excepciones vencidas), asi que estructuralo de forma que sea facil de parsear.

## Que deberia verse al terminar

- `docs/sast-exceptions.yml` existe y contiene al menos una excepcion completa.
- La excepcion es legible por cualquier revisor sin necesidad de contexto adicional.
- Queda claro que la decision de marcarla como falso positivo se baso en un analisis, no en conveniencia.
- Los cinco campos estan presentes y ninguno tiene un valor vacio o de relleno.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-08.py` comprueba este paso contra el archivo configurado.
- El workflow busca `exceptions:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `rule_id:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `path:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `reason:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `owner:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `expires_on:` dentro de `docs/sast-exceptions.yml`.

## Criterio de finalizacion

El paso 8 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 9.
