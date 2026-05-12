# SAST OpenGrep Professional

Tutorial profesional de análisis estático con OpenGrep.

## Objetivo

Aprender a ejecutar y escalar un programa de SAST con enfoque profesional: reglas, priorización por contexto, gestión de falsos positivos, excepciones, baseline, métricas y reporting técnico/ejecutivo.

## Audiencia

Equipos de AppSec, DevSecOps, ingeniería de plataforma y desarrollo que necesiten operar análisis estático en múltiples repositorios con criterios de gobierno.

## Requisitos previos

- Conocimientos intermedios de Git y Pull Request.
- Experiencia básica con GitHub Actions.
- Nociones de análisis estático y gestión de vulnerabilidades.

## Herramientas utilizadas

- OpenGrep
- GitHub Actions
- SARIF
- GitHub Code Scanning (cuando aplique)
- Scripts de validación del curso

## Inicio del tutorial

[![Empezar tutorial](https://img.shields.io/badge/Empezar%20tutorial-0b69ff?style=for-the-badge&logo=github&logoColor=white)](https://github.com/new?template_name=template-sast-opengrep-professional&template_owner=jgutierrezdtt)

## Acceso al repositorio

- [Crear mi repositorio desde este template](https://github.com/new?template_name=template-sast-opengrep-professional&template_owner=jgutierrezdtt)
- [Volver al portal general](https://github.com/jgutierrezdtt/security-learning-portal)

## Gestión del progreso

- [Validar progreso](../../actions/workflows/validate.yml)
- [Probar integridad del tutorial](../../actions/workflows/test-tutorial.yml)
- [Ejecutar tests funcionales del tutorial](../../actions/workflows/functional-tests.yml)
- [Reiniciar tutorial](../../actions/workflows/reset-tutorial.yml)
- [Ver pasos del tutorial](./.tutorial/steps/)

## Arquitectura del laboratorio

El laboratorio combina una base de código vulnerable con reglas de OpenGrep, control de excepciones y flujo de reporting. Cada paso añade una capacidad operativa para evolucionar desde una ejecución básica hasta un modelo de gobierno escalable.

## Tabla de pasos

| Paso | Tema |
| --- | --- |
| 0 | Introducción |
| 1 | Aplicación vulnerable base |
| 2 | Primer escaneo con OpenGrep |
| 3 | Interpretación de resultados |
| 4 | Reglas por defecto |
| 5 | Primera regla custom |
| 6 | Regla con metavariables |
| 7 | Regla con exclusiones |
| 8 | Falso positivo documentado |
| 9 | Gestión de excepciones |
| 10 | Excepciones con caducidad |
| 11 | Excepciones con owner |
| 12 | Excepciones con justificación |
| 13 | Baseline inicial |
| 14 | Detección de nuevas vulnerabilidades |
| 15 | Priorización por contexto |
| 16 | Severidad técnica frente a severidad contextual |
| 17 | Confianza del hallazgo |
| 18 | Inventario de repositorios |
| 19 | Escaneo organizativo simulado |
| 20 | GitHub Actions |
| 21 | Exportación SARIF |
| 22 | Quality gate no bloqueante |
| 23 | Quality gate bloqueante por criticidad |
| 24 | Reglas prohibidas por organización |
| 25 | Revisión de excepciones vencidas |
| 26 | Métricas |
| 27 | Reporting ejecutivo |
| 28 | Reporting técnico |
| 29 | Afinación de reglas |
| 30 | Medalla final SAST Professional |

## Paso 0

El paso 0 describe el entorno, permisos y limitaciones del laboratorio. No bloquea el flujo: el botón principal abre directamente el paso 1.

## Actualización desde template

Este repositorio incluye `.template-version` y workflow de actualización para revisar cambios del template sin sobrescribir trabajo del usuario.

## Badge final

Al cerrar el curso se generan artefactos de finalización en:

- `.tutorial/badges/completion-badge.md`
- `.tutorial/badges/completion-badge.svg`
- `.tutorial/evidence/completion.json`

## Referencias

- [OpenGrep](https://github.com/opengrep/opengrep)
- [GitHub Actions](https://docs.github.com/actions)
- [SARIF](https://sarifweb.azurewebsites.net/)
