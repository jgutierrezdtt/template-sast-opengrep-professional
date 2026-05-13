# Paso 11. Excepciones con owner

## Objetivo de aprendizaje

Entender por que el campo `owner:` convierte una excepcion de registro anonimo en una responsabilidad asignada, y como esa asignacion cambia la dinamica del programa SAST.

## Por que importa esto

Una excepcion sin owner es una decision que nadie se atribuye. Cuando llega la fecha de revision, nadie sabe a quien preguntar si la justificacion sigue siendo valida. Cuando el codigo cambia, nadie notifica al responsable. Cuando el auditor pregunta quien aprobo la excepcion, no hay respuesta.

El campo `owner:` no es burocracia: es el mecanismo que hace que la excepcion tenga un ciclo de vida gestionado por alguien, no solo registrado en un archivo.

## Que vas a cambiar y por que

Asegurate de que el campo `owner:` en `docs/sast-exceptions.yml` referencia a un equipo o persona que existe hoy y que tiene capacidad de responder en la proxima revision. Un owner que ya no forma parte del equipo, o un equipo que no tiene proceso de revision, no cumple el proposito.

Este paso enseña a pensar en la excepcion como un contrato entre quien la aprueba y quien la va a revisar.

## Archivo y seccion que debes modificar

- Archivo objetivo: `docs/sast-exceptions.yml`.
- Revisa el campo `owner:` de la entrada existente para que refleje al equipo o persona real que responde por esta excepcion.
- Si usas un nombre de equipo, asegurate de que ese equipo tiene un proceso definido para revisar excepciones SAST.

## Cambio base recomendado

Usa este bloque para entender que el `owner:` debe ser un identificador que permita localizar a quien puede tomar la decision de renovar o cerrar la excepcion.

```yaml
exceptions:
  - rule_id: insecure-eval
    path: src/safe-eval.js
    reason: Uso validado por analisis de flujo de entrada
    owner: appsec-team
    expires_on: 2026-12-31
```

## Que te esta enseñando este cambio

- `owner:` en un programa SAST cumple la misma funcion que el campo de responsable en un ticket de vulnerabilidad: sin el, la excepcion queda en un estado sin gobierno.
- Un nombre de equipo como `appsec-team` es mas estable que un nombre individual, pero requiere que el equipo tenga un proceso definido para actuar cuando la excepcion vence.
- El owner es el primer contacto cuando el codigo bajo la excepcion cambia de forma que invalida la justificacion. Sin este campo, esa informacion no llega a nadie.
- En una auditoria, el auditor no solo preguntara "hay excepciones" sino "quien las aprobo y quien las revisa". El campo `owner:` es la respuesta.

## Como adaptarlo correctamente

- Si el owner es una persona, considera si seguira en el equipo cuando venza la excepcion. Si hay riesgo de rotacion, usa un alias de equipo.
- No uses un owner que no tenga visibilidad del codigo que cubre la excepcion. Un equipo de infraestructura no puede revisar una excepcion en logica de aplicacion.
- Si la excepcion nacio de una decision tecnica de desarrollo, el owner deberia incluir tambien a alguien de desarrollo, no solo de seguridad.
- Documenta en el `reason:` el proceso por el que se asigno el owner si es relevante para la revision futura.

## Que deberia verse al terminar

- La entrada en `docs/sast-exceptions.yml` tiene un `owner:` que es un equipo o persona identificable que puede actuar cuando la excepcion vence.
- El equipo puede explicar en una frase que proceso seguira el owner cuando llegue la fecha de revision.
- Queda claro que el campo `owner:` no es un campo de trazabilidad pasiva sino de responsabilidad activa.
- Los marcadores esperados del paso siguen presentes de forma natural en la configuracion.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-11.py` comprueba este paso contra el archivo configurado.
- El workflow busca `exceptions:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `rule_id:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `path:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `reason:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `owner:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `expires_on:` dentro de `docs/sast-exceptions.yml`.

## Criterio de finalizacion

El paso 11 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 12.
