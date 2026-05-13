# Paso 2. Primer escaneo con opengrep

## Objetivo de aprendizaje

Entender qué aporta el primer escaneo con OpenGrep. El objetivo de este paso no es construir todavía la mejor regla del laboratorio, sino comprobar que existe una señal básica, que el motor puede cargarla y que tú sabes relacionar esa regla con los resultados que aparezcan.

## Que vas a cambiar y por que

Vas a mantener en `rules/security-rules.yml` una regla muy simple para preparar el primer recorrido completo: regla, escaneo y lectura inicial del resultado. La clave pedagógica del paso es aprender que un escaneo útil empieza por una señal comprensible. Si la primera regla ya nace confusa, el equipo no sabrá si un hallazgo viene de una detección real, de una mala configuración o de una política mal definida.

## Archivo y seccion que debes modificar

- Archivo objetivo: `rules/security-rules.yml`.
- Este paso sigue trabajando sobre la regla mínima del arranque para que el primer escaneo tenga una referencia clara.
- Piensa el cambio como preparación del flujo completo: definir la regla, lanzar el análisis y reconocer después qué señal produjo.

## Cambio base recomendado

No copies este bloque como solución final. Aquí interesa que la regla sea lo bastante simple como para entender qué está pasando durante el primer escaneo.

```yaml
rules:
  - id: demo-rule
    severity: WARNING
```

## Que deberias observar en este primer escaneo

- `id: demo-rule` te permite reconocer con facilidad qué regla disparó un resultado.
- `severity: WARNING` evita que el primer contacto con el análisis se convierta de inmediato en un bloqueo duro; primero hay que aprender a leer la señal.
- La simplicidad de la regla ayuda a separar problemas del motor, de la configuración o del código analizado.

## Como adaptarlo correctamente

- Mantén la regla lo bastante simple como para que cualquier resultado sea fácil de atribuir a esta primera configuración.
- No intentes endurecer aún la política; en este paso importa validar el circuito completo de análisis.
- Usa `WARNING` como una señal de arranque que invite a observar y entender antes de bloquear.
- El aprendizaje real aquí es conectar la regla con el comportamiento del escaneo.

## Que deberia verse al terminar

- El lector entiende qué regla se usa para arrancar el análisis y por qué es deliberadamente simple.
- Queda claro que el primer escaneo sirve para validar el flujo, no para declarar madura la cobertura SAST.
- La relación entre la regla definida y los resultados esperados del análisis se vuelve explícita.
- Los marcadores esperados del paso siguen presentes de forma natural en la configuración.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-02.py` comprueba este paso contra el archivo configurado.
- El workflow busca `rules:` dentro de `rules/security-rules.yml`.
- El workflow busca `id: demo-rule` dentro de `rules/security-rules.yml`.
- El workflow busca `severity: WARNING` dentro de `rules/security-rules.yml`.

## Criterio de finalizacion

El paso 2 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 3.
