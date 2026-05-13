# Paso 30. Medalla final SAST Professional

## Objetivo de aprendizaje

Consolidar la vision completa del programa SAST que has construido a lo largo del tutorial y entender que elementos definen la diferencia entre un programa en funcionamiento y uno en nivel profesional.

## Lo que has construido

A lo largo de los 30 pasos has construido un programa SAST con todos sus componentes:

- Reglas custom propias del equipo con patrones, metavariables y exclusiones calibradas (pasos 5-7).
- Sistema de excepciones con justificacion, owner, caducidad y revision periodica (pasos 8-12).
- Baseline de hallazgos con analisis de severidad contextual y confianza (pasos 13-17).
- Inventario de repositorios con vision organizativa del riesgo (pasos 18-19).
- Pipeline CI/CD con SAST integrado, exportacion SARIF y quality gates calibrados (pasos 20-23).
- Reglas como politica organizativa y proceso de revision de excepciones vencidas (pasos 24-25).
- Metricas, reporting ejecutivo y tecnico para audiencias distintas (pasos 26-28).
- Afinacion de reglas basada en datos reales del programa (paso 29).

## Que distingue nivel professional

Un programa SAST professional no se mide por el numero de reglas activas ni por la herramienta que usa. Se mide por:

- Precision: las reglas detectan lo que deben detectar y no generan ruido que el equipo aprenda a ignorar.
- Trazabilidad: cada excepcion tiene owner, justificacion y caducidad. Cada hallazgo critico tiene un plan de correccion con fecha.
- Escalabilidad: el programa funciona igual en 5 repositorios que en 50, porque las decisiones de gobierno son sistematicas y no dependen de que alguien recuerde ejecutar algo.
- Visibilidad: el management sabe si el riesgo del software mejora o empeora sin necesitar acceso al pipeline.

## Que hacer a continuacion

El programa que has construido es un punto de partida, no un estado final. Los proximos pasos naturales son:

- Centralizar las reglas en un repositorio compartido por toda la organizacion para que los cambios lleguen a todos los equipos a la vez.
- Integrar los resultados SARIF con GitHub Code Scanning para tener el historial de hallazgos visible directamente en los pull requests.
- Automatizar la deteccion de excepciones proximas a vencer para que el proceso de revision periodica no dependa de recordatorios manuales.
- Añadir metricas de cobertura de reglas: no solo cuantos hallazgos hay sino cuantos tipos de vulnerabilidad estan cubiertos por el conjunto de reglas activo.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-30.py` comprueba este paso contra el archivo configurado.
- El workflow busca `## Hallazgo` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Regla o fuente` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Severidad` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Confianza` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Decision` dentro de `docs/sast-analysis.md`.

## Criterio de finalizacion

El paso 30 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Este es el ultimo paso del tutorial.
