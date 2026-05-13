# Paso 24. Reglas prohibidas por organizacion

## Objetivo de aprendizaje

Entender como las reglas SAST pueden actuar como politica organizativa: no solo detectando vulnerabilidades tecnicas sino prohibiendo patrones de codigo que la organizacion ha decidido que son inaceptables independientemente del contexto.

## Por que importa esto

Hay patrones de codigo que una organizacion decide prohibir no porque cada uso sea una vulnerabilidad, sino porque el riesgo agregado de permitirlos supera el beneficio en cualquier caso de uso. `eval`, ciertos mecanismos de deserializacion, funciones de hash obsoletas para credenciales, o el uso de APIs internas que han sido deprecadas por seguridad.

Las reglas como politica organizativa son las que hacen que el programa SAST sea mas que un scanner: son los controles que el equipo de seguridad ha decidido que todos los repositorios deben respetar.

## Que vas a cambiar y por que

Actualiza `rules/security-rules.yml` para añadir una regla que no detecta una vulnerabilidad tecnica generica sino un patron que la organizacion ha decidido prohibir explicitamente. La diferencia debe quedar clara en el `message:`: no es "esto puede ser inseguro" sino "esto viola la politica de seguridad de la organizacion".

## Archivo y seccion que debes modificar

- Archivo objetivo: `rules/security-rules.yml`.
- Añade una regla que funcione como control de politica organizativa, distinta de las reglas de deteccion tecnica de los pasos anteriores.

## Cambio base recomendado

```yaml
rules:
  - id: insecure-eval
    message: Evita eval con input controlado por usuario
    severity: ERROR
    languages: [javascript]
    pattern: eval($X)

  - id: org-policy-no-md5-passwords
    message: "Politica organizativa: MD5 esta prohibido para hashing de credenciales. Usa bcrypt, argon2 o PBKDF2."
    severity: ERROR
    languages: [javascript, python]
    pattern: md5($PASSWORD)
```

## Que te esta enseñando este cambio

- El `message:` de una regla de politica organizativa tiene una estructura distinta a la de una regla de deteccion tecnica: nombra la politica, el patron prohibido y la alternativa. Sin la alternativa, el desarrollador sabe que no puede hacer pero no sabe que si puede.
- El `id: org-policy-no-md5-passwords` tiene el prefijo `org-policy-` para que sea inmediatamente distinguible en los reportes de las reglas de deteccion tecnica generica.
- Una regla de politica organizativa tiene mas peso en una auditoria que una deteccion tecnica: si aparece en el programa es porque el equipo de seguridad tomo una decision explicita de prohibicion.
- La diferencia entre "puede ser inseguro" y "viola la politica de la organizacion" es la diferencia entre un hallazgo que el desarrollador puede argumentar y uno que no puede excepcionar sin aprobacion del equipo de seguridad.

## Como adaptarlo correctamente

- Las reglas de politica organizativa deben distribuirse a todos los repositorios del programa, no solo al repositorio donde se crean. En pasos avanzados esto se hace mediante un repositorio central de reglas.
- El `message:` debe incluir la alternativa aprobada. Sin ella, la regla solo bloquea sin orientar.
- Considera versionar las reglas de politica con una fecha o version para que el historial de cambios sea trazable.
- Una excepcion a una regla de politica organizativa requiere mas justificacion que una excepcion a una deteccion tecnica generica. Documenta ese proceso.

## Que deberia verse al terminar

- `rules/security-rules.yml` tiene al menos una regla que funciona como control de politica organizativa, distinguible de las reglas de deteccion tecnica.
- El `message:` de esa regla nombra la politica, el patron prohibido y la alternativa aprobada.
- El `id` de la regla sigue una convencion de naming que la distingue de las reglas de deteccion generica.
- Los markers esperados del paso aparecen de forma natural en el archivo.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-24.py` comprueba este paso contra el archivo configurado.
- El workflow busca `rules:` dentro de `rules/security-rules.yml`.
- El workflow busca `id: insecure-eval` dentro de `rules/security-rules.yml`.
- El workflow busca `message:` dentro de `rules/security-rules.yml`.
- El workflow busca `severity: ERROR` dentro de `rules/security-rules.yml`.
- El workflow busca `pattern: eval($X)` dentro de `rules/security-rules.yml`.

## Criterio de finalizacion

El paso 24 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 25.
