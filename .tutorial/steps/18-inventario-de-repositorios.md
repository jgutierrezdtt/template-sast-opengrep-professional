# Paso 18. Inventario de repositorios

## Objetivo de aprendizaje

Entender que un programa SAST organizativo no gestiona repositorios, sino hallazgos con contexto de repositorio. El inventario es la base que permite saber en que repositorios hay cobertura SAST, en cuales no, y como se compara el estado de seguridad entre ellos.

## Por que importa esto

Cuando el SAST solo existe en un repositorio aislado, el equipo tiene una foto de ese repositorio pero no del riesgo organizativo real. Las vulnerabilidades mas criticas suelen aparecer en los repositorios que nadie mira: los legacy, los que "nadie toca", los que se asume que estan bien porque llevan mucho tiempo sin cambios.

Un inventario de repositorios con su estado SAST convierte la seguridad de aplicaciones de una actividad por repositorio a un programa con visibilidad organizativa.

## Que vas a cambiar y por que

Añade en `docs/sast-analysis.md` una seccion que registre al menos un repositorio con su estado de cobertura SAST, su nivel de riesgo estimado y las decisiones pendientes. No es un informe exhaustivo: es el punto de partida del inventario.

## Archivo y seccion que debes modificar

- Archivo objetivo: `docs/sast-analysis.md`.
- Añade una seccion de inventario que siga el formato de analisis con los cinco campos del programa.

## Cambio base recomendado

```markdown
## Hallazgo

Repositorio api-gateway sin cobertura SAST activa. Ultimo commit hace 3 dias. Dependencias con 4 CVEs criticos segun Dependabot.

## Regla o fuente

Inventario de repositorios — revision manual Q2 2026.

## Severidad

ERROR

## Confianza

Alta — ausencia de workflow SAST confirmada. CVEs verificados en Dependabot Security.

## Decision

Activar SAST en api-gateway en el sprint actual: añadir workflow con OpenGrep y reglas basicas. El volumen de hallazgos inicial se tratara como baseline sin bloqueo.
```

## Que te esta enseñando este cambio

- Un repositorio sin cobertura SAST es en si mismo un hallazgo de seguridad. El inventario lo hace visible con el mismo formato que cualquier otro hallazgo.
- La referencia a la fuente ("Inventario de repositorios — revision manual") distingue este tipo de hallazgo de los detectados automaticamente por reglas. Ambos son validos en el programa.
- La decision de "tratar el volumen inicial como baseline sin bloqueo" es una decision de incorporacion progresiva: activar el control sin bloquear el desarrollo inmediatamente.
- El campo `## Confianza` en un hallazgo de inventario registra si la informacion del repositorio fue verificada o es una estimacion.

## Como adaptarlo correctamente

- El inventario no necesita cubrir todos los repositorios en el primer paso: empieza con los de mayor criticidad o los que tienen cambios mas frecuentes.
- Incluye en el inventario repositorios que ya tienen SAST activo: el inventario no es solo una lista de lo que falta sino una vista de cobertura completa.
- Usa la misma estructura de cinco campos para todos los hallazgos de inventario. La consistencia es lo que permite agregar y comparar datos.
- Este documento es la entrada del paso 19 (escaneo organizativo simulado), donde simularas como se veria el estado SAST de una cartera de repositorios.

## Que deberia verse al terminar

- `docs/sast-analysis.md` tiene al menos una entrada de inventario de repositorios con los cinco campos.
- La entrada describe un repositorio real o realista con su estado de cobertura y el riesgo asociado.
- La decision es accionable: no "revisar algun dia" sino una accion con horizonte temporal.
- El documento ya empieza a tomar forma de un programa SAST con alcance organizativo.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-18.py` comprueba este paso contra el archivo configurado.
- El workflow busca `## Hallazgo` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Regla o fuente` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Severidad` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Confianza` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Decision` dentro de `docs/sast-analysis.md`.

## Criterio de finalizacion

El paso 18 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 19.
