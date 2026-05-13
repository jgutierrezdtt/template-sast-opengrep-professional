# Paso 27. Reporting ejecutivo

## Objetivo de aprendizaje

Transformar los datos del programa SAST en un resumen legible para una audiencia que no revisa codigo: responsables de producto, CISO, directores de ingenieria. El reporting ejecutivo no explica como funciona OpenGrep: explica cuanto riesgo tiene el software de la organizacion y si ese riesgo esta mejorando.

## Por que importa esto

Un programa SAST sin reporte ejecutivo es invisible para quien decide prioridades y presupuesto. Si los responsables de negocio no tienen visibilidad del estado de seguridad del software, las decisiones de priorizacion se toman sin ese input.

El reporting ejecutivo es el mecanismo que conecta el trabajo tecnico del equipo de seguridad con las decisiones de negocio de la organizacion.

## Que vas a cambiar y por que

Añade en `docs/sast-analysis.md` una entrada que represente el contenido de un reporte ejecutivo trimestral: estado del riesgo en lenguaje de negocio, tendencia respecto al trimestre anterior, y las decisiones pendientes que requieren atencion de management.

## Archivo y seccion que debes modificar

- Archivo objetivo: `docs/sast-analysis.md`.
- Añade una entrada con el formato estandar del programa que represente el reporte ejecutivo.

## Cambio base recomendado

```markdown
## Hallazgo

Reporte ejecutivo SAST — Q2 2026

## Regla o fuente

Programa SAST — resumen trimestral para management

## Severidad

Informativo

## Confianza

Alta — basado en datos verificados del programa.

## Decision

Distribuir al CISO y directores de ingenieria. Puntos clave:

Estado actual: 4 hallazgos activos. 2 criticos en proceso de correccion (plazo: fin de sprint). 2 medios en backlog priorizado.

Tendencia: reduccion del 30% respecto a Q1. El quality gate bloqueante activado en el paso 23 ha prevenido 3 nuevas vulnerabilidades criticas en el ultimo mes.

Cobertura: 3 de 5 repositorios criticos con SAST activo. Los 2 restantes (api-gateway, payments-service) tienen plan de incorporacion en Q3.

Riesgo residual: 1 excepcion activa en src/safe-eval.js con vencimiento en septiembre. Bajo riesgo: acceso restringido a administradores.

Proxima accion de management: aprobar presupuesto para incorporar los 2 repositorios pendientes en Q3.
```

## Que te esta enseñando este cambio

- Un reporte ejecutivo de SAST tiene tres componentes: estado actual (que riesgo hay ahora), tendencia (si el riesgo mejora o empeora) y proxima accion (que necesita el equipo de management para continuar).
- "El quality gate bloqueante activado ha prevenido 3 nuevas vulnerabilidades criticas" es lenguaje de impacto: convierte una configuracion tecnica en un resultado de negocio.
- Nombrar los repositorios pendientes de incorporacion con su plan de Q3 convierte un gap de cobertura en un commitment con fecha. Sin esa especificidad, el gap queda invisible.
- La "proxima accion de management" es el elemento que distingue un reporte informativo de uno accionable. Sin el, el reporte termina en una bandeja sin respuesta.

## Como adaptarlo correctamente

- Usa numeros absolutos y porcentajes juntos: "2 criticos (reduccion del 50% respecto al trimestre anterior)" tiene mas contexto que solo "2 criticos".
- El lenguaje debe ser neutro respecto a la herramienta: el CISO no necesita saber que herramienta ejecuta el scan; necesita saber si el riesgo del software esta bajo control.
- Evita tecnicismos en el reporte ejecutivo: "inyeccion SQL" puede explicarse como "vulnerabilidad que permitiria acceso no autorizado a la base de datos".
- Si hay hallazgos criticos sin plan de resolucion, el reporte ejecutivo debe hacerlos visibles aunque sea incomodo. Eso es lo que hace que el reporte sea util y no solo optimista.

## Que deberia verse al terminar

- `docs/sast-analysis.md` tiene una entrada que representa un reporte ejecutivo con estado, tendencia y proxima accion.
- El contenido es legible para alguien sin contexto tecnico de OpenGrep.
- Los numeros del reporte son coherentes con las metricas del paso 26.
- Los markers esperados del paso siguen presentes de forma natural en la configuracion.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-27.py` comprueba este paso contra el archivo configurado.
- El workflow busca `## Hallazgo` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Regla o fuente` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Severidad` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Confianza` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Decision` dentro de `docs/sast-analysis.md`.

## Criterio de finalizacion

El paso 27 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 28.
