# Paso 16. Severidad tecnica frente a severidad contextual

## Objetivo de aprendizaje

Distinguir entre la severidad que asigna la herramienta (tecnica) y la severidad que decide el equipo segun el contexto real del repositorio (contextual). Saber cuándo ajustar una y cuándo respetar la otra.

## Por que importa esto

Los escáneres SAST asignan severidad tecnica basada en el tipo de patron detectado, no en el contexto de uso. Un SQL injection es ERROR independientemente de si el repositorio es un servicio de produccion o un entorno de demostracion sin datos reales.

Si el equipo trata todas las severidades tecnicas como definitivas, acaba con backlogs de seguridad que no reflejan el riesgo real. Si las ignora completamente en favor del contexto, pierde la señal que aporta la herramienta.

El equilibrio es usar la severidad tecnica como primera señal y ajustarla con el contexto del repositorio para llegar a una severidad contextual que guie la accion real.

## Que vas a cambiar y por que

Añade una entrada en `docs/sast-analysis.md` donde la severidad contextual difiera de la tecnica y quede documentado el razonamiento. No es suficiente con cambiar la etiqueta: el campo `## Decision` debe explicar por que el contexto justifica el ajuste.

## Archivo y seccion que debes modificar

- Archivo objetivo: `docs/sast-analysis.md`.
- Añade o actualiza una entrada donde los campos `## Severidad` y `## Decision` reflejen juntos la distincion entre severidad tecnica y contextual.

## Cambio base recomendado

```markdown
## Hallazgo

Deserializacion insegura en src/legacy/importer.js linea 156.

## Regla o fuente

unsafe-deserialization (rules/security-rules.yml)

## Severidad

ERROR (tecnica) — MEDIUM (contextual): el modulo solo es accesible desde la red interna y requiere autenticacion previa de administrador.

## Confianza

Media — el importer es accesible solo por admins autenticados, pero el modulo legacy no tiene tests de integracion que confirmen los controles de acceso.

## Decision

Correccion en proximo trimestre: la ventana de exposicion es baja pero el patron es explotable si los controles de acceso fallaran. Se añade test de integracion que verifique la autenticacion previa como medida de compensacion inmediata.
```

## Que te esta enseñando este cambio

- El campo `## Severidad` puede registrar ambas severidades para que quede claro que la decision no ignora la señal tecnica sino que la ajusta con justificacion.
- Una confianza media refleja que hay un factor de incertidumbre: los controles de acceso no estan cubiertos por tests. Esa incertidumbre influye en la decision final aunque la exposicion sea baja.
- Una medida de compensacion inmediata (test de integracion) permite bajar la urgencia de la correccion sin ignorar el riesgo. Eso es una decision de riesgo informada, no una evasion.
- El trimestre como horizonte de correccion es mas honesto que "pendiente indefinidamente" y permite trazabilidad en el reporting.

## Como adaptarlo correctamente

- No uses la severidad contextual para eliminar sistematicamente ERRORs del backlog. Cada ajuste hacia abajo necesita una justificacion mas solida, no menos.
- Si ajustas la severidad contextual hacia arriba respecto a la tecnica (un WARNING que en realidad es critico por contexto), documenta igual el razonamiento.
- La confianza media o baja en un hallazgo de severidad alta justifica investigacion adicional antes de tomar la decision, no descarte directo.
- Este campo es la base del reporting tecnico del paso 28, donde los receptores necesitan ver la distincion entre lo que dice la herramienta y lo que decide el equipo.

## Que deberia verse al terminar

- Al menos una entrada en `docs/sast-analysis.md` muestra las dos severidades y el razonamiento del ajuste.
- La decision es coherente con la severidad contextual resultante, no con la tecnica aislada.
- Queda claro que el ajuste fue deliberado y no es una forma de ignorar el hallazgo.
- Los marcadores esperados del paso siguen presentes de forma natural en la configuracion.

## Que valida el workflow automaticamente

- `validate-steps.yml` se ejecuta con `push`, `pull_request` y `workflow_dispatch`.
- `scripts/validate-step-16.py` comprueba este paso contra el archivo configurado.
- El workflow busca `## Hallazgo` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Regla o fuente` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Severidad` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Confianza` dentro de `docs/sast-analysis.md`.
- El workflow busca `## Decision` dentro de `docs/sast-analysis.md`.

## Criterio de finalizacion

El paso 16 queda completado cuando el workflow de GitHub Actions valida este cambio sin errores.

Siguiente paso: Paso 17.
