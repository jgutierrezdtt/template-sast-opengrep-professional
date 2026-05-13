# Paso 29. Afinacion de reglas

## Objetivo de aprendizaje

Mejorar la precision de las reglas existentes reduciendo falsos positivos sin perder detecciones reales. La afinacion es la actividad que convierte un conjunto de reglas de arranque en un conjunto de reglas de produccion.

## Por que importa esto

Una regla que genera muchos falsos positivos pierde credibilidad rapidamente. El equipo de desarrollo aprende a ignorarla. Una regla que genera muchos falsos negativos (no detecta los casos reales) da una falsa sensacion de seguridad.

La afinacion es el proceso iterativo que lleva una regla desde "detecta el patron" hasta "detecta el patron de forma util en nuestro repositorio especifico".

Un programa SAST maduro no tiene mas reglas que uno inmaduro: tiene reglas mas precisas.

## Que vas a cambiar y por que

Actualiza al menos una regla en `rules/security-rules.yml` para añadir un refinamiento que mejore su precision: una ruta de exclusion, una condicion adicional, un mensaje mas especifico o una metavariable mas acotada. El cambio debe estar justificado por un hallazgo real del programa.

## Archivo y seccion que debes modificar

- Archivo objetivo: `rules/security-rules.yml`.
- Edita una regla existente para añadir un refinamiento de precision.
- Documenta en la regla el motivo del refinamiento.

## Cambio base recomendado

```yaml
rules:
  - id: insecure-eval
    message: Evita eval con input controlado por usuario. Alternativa: usa una funcion de despacho con allowlist de operaciones permitidas.
    severity: ERROR
    languages: [javascript]
    pattern: eval($X)
    paths:
      exclude:
        - "**/__tests__/**"
        - "**/test/**"
        - "**/fixtures/**"
```

## Que te esta enseñando este cambio

- `paths.exclude` con rutas de test es la afinacion mas comun y mas util. Los archivos de test suelen usar `eval` de forma segura y controlada. Excluirlos reduce el ruido sin perder detecciones en codigo de produccion.
- El `message:` actualizado ahora incluye la alternativa: "usa una funcion de despacho con allowlist". Eso convierte la regla en orientacion de desarrollo, no solo en una señal de parada.
- La lista de exclusiones usa globbing (`**/__tests__/**`) para cubrir estructuras de directorio anidadas. Usar rutas fijas seria menos robusto.
- Añadir la alternativa en el mensaje es una afinacion de calidad, no de precision tecnica. Pero es igualmente importante: reduce el tiempo que el desarrollador tarda en saber que hacer despues de ver el hallazgo.

## Como adaptarlo correctamente

- Basa cada afinacion en un hallazgo real del programa: "teniamos X falsos positivos en tests" es la justificacion. No afines de forma preventiva sin datos.
- Documenta en el historial de git por que se añadio cada exclusion. Un mes despues, nadie recordara si la exclusion fue por falso positivo confirmado o por conveniencia.
- No uses exclusiones muy amplias como `src/legacy/**` sin analizar cada archivo del directorio. Una exclusion amplia puede silenciar hallazgos reales.
- Despues de cada afinacion, ejecuta el scanner sobre el repositorio y compara el numero de hallazgos antes y despues. Si bajo mas de lo esperado, la exclusion puede ser demasiado amplia.

## Que deberia verse al terminar

- Al menos una regla en `rules/security-rules.yml` tiene un refinamiento documentado que mejora su precision.
- El refinamiento esta justificado por la experiencia del programa, no por conveniencia.
- El `message:` de la regla incluye la alternativa recomendada.
- Los markers esperados del paso siguen presentes de forma natural en el archivo.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-29.py` comprueba este paso contra el archivo configurado.
- El workflow busca `rules:` dentro de `rules/security-rules.yml`.
- El workflow busca `id: insecure-eval` dentro de `rules/security-rules.yml`.
- El workflow busca `message:` dentro de `rules/security-rules.yml`.
- El workflow busca `severity: ERROR` dentro de `rules/security-rules.yml`.
- El workflow busca `pattern: eval($X)` dentro de `rules/security-rules.yml`.

## Criterio de finalizacion

El paso 29 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 30.
