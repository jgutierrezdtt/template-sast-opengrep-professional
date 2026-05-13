# Paso 21. Exportacion SARIF

## Objetivo de aprendizaje

Entender que SARIF no es solo un formato de exportacion: es el estandar que permite integrar los hallazgos SAST con GitHub Code Scanning, comparar resultados entre herramientas y alimentar sistemas de gestion de vulnerabilidades externos.

## Por que importa esto

Sin exportacion SARIF, los hallazgos de OpenGrep existen solo en el log del pipeline. Nadie puede ver el historial de hallazgos, nadie puede ver si un hallazgo nuevo fue introducido por un PR especifico, y no hay forma de integrar los resultados con otros sistemas de la organizacion.

SARIF convierte una ejecucion de scanner en un resultado estructurado, portable y comparable con el tiempo.

## Que vas a cambiar y por que

Actualiza `.github/workflows/sast.yml` para añadir la exportacion del resultado en formato SARIF y subirlo como artefacto del workflow. Este cambio no altera los triggers ni las reglas: solo añade la capa de observabilidad que hace que los resultados sean utiles mas alla del log.

## Archivo y seccion que debes modificar

- Archivo objetivo: `.github/workflows/sast.yml`.
- Añade los pasos de exportacion SARIF y subida de artefacto despues del paso de escaneo.

## Cambio base recomendado

```yaml
      - name: Export SARIF
        run: |
          opengrep scan --config rules/security-rules.yml src/ --sarif > results.sarif
        continue-on-error: true

      - name: Upload SARIF
        uses: actions/upload-artifact@v4
        with:
          name: sast-results-${{ github.sha }}
          path: results.sarif
          retention-days: 30
```

## Que te esta enseñando este cambio

- `--sarif > results.sarif` produce un archivo en formato estandar que GitHub Code Scanning puede importar directamente. Sin este flag, el resultado solo existe como texto en el log.
- `continue-on-error: true` en el paso de exportacion evita que el workflow falle si el scanner detecta hallazgos y los exporta con exit code no-cero. La gestion del fallo se separa de la exportacion del resultado.
- `name: sast-results-${{ github.sha }}` nombra el artefacto con el SHA del commit, lo que permite correlacionar resultados con el estado exacto del codigo en ese momento.
- `retention-days: 30` define cuanto tiempo GitHub guarda el artefacto. 30 dias es un balance entre visibilidad historica y coste de almacenamiento.

## Como adaptarlo correctamente

- Si quieres integrar con GitHub Code Scanning, el siguiente paso seria usar `github/codeql-action/upload-sarif` en lugar de `upload-artifact`. El tutorial usa artefactos para no requerir permisos adicionales.
- No uses `continue-on-error: true` en el paso de escaneo si quieres que el pipeline falle cuando hay hallazgos criticos. Ese comportamiento lo configuras en el paso 23.
- Guarda los SARIFs con el SHA del commit como parte del nombre: eso es lo que permite reconstruir el estado de seguridad en cualquier punto del historial.
- El archivo `results.sarif` es la entrada para las metricas del paso 26 y para el reporting tecnico del paso 28.

## Que deberia verse al terminar

- `.github/workflows/sast.yml` genera un archivo `results.sarif` en cada ejecucion.
- El artefacto se sube con el SHA del commit como parte del nombre.
- El equipo puede explicar que ventajas tiene el formato SARIF respecto a leer el log del pipeline.
- Los markers esperados del paso aparecen de forma natural en el workflow.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-21.py` comprueba este paso contra el archivo configurado.
- El workflow busca `Export SARIF` dentro de `.github/workflows/sast.yml`.
- El workflow busca `--sarif` dentro de `.github/workflows/sast.yml`.
- El workflow busca `results.sarif` dentro de `.github/workflows/sast.yml`.

## Criterio de finalizacion

El paso 21 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 22.
