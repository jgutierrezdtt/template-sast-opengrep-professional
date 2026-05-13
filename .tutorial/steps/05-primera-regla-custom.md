# Paso 5. Primera regla custom

## Objetivo de aprendizaje

Escribir una regla SAST propia, no reutilizar la que viene por defecto. Este paso enseña a elegir un patrón inseguro real, definir su mensaje de forma legible y decidir la severidad antes de conectarla al pipeline.

## Por que importa esto

Las reglas por defecto cubren vulnerabilidades conocidas en el ecosistema general. No detectan los patrones inseguros que son propios de la arquitectura o del lenguaje del equipo. Una organizacion que solo usa reglas de terceros tiene un programa SAST que no conoce su propio codigo.

Escribir la primera regla custom es el momento en que el equipo pasa de consumidor de alertas a autor de controles.

## Que vas a cambiar y por que

Añade en `rules/security-rules.yml` una regla que el equipo pudiera llevar a produccion hoy. No un ejemplo de manual: una deteccion que tenga `id` estable, `message` que explique el riesgo, `severity` que refleje la gravedad real y `pattern` que no dispare en todos los archivos del repositorio.

La diferencia entre esta regla y la del paso 4 es que aqui ya sabes qué estas buscando y por que merece ser una regla propia.

## Archivo y seccion que debes modificar

- Archivo objetivo: `rules/security-rules.yml`.
- Si el archivo no existe todavia, créalo y añade la regla como primer elemento.
- El cambio es evolutivo: esta regla convivirá con las siguientes sin duplicar ids.

## Cambio base recomendado

No copies este bloque como solucion final. Usalo para entender qué elementos hacen que una regla custom sea operativa desde el primer dia.

```yaml
rules:
  - id: insecure-eval
    message: Evita eval con input controlado por usuario
    severity: ERROR
    languages: [javascript]
    pattern: eval($X)
```

## Que te esta enseñando este cambio

- `id: insecure-eval` es el nombre del control. Debe ser estable porque los sistemas de excepciones, el reporting y los dashboards lo van a referenciar. Cambiarlo rompe el historial.
- `message:` es lo que ve el desarrollador cuando falla el check. Si el mensaje no explica el riesgo, el desarrollador no sabe si ignorarlo o remediarlo.
- `severity: ERROR` significa que el equipo ha decidido que este patron merece atencion inmediata, no solo observacion. Usalo cuando el patron sea explotable directamente.
- `languages: [javascript]` acota la regla a un ecosistema. Sin esto, OpenGrep intentara aplicarla a todos los lenguajes del repositorio.
- `pattern: eval($X)` usa una metavariable para capturar cualquier argumento pasado a `eval`. No es un literal fijo: es una plantilla de patron.

## Como adaptarlo correctamente

- Elige un patron que ya hayas visto en el codigo del repositorio, no uno hipotetico.
- El mensaje debe ser especifico: "Evita eval con input controlado por usuario" es mejor que "Uso de eval".
- Si el repositorio no tiene JavaScript, cambia `languages` y `pattern` al lenguaje real.
- No escribas un `id` generico como `rule-001`. Un revisor que lea el id debe entender qué detecta sin abrir el archivo.

## Que deberia verse al terminar

- La regla tiene `id`, `message`, `severity`, `languages` y `pattern`.
- Cualquier revisor puede leer la regla y entender qué detecta y por que es un riesgo.
- El patron no es tan amplio que convierta archivos de test o de configuracion en falsos positivos.
- El equipo podria llevar esta regla a produccion sin mas explicacion.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-05.py` comprueba este paso contra el archivo configurado.
- El workflow busca `rules:` dentro de `rules/security-rules.yml`.
- El workflow busca `id: insecure-eval` dentro de `rules/security-rules.yml`.
- El workflow busca `message:` dentro de `rules/security-rules.yml`.
- El workflow busca `severity: ERROR` dentro de `rules/security-rules.yml`.
- El workflow busca `pattern: eval($X)` dentro de `rules/security-rules.yml`.

## Criterio de finalizacion

El paso 5 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 6.
