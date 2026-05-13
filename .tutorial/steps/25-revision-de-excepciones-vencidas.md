# Paso 25. Revision de excepciones vencidas

## Objetivo de aprendizaje

Ejecutar el proceso de revision periodica de excepciones: identificar las que han vencido, evaluar si la justificacion original sigue siendo valida y tomar una decision explicita sobre cada una: renovar, cerrar o escalar.

## Por que importa esto

Las excepciones que se crean y nunca se revisan son la forma mas comun de acumular deuda de seguridad oculta en un programa SAST. Cada excepcion vencida es un riesgo que el equipo decidio aceptar temporalmente y luego olvido.

El proceso de revision periodica es lo que convierte el archivo de excepciones en un control vivo. Sin este proceso, el archivo solo acumula entradas que nadie cuestiona.

## Que vas a cambiar y por que

Revisa las entradas en `docs/sast-exceptions.yml` y actualiza las que han vencido o estan proximas a vencer. Para cada entrada, debes tomar una decision explicita documentada: renovar con nueva justificacion, cerrar porque el problema fue resuelto, o escalar porque la situacion ha cambiado.

## Archivo y seccion que debes modificar

- Archivo objetivo: `docs/sast-exceptions.yml`.
- Actualiza las fechas o las decisiones de las excepciones existentes con el resultado de la revision.
- Si una excepcion fue resuelta, eliminala del archivo o añade un campo `status: closed` con la fecha de cierre.

## Cambio base recomendado

```yaml
exceptions:
  - rule_id: insecure-eval
    path: src/safe-eval.js
    reason: Revision Q2 2026 — La allowlist estatica sigue activa y la ruta de input externo sigue sin existir. Refactorizacion planificada para Q3 2026. Se renueva hasta esa fecha.
    owner: appsec-team
    expires_on: 2026-09-30
```

## Que te esta enseñando este cambio

- Una renovacion no es automatica: el `reason:` actualizado debe confirmar que las condiciones que justificaron la excepcion original siguen vigentes. "Se renueva" sin verificacion no es una revision.
- La nueva fecha de expiracion debe coincidir con el horizonte de resolucion planificado. Si la refactorizacion es en Q3, la fecha es el fin de Q3, no seis meses mas por defecto.
- El proceso de revision periodica es la diferencia entre un programa de excepciones con gobierno y una lista de silencias acumulados. El audit trail del campo `reason:` en cada revision es lo que hace que la historia sea trazable.
- Si una excepcion fue resuelta porque se corrigio la vulnerabilidad, eliminarla del archivo activo es la accion correcta. Dejarla con status closed es opcional pero util si el historial importa para auditorias.

## Como adaptarlo correctamente

- Define la cadencia de revision antes de necesitarla: mensual para excepciones de severidad critica, trimestral para el resto.
- La revision no debe ser solo una actualizacion de fechas: debe incluir verificacion de que las condiciones del `reason:` original siguen siendo ciertas.
- Si el owner de una excepcion ya no esta en el equipo, la revision periodica es el momento de reasignar, no de dejarlo sin owner.
- Considera generar automaticamente una lista de excepciones proximas a vencer (por ejemplo, en los proximos 30 dias) como parte del workflow del pipeline.

## Que deberia verse al terminar

- Las excepciones en `docs/sast-exceptions.yml` tienen fechas de expiracion actualizadas o decisiones de cierre documentadas.
- El `reason:` de cada excepcion renovada explica que verificacion se hizo en la revision, no solo que se renueva.
- El equipo tiene claro cual es la cadencia de revision y quien es responsable de ejecutarla.
- Los markers esperados del paso siguen presentes de forma natural en la configuracion.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-25.py` comprueba este paso contra el archivo configurado.
- El workflow busca `exceptions:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `rule_id:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `path:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `reason:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `owner:` dentro de `docs/sast-exceptions.yml`.
- El workflow busca `expires_on:` dentro de `docs/sast-exceptions.yml`.

## Criterio de finalizacion

El paso 25 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 26.
