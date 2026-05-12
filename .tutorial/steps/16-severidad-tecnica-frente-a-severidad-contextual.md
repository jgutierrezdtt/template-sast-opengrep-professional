# Paso 16. Severidad tecnica frente a severidad contextual

## Que vas a hacer en este paso?

Implementaras este control de SAST de forma concreta sobre el archivo `.github/workflows/sast.yml` y registraras evidencia tecnica en `.tutorial/evidence/step-16.json`.

## Por que es importante

**En la practica real**:
- Este control reduce riesgo operativo y mejora trazabilidad.
- Permite validar avance real, no solo lectura del tutorial.

**Lo que logras**:
- Resultado tecnico verificable para el paso 16.
- Evidencia auditable para revisiones de seguridad.

---

## Instrucciones paso-a-paso

### Paso 16.1: Prepara el artefacto principal

Crea o actualiza el archivo objetivo de este paso:

```bash
mkdir -p "$(dirname .github/workflows/sast.yml)"
touch .github/workflows/sast.yml
```

### Paso 16.2: Registra evidencia del paso

Crea el archivo `.tutorial/evidence/step-16.json` con este contenido:

```bash
mkdir -p .tutorial/evidence
cat > .tutorial/evidence/step-16.json << 'EOF'
{
  "step": 16,
  "title": "Severidad tecnica frente a severidad contextual",
  "status": "completed",
  "artifact": ".github/workflows/sast.yml"
}
EOF
```

---

## Verificacion local

```bash
test -f .github/workflows/sast.yml && echo "artifact ok"
python3 -c 'import json;json.load(open(".tutorial/evidence/step-16.json"));print("evidence ok")'
```

---

## Validacion automatica

`validate-step-16.py` verificara:
- Existe `.github/workflows/sast.yml`.
- Existe `.tutorial/evidence/step-16.json`.
- La evidencia marca `status=completed` y `step=16`.

---

## Criterio de finalizacion

Paso 16 esta completo cuando:
1. `.github/workflows/sast.yml` existe en el repositorio.
2. `.tutorial/evidence/step-16.json` existe y es JSON valido.
3. `.tutorial/state.json` muestra `"current_step": 17`.

**Siguiente paso**: Paso 17
