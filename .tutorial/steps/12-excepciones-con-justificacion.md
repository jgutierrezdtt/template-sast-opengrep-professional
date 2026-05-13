# Paso 12. Excepciones con justificacion

## Objetivo de aprendizaje

Escribir un campo `reason:` que explique el analisis que llevo a la decision, no solo que la nombre. La diferencia entre una justificacion util y una vacia puede determinar si una auditoria considera la excepcion aceptable o no.

## Por que importa esto

"Falso positivo", "controlado" o "excepcion aprobada" no son justificaciones. Son etiquetas. Una justificacion real responde a: que analisis se hizo, que evidencia lo soporta y bajo que condicion dejaria de ser valida.

Sin eso, el campo `reason:` solo confirma que alguien tecleo algo. En una auditoria de conformidad, una excepcion con justificacion generica puede tratarse igual que una vulnerabilidad sin resolver.

## Que vas a cambiar y por que

Mejora el campo `reason:` en `docs/sast-exceptions.yml` para que cualquier revisor que no conozca el contexto original pueda leer la entrada, entender el analisis y decidir si la excepcion sigue siendo valida en la proxima revision.

Dos frases especificas son suficientes si explican el analisis concreto y la condicion que cambiaria la decision.

## Archivo y seccion que debes modificar

- Archivo objetivo: `docs/sast-exceptions.yml`.
- Edita el campo `reason:` de la entrada existente.
- No añadas campos nuevos: trabaja la calidad del `reason:`.

## Cambio base recomendado

```yaml
exceptions:
  - rule_id: insecure-eval
    path: src/safe-eval.js
    reason: El argumento de eval proviene exclusivamente de una allowlist estatica en constants.js. No existe ruta de ejecucion donde el input llegue desde el usuario o la red.
    owner: appsec-team
    expires_on: 2026-12-31
```

## Que te esta enseñando este cambio

- Un `reason:` util responde a "que analisis se hizo" y "que cambiaria esta decision". El ejemplo hace las dos cosas: nombra la allowlist estatica y descarta la ruta desde input externo.
- La especificidad es verificable. "Allowlist estatica en constants.js sin ruta de input externo" se puede comprobar leyendo el codigo. "Uso controlado" no.
- Un buen `reason:` reduce el coste de la revision periodica: el revisor no reconstruye el analisis desde cero, solo verifica que las condiciones siguen siendo ciertas.
- Si no puedes escribir dos frases especificas, probablemente la decision original no fue suficientemente rigurosa para merecer una excepcion.

## Como adaptarlo correctamente

- Incluye una referencia a donde se puede verificar la condicion: linea de codigo, archivo, test, ticket.
- Evita frases aplicables a cualquier excepcion: "revisado y aprobado", "no aplica en este contexto".
- Si la justificacion hace referencia a un ticket externo, incluye el identificador.
- Cuando el codigo bajo la excepcion cambie, un `reason:` especifico es lo que permite detectar que la condicion ya no se cumple.

## Que deberia verse al terminar

- El `reason:` explica el analisis especifico que llevo a la decision.
- Cualquier revisor puede entender bajo que condicion la excepcion dejaria de ser valida.
- La justificacion es verificable: referencia algo concreto en el codigo o en el proceso.
- Los marcadores esperados del paso siguen presentes de forma natural en la configuracion.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-12.py` comprueba este paso contra el archivo configurado.
- El workflow busca `exceptions:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `rule_id:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `path:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `reason:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `owner:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `expires_on:` dentro de `docs/sast-exceptions.yml`.

## Criterio de finalizacion

El paso 12 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 13.
