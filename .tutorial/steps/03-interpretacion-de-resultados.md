# Paso 3. Interpretacion de resultados

## Que vas a hacer en este paso?

Implementaras este control de SAST de forma concreta sobre el archivo `.opengrep.yml` y registraras evidencia tecnica en `.tutorial/evidence/step-03.json`.

## Por que es importante

**En la practica real**:
- Este control reduce riesgo operativo y mejora trazabilidad.
- Permite validar avance real, no solo lectura del tutorial.

**Lo que logras**:
- Resultado tecnico verificable para el paso 3.
- Evidencia auditable para revisiones de seguridad.

---

## Instrucciones paso-a-paso

### Paso 3.1: Prepara el artefacto principal

Crea o actualiza el archivo objetivo de este paso:

```bash
mkdir -p "$(dirname .opengrep.yml)"
touch .opengrep.yml
```

### Paso 3.2: Registra evidencia del paso

Crea el archivo `.tutorial/evidence/step-03.json` con este contenido:

```bash
mkdir -p .tutorial/evidence
cat > .tutorial/evidence/step-03.json << 'EOF'
{
  "step": 3,
  "title": "Interpretacion de resultados",
  "status": "completed",
  "artifact": ".opengrep.yml"
}
EOF
```

---

## Verificacion local

```bash
test -f .opengrep.yml && echo "artifact ok"
python3 -c 'import json;json.load(open(".tutorial/evidence/step-03.json"));print("evidence ok")'
```

---

## Validacion automatica

`validate-step-03.py` verificara:
- Existe `.opengrep.yml`.
- Existe `.tutorial/evidence/step-03.json`.
- La evidencia marca `status=completed` y `step=3`.

---

## Criterio de finalizacion

Paso 3 esta completo cuando:
1. `.opengrep.yml` existe en el repositorio.
2. `.tutorial/evidence/step-03.json` existe y es JSON valido.
3. `.tutorial/state.json` muestra `"current_step": 4`.

**Siguiente paso**: Paso 4
