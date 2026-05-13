# Paso 3. Interpretacion de resultados

## Objetivo de aprendizaje

Este paso introduce la interpretación de resultados SAST y debe dejar un cambio comprensible en `docs/sast-analysis.md`.

## Que vas a cambiar y por que

Actualiza `docs/sast-analysis.md` para que un hallazgo de SAST no quede reducido a una alerta sin contexto. En este paso el documento debe ayudarte a responder qué se encontró, qué regla lo originó, qué severidad y confianza tiene y qué decisión corresponde tomar.

## Archivo y seccion que debes modificar

- Archivo objetivo: `docs/sast-analysis.md`.
- Aplícalo en la parte del archivo que corresponde al título del paso.
- Si el archivo aún no existe, créalo con este contenido inicial y luego evoluciona desde ahí en los siguientes pasos.

## Cambio base recomendado

Este bloque no es para pegar a ciegas: úsalo como punto de partida y ajústalo al contexto del repositorio.

```markdown
## Hallazgo
## Regla o fuente
## Severidad
## Confianza
## Decision
```

## Como adaptarlo correctamente

- Mantén el cambio pequeño y centrado en una sola idea por paso.
- Usa `## Regla o fuente` para conectar el hallazgo con la regla que lo detectó o con su origen.
- Usa `## Confianza` para distinguir señal sólida de hallazgo que necesita revisión adicional.
- Haz que `## Decision` cierre el análisis con una acción clara y no con una descripción pasiva.
- Evita añadir configuración que no esté relacionada con el objetivo del paso.

## Que deberia verse al terminar

- La intención del cambio se entiende leyendo el archivo.
- El archivo muestra el control sin depender de comentarios ambiguos.
- Los marcadores esperados del paso aparecen de forma natural en la configuración.
- El documento ya sirve para convertir resultados de OpenGrep en decisiones operables.

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
