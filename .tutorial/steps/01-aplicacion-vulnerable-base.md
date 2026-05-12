# Paso 1. Aplicacion vulnerable base

## Que vas a hacer en este paso?

Implementaras este control de SAST de forma concreta sobre el archivo `.opengrep.yml` y registraras evidencia tecnica en `.tutorial/evidence/step-01.json`.

## Por que es importante

**En la practica real**:
- Este control reduce riesgo operativo y mejora trazabilidad.
- Permite validar avance real, no solo lectura del tutorial.

**Lo que logras**:
- Resultado tecnico verificable para el paso 1.
- Evidencia auditable para revisiones de seguridad.

---

## Instrucciones paso-a-paso

### Paso 1.1: Prepara el artefacto principal

Crea o actualiza el archivo objetivo de este paso:

```bash
mkdir -p "$(dirname .opengrep.yml)"
touch .opengrep.yml
```

### Paso 1.2: Registra evidencia del paso

Crea el archivo `.tutorial/evidence/step-01.json` con este contenido:

```bash
mkdir -p .tutorial/evidence
cat > .tutorial/evidence/step-01.json << 'EOF'
{
  "step": 1,
  "title": "Aplicacion vulnerable base",
  "status": "completed",
  "artifact": ".opengrep.yml"
}
EOF
```

---

## Verificacion local

```bash
test -f .opengrep.yml && echo "artifact ok"
python3 -c 'import json;json.load(open(".tutorial/evidence/step-01.json"));print("evidence ok")'
```

---

## Validacion automatica

`validate-step-01.py` verificara:
- Existe `.opengrep.yml`.
- Existe `.tutorial/evidence/step-01.json`.
- La evidencia marca `status=completed` y `step=1`.

---

## Criterio de finalizacion

Paso 1 esta completo cuando:
1. `.opengrep.yml` existe en el repositorio.
2. `.tutorial/evidence/step-01.json` existe y es JSON valido.
3. `.tutorial/state.json` muestra `"current_step": 2`.

**Siguiente paso**: Paso 2
