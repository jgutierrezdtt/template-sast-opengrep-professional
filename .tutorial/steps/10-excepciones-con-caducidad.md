# Paso 10. Excepciones con caducidad

## Objetivo de aprendizaje

Entender por que `expires_on:` no es un campo opcional y como la fecha de caducidad convierte una excepcion en un compromiso de revision, no en una aceptacion permanente.

## Por que importa esto

La mayoria de las excepciones nacen con una justificacion valida: "la mitigacion esta en progreso", "es un entorno de desarrollo", "se va a refactorizar en el proximo sprint". Sin una fecha de caducidad, esa justificacion queda congelada indefinidamente aunque el contexto haya cambiado.

Las excepciones sin caducidad son la forma mas comun de acumular deuda de seguridad silenciosa en un programa SAST. El codigo cambia, las dependencias cambian, los equipos cambian, pero las excepciones permanecen.

## Que vas a cambiar y por que

Revisa el campo `expires_on:` en `docs/sast-exceptions.yml` para que sea una fecha real y proxima que obligue a una revision genuina. No es solo un campo de formato: es el mecanismo que hace que el programa SAST no pierda de vista las decisiones de seguridad pasadas.

La caducidad bien usada es lo que separa un programa con gobierno de uno con deuda acumulada.

## Archivo y seccion que debes modificar

- Archivo objetivo: `docs/sast-exceptions.yml`.
- Revisa la entrada existente para que `expires_on:` tenga una fecha con la que el equipo se compromete a revisar si la excepcion sigue siendo valida.
- No pongas fechas arbitrariamente lejanas. Una caducidad en tres años para una excepcion "temporal" es contradictoria.

## Cambio base recomendado

Usa este bloque para entender que `expires_on:` debe reflejar el tiempo real que se necesita para resolver la situacion que justifica la excepcion.

```yaml
exceptions:
  - rule_id: insecure-eval
    path: src/safe-eval.js
    reason: Mitigacion temporal pendiente de cierre en sprint Q2
    owner: appsec-team
    expires_on: 2026-12-31
```

## Que te esta enseñando este cambio

- `expires_on:` como campo obligatorio cambia la psicologia del equipo respecto a las excepciones: ya no es "ignorar para siempre" sino "acepto hasta esta fecha con compromiso de revision".
- La fecha debe corresponder al tiempo real estimado para resolver lo que justifica la excepcion. Si la mitigacion esta en el proximo sprint, la fecha no deberia ser en seis meses.
- Un `reason:` que menciona el sprint o el ticket de resolucion hace que la caducidad tenga contexto: el revisor sabe que buscar cuando llegue la fecha.
- Cuando `expires_on:` pase, el paso 25 (revision de excepciones vencidas) detectara la entrada y forzara una decision: renovar con nueva justificacion o retirar.

## Como adaptarlo correctamente

- Si no sabes cuánto tiempo tardara la resolucion, usa 90 dias como plazo por defecto y revisa al llegar.
- Una fecha de expiracion no es una promesa de que el problema estara resuelto: es una promesa de que el equipo volvera a evaluarlo.
- Evita la tentacion de poner una fecha muy lejana para "no tener que pensar en ello". Eso convierte la excepcion en permanente sin serlo en nombre.
- El proceso de revision periodica (paso 25) es lo que hace que esta fecha tenga valor real.

## Que deberia verse al terminar

- La entrada en `docs/sast-exceptions.yml` tiene una fecha de expiracion que refleja un compromiso real, no una fecha arbitraria.
- El `reason:` menciona cual es la situacion temporal que justifica la excepcion y que triggerearia su cierre.
- El equipo puede explicar en una frase que pasara cuando llegue la fecha de expiracion.
- Los marcadores esperados del paso siguen presentes de forma natural en la configuracion.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-10.py` comprueba este paso contra el archivo configurado.
- El workflow busca `exceptions:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `rule_id:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `path:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `reason:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `owner:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `expires_on:` dentro de `docs/sast-exceptions.yml`.

## Criterio de finalizacion

El paso 10 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 11.
