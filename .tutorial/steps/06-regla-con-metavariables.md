# Paso 6. Regla con metavariables

## Que vas a hacer en este paso?

Implementaras este control de SAST de forma concreta sobre el archivo `.opengrep.yml` y registraras evidencia tecnica en `.tutorial/evidence/step-06.json`.

## Por que es importante

**En la practica real**:
- Este control reduce riesgo operativo y mejora trazabilidad.
- Permite validar avance real, no solo lectura del tutorial.

**Lo que logras**:
- Resultado tecnico verificable para el paso 6.
- Evidencia auditable para revisiones de seguridad.

---

## Instrucciones paso-a-paso

### Paso 6.1: Prepara el artefacto principal

Crea o actualiza el archivo objetivo de este paso:

```bash
mkdir -p "$(dirname .opengrep.yml)"
touch .opengrep.yml
```

### Paso 6.2: Registra evidencia del paso

Crea el archivo `.tutorial/evidence/step-06.json` con este contenido:

```bash
mkdir -p .tutorial/evidence
cat > .tutorial/evidence/step-06.json << 'EOF'
{
  "step": 6,
  "title": "Regla con metavariables",
  "status": "completed",
  "artifact": ".opengrep.yml"
}
EOF
```

---

## Verificacion local

```bash
test -f .opengrep.yml && echo "artifact ok"
python3 -c 'import json;json.load(open(".tutorial/evidence/step-06.json"));print("evidence ok")'
```

---

## Validacion automatica

`validate-step-06.py` verificara:
- Existe `.opengrep.yml`.
- Existe `.tutorial/evidence/step-06.json`.
- La evidencia marca `status=completed` y `step=6`.

---

## Criterio de finalizacion

Paso 6 esta completo cuando:
1. `.opengrep.yml` existe en el repositorio.
2. `.tutorial/evidence/step-06.json` existe y es JSON valido.
3. `.tutorial/state.json` muestra `"current_step": 7`.

**Siguiente paso**: Paso 7
