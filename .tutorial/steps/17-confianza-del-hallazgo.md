# Paso 17. Confianza del hallazgo

## Objetivo de aprendizaje

Usar el campo `## Confianza` como un indicador de cuanto se puede confiar en la deteccion antes de actuar. La confianza no es una opinion subjetiva: se basa en si el flujo de datos entre la fuente del riesgo y el punto de explotacion fue trazado o no.

## Por que importa esto

Los scanners SAST tienen tasas de falsos positivos que varian mucho segun la herramienta y el tipo de patron. Sin un campo de confianza, el equipo trata todos los hallazgos como igualmente fiables, lo que lleva a dos problemas: invertir tiempo en corregir falsos positivos, o desconfiar del programa entero y empezar a ignorar todo.

La confianza es el campo que permite al equipo distinguir entre "este hallazgo requiere accion inmediata" y "este hallazgo requiere verificacion antes de actuar".

## Que vas a cambiar y por que

Asegurate de que las entradas en `docs/sast-analysis.md` tienen un campo `## Confianza` que va mas alla de etiquetas simples. Alta, media o baja deben ir acompañadas de la razon: que se sabe del flujo de datos, que no se sabe y que llevaria a cambiar la evaluacion.

## Archivo y seccion que debes modificar

- Archivo objetivo: `docs/sast-analysis.md`.
- Revisa las entradas existentes o añade una nueva donde el campo `## Confianza` este bien razonado.

## Cambio base recomendado

```markdown
## Hallazgo

Path traversal en src/files/reader.js linea 34: el path construido con req.params.filename sin normalizacion.

## Regla o fuente

path-traversal (rules/security-rules.yml)

## Severidad

ERROR

## Confianza

Alta — trazado completo desde req.params.filename hasta fs.readFileSync sin normalizacion ni validacion de la ruta resultante. Confirmado con prueba manual: ../../../etc/passwd retorna el archivo en entorno de desarrollo.

## Decision

Correccion inmediata: normalizar la ruta con path.resolve y validar que el resultado este dentro del directorio permitido antes de abrir el archivo.
```

## Que te esta enseñando este cambio

- Una confianza alta no es una impresion: es el resultado de trazar el flujo de datos de principio a fin y confirmar que no hay validacion intermedia. La prueba manual en desarrollo es evidencia adicional que sube la confianza.
- Una confianza media indicaria que el trazado es parcial: se sabe el origen y el destino pero hay una funcion intermedia cuyo comportamiento no se ha verificado completamente.
- Una confianza baja justifica investigacion antes de actuar: el patron coincide pero el contexto no esta claro. En ese caso la decision es "investigar" y no directamente "corregir" o "excepcionar".
- El nivel de confianza determina la urgencia operativa tanto o mas que la severidad: un ERROR de confianza baja puede esperar a verificacion; un WARNING de confianza alta puede necesitar accion inmediata.

## Como adaptarlo correctamente

- Usa "trazado desde X hasta Y" como estructura base para justificar confianza alta.
- Indica explicitamente que informacion falta para justificar confianza media o baja.
- Si la prueba manual confirma el hallazgo, documentalo: es la evidencia mas solida para confianza alta.
- No pongas confianza alta en hallazgos donde el flujo de datos no fue trazado. Eso infla artificialmente la urgencia y erosiona la credibilidad del programa.

## Que deberia verse al terminar

- Al menos una entrada en `docs/sast-analysis.md` tiene una confianza con razonamiento explicito, no solo una etiqueta.
- El equipo puede explicar por que la confianza es alta, media o baja para cada hallazgo documentado.
- Queda claro como el nivel de confianza influye en la decision tomada.
- Los marcadores esperados del paso siguen presentes de forma natural en la configuracion.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-17.py` comprueba este paso contra el archivo configurado.
- El workflow busca `## Hallazgo` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Regla o fuente` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Severidad` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Confianza` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Decision` dentro de `docs/sast-analysis.md`.

## Criterio de finalizacion

El paso 17 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 18.
