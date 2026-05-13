# Paso 15. Priorizacion por contexto

## Objetivo de aprendizaje

Entender que la severidad tecnica de un hallazgo no determina sola su urgencia operativa. El contexto del repositorio, la exposicion real del codigo y el impacto de negocio son los factores que convierten un ERROR tecnico en una prioridad real o en un hallazgo de baja urgencia.

## Por que importa esto

Un equipo que prioriza solo por severidad tecnica acaba gestionando el pipeline SAST como una lista de errores ordenada por color. Un equipo que prioriza por contexto puede decir "este ERROR en el servicio de autenticacion de produccion va al sprint de hoy, y este otro ERROR en un script de migracion interno va al backlog del trimestre".

La priorizacion por contexto es lo que hace que el programa SAST sea util para el negocio y no solo para el auditor.

## Que vas a cambiar y por que

Actualiza una entrada en `docs/sast-analysis.md` para que el campo `## Decision` refleje la priorizacion por contexto: no solo "corregir" o "aceptar" sino cuando y por que tiene esa urgencia relativa en este repositorio concreto.

## Archivo y seccion que debes modificar

- Archivo objetivo: `docs/sast-analysis.md`.
- Edita o añade una entrada donde la decision explique la prioridad segun el contexto de uso del codigo.

## Cambio base recomendado

```markdown
## Hallazgo

Hash debil (MD5) para almacenamiento de tokens en src/auth/tokens.js linea 89.

## Regla o fuente

weak-hash-algorithm (rules/security-rules.yml)

## Severidad

WARNING

## Confianza

Alta — MD5 confirmado como algoritmo de hashing de tokens de sesion.

## Decision

Prioridad alta a pesar de severidad WARNING: los tokens son credenciales de sesion de usuarios finales en produccion. Correccion planificada en sprint actual con migracion a SHA-256.
```

## Que te esta enseñando este cambio

- Un WARNING en credenciales de sesion de produccion tiene mas urgencia real que un ERROR en un script de migracion de base de datos interna. La severidad tecnica es un punto de partida, no la decision final.
- El campo `## Decision` es donde se registra el razonamiento de priorizacion, no solo la accion. "Prioridad alta a pesar de severidad WARNING" con su justificacion es informacion que ninguna herramienta automatica puede generar.
- La referencia al sprint concreto convierte la decision en un compromiso trazable, no en una intencion sin fecha.
- Este tipo de analisis es lo que permite presentar el estado del programa SAST a un responsable de negocio: "tenemos N hallazgos, los de mayor riesgo real estan en el sprint actual".

## Como adaptarlo correctamente

- El contexto de priorizacion incluye: exposicion del codigo (internet, intranet, interno), tipo de datos que maneja (credenciales, datos personales, configuracion interna) y frecuencia de uso.
- No uses el contexto para bajar artificialmente la prioridad de hallazgos incomodos. El contexto debe reducir la urgencia cuando el riesgo real es menor, no cuando la correccion es costosa.
- Documenta en la decision cuales son los factores de contexto que determinaron la prioridad.
- Este documento es la base del reporting ejecutivo del paso 27, donde necesitaras explicar prioridades en terminos de negocio.

## Que deberia verse al terminar

- Al menos una entrada en `docs/sast-analysis.md` tiene una decision que explica la prioridad por contexto, no solo la accion tecnica.
- El razonamiento de priorizacion es legible por alguien sin contexto tecnico profundo del repositorio.
- Queda claro que la severidad tecnica es un input para la decision, no la decision misma.
- Los marcadores esperados del paso siguen presentes de forma natural en la configuracion.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-15.py` comprueba este paso contra el archivo configurado.
- El workflow busca `## Hallazgo` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Regla o fuente` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Severidad` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Confianza` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Decision` dentro de `docs/sast-analysis.md`.

## Criterio de finalizacion

El paso 15 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 16.
