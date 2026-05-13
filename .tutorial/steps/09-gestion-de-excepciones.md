# Paso 9. Gestion de excepciones

## Objetivo de aprendizaje

Pasar de tener una excepcion aislada a tener una estructura de gobierno de excepciones. La diferencia no esta en el numero de entradas, sino en que el archivo ya puede soportar un proceso de revision periodica.

## Por que importa esto

Un programa SAST maduro no acumula excepciones: las administra. La diferencia entre un equipo que gestiona bien y uno que no es que el primero puede responder en todo momento cuantas excepciones activas tiene, quien las aprobo, por que motivo y cuándo vencen.

Sin estructura, las excepciones se apilan sin control hasta que el archivo pierde credibilidad y nadie lo revisa.

## Que vas a cambiar y por que

Consolida en `docs/sast-exceptions.yml` una estructura que ya se puede gobernar: al menos una excepcion con todos sus campos cubiertos, en un formato que un proceso automatizado pueda parsear para detectar entradas vencidas, sin owner o sin razon suficiente.

Este paso es la transicion entre "tengo un falso positivo documentado" y "tengo un sistema para gestionar las excepciones del programa SAST".

## Archivo y seccion que debes modificar

- Archivo objetivo: `docs/sast-exceptions.yml`.
- Edita el archivo del paso anterior para asegurarte de que su estructura soporta multiples entradas y revision periodica.
- No tienes que añadir mas entradas: lo importante es que la estructura ya este preparada para ello.

## Cambio base recomendado

Este bloque muestra una estructura de excepcion que ya puede ser parte de un proceso de gobierno.

```yaml
exceptions:
  - rule_id: insecure-eval
    path: src/safe-eval.js
    reason: Excepcion temporal aprobada por analisis de flujo de datos
    owner: appsec-team
    expires_on: 2026-12-31
```

## Que te esta enseñando este cambio

- La clave de este paso es el `reason:` mas detallado. "Aprobada por analisis de flujo de datos" implica que hubo un proceso de analisis, no solo una decision rapida.
- La estructura `exceptions:` como lista YAML permite añadir entradas sin cambiar el formato. Eso es lo que hace que sea gobernable: el proceso de revision puede iterar sobre la lista.
- Un `path:` especifico es mas gobernable que uno generico. Si la excepcion cubre `src/` completo, no hay forma de saber cuando ha dejado de ser necesaria.
- El `owner:` en este paso no es solo un campo de trazabilidad: es la persona o equipo que tiene que responder en la proxima revision periodica.

## Como adaptarlo correctamente

- Piensa en este archivo como un contrato: cada entrada es un acuerdo entre el equipo de seguridad y el equipo de desarrollo con fecha de caducidad.
- Evita excepciones con `path: .` o rutas muy amplias. El alcance minimo posible reduce el riesgo de silenciar hallazgos reales futuros.
- Si el `reason` de una excepcion no puedes explicarlo en dos frases, probablemente la decision no fue suficientemente rigurosa.
- Diseña el archivo pensando en quien va a revisarlo en el paso 25, no solo en quien lo escribe hoy.

## Que deberia verse al terminar

- `docs/sast-exceptions.yml` tiene una estructura lista para multiples entradas.
- Cualquier miembro del equipo puede leer el archivo y entender el proceso de gobierno que hay detras.
- La excepcion existente tiene un `reason` que explica el analisis y no solo renombra la regla.
- Los marcadores esperados del paso siguen presentes de forma natural en la configuracion.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-09.py` comprueba este paso contra el archivo configurado.
- El workflow busca `exceptions:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `rule_id:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `path:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `reason:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `owner:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `expires_on:` dentro de `docs/sast-exceptions.yml`.

## Criterio de finalizacion

El paso 9 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 10.
