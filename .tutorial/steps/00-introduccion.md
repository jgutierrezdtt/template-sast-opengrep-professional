# Paso 0. Introducción

Este laboratorio está diseñado para practicar SAST con una perspectiva profesional. El objetivo no es solo ejecutar OpenGrep sobre un repositorio, sino aprender a operar reglas, interpretar hallazgos, gestionar excepciones, establecer baselines y convertir el análisis estático en un control útil para varios equipos.

## Qué vas a trabajar

Durante el recorrido vas a pasar por decisiones que suelen separar un escaneo aislado de un programa SAST mantenible:

- lectura inicial de una base vulnerable y primer escaneo
- uso y evolución de reglas por defecto y reglas propias
- reducción de falsos positivos y documentación de excepciones
- construcción de baseline y detección de nuevas vulnerabilidades
- priorización por contexto, severidad y confianza
- integración con GitHub Actions, SARIF y quality gates
- reporting ejecutivo y técnico

## Qué problema intenta resolver este laboratorio

SAST pierde valor cuando se usa sin gobierno. Los fallos más frecuentes son:

- demasiados hallazgos sin criterio de priorización
- reglas genéricas que producen ruido y fatiga
- excepciones abiertas sin trazabilidad ni caducidad
- gates que bloquean de más o no sirven para nada
- reporting incapaz de orientar remediación o decisiones

Este tutorial está orientado a corregir precisamente ese patrón.

## Cómo se recorre el tutorial

El orden importa. Primero entiendes la base vulnerable y el primer escaneo, luego aprendes a controlar calidad de reglas y excepciones, después construyes baseline y priorización, y finalmente conviertes el análisis en un flujo gobernable con automatización, métricas y reporting.

## Qué conviene tener claro antes de empezar

- más reglas no implica mejor señal
- una excepción sin justificación ni caducidad degrada el programa
- la severidad técnica por sí sola no basta para priorizar
- un programa SAST útil necesita reglas, contexto, evidencia y decisiones repetibles

## Siguiente paso

El botón **Empezar tutorial** abre directamente el paso 1.
