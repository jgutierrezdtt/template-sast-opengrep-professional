# Paso 3. Interpretacion de resultados

## Objetivo de aprendizaje

Aprender a convertir una alerta SAST en un análisis útil. Un resultado de OpenGrep por sí solo no te dice qué hacer; este paso te enseña a descomponerlo en hallazgo, origen, severidad, confianza y decisión para que el equipo pueda actuar con criterio.

## Que vas a cambiar y por que

Vas a estructurar `docs/sast-analysis.md` para que un hallazgo deje de ser una línea aislada en la salida del escáner. La finalidad del paso es obligarte a responder cinco preguntas concretas: qué se encontró, de dónde viene, qué gravedad técnica aparenta tener, cuánta confianza merece y qué decisión operativa debe tomarse. Esa disciplina es la que separa un escaneo ruidoso de un programa SAST gobernable.

## Archivo y seccion que debes modificar

- Archivo objetivo: `docs/sast-analysis.md`.
- Este documento no sirve para copiar la salida del escáner, sino para interpretarla.
- Piensa la edición como una plantilla de análisis que otro revisor pueda leer y entender sin volver a ejecutar nada.

## Cambio base recomendado

No copies este bloque como un formulario vacío. Úsalo como estructura para obligarte a pensar cada hallazgo antes de decidir si se corrige, se acepta o se sigue investigando.

```markdown
## Hallazgo
## Regla o fuente
## Severidad
## Confianza
## Decision
```

## Como leer cada seccion

- `## Hallazgo` describe el comportamiento inseguro observado, no el nombre del archivo sin más.
- `## Regla o fuente` conecta la señal con la regla, consulta o fuente que originó la detección.
- `## Severidad` expresa el posible impacto técnico si el hallazgo es real.
- `## Confianza` indica cuán probable es que la alerta represente un problema verdadero y no ruido.
- `## Decision` fuerza una conclusión operativa: corregir, investigar más, aceptar con justificación o crear excepción.

## Como adaptarlo correctamente

- No trates todas las alertas como iguales; este documento existe precisamente para distinguirlas.
- Usa `## Confianza` para evitar decisiones precipitadas sobre hallazgos débiles o ambiguos.
- Haz que `## Decision` termine en una acción defendible y no en una frase neutra.
- El objetivo es que cualquiera pueda entender por qué el equipo hizo lo que hizo con ese resultado.

## Que deberia verse al terminar

- El documento deja claro cómo pasar de una alerta a una decisión.
- El lector entiende que severidad y confianza no significan lo mismo y que ambas influyen en la respuesta.
- La plantilla resultante sirve para discutir hallazgos con desarrollo, seguridad o gestión sin perder contexto.
- Los marcadores esperados del paso siguen presentes de forma natural en la configuración.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-03.py` comprueba este paso contra el archivo configurado.
- El workflow busca `## Hallazgo` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Regla o fuente` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Severidad` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Confianza` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Decision` dentro de `docs/sast-analysis.md`.

## Criterio de finalizacion

El paso 3 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 4.
