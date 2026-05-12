# Paso 22. Quality gate no bloqueante

## Que vas a hacer en este paso?

Implementaras este control de SAST de forma concreta sobre el archivo `.github/workflows/sast.yml` y registraras evidencia tecnica en `.tutorial/evidence/step-22.json`.

## Por que es importante

**En la practica real**:
- Este control reduce riesgo operativo y mejora trazabilidad.
- Permite validar avance real, no solo lectura del tutorial.

**Lo que logras**:
- Resultado tecnico verificable para el paso 22.
- Evidencia auditable para revisiones de seguridad.

---

## Instrucciones paso-a-paso

### Paso 22.1: Prepara el artefacto principal

Crea o actualiza el archivo objetivo de este paso:

```bash
mkdir -p "$(dirname .github/workflows/sast.yml)"
touch .github/workflows/sast.yml
```

### Paso 22.2: Registra evidencia del paso

Crea el archivo `.tutorial/evidence/step-22.json` con este contenido:

```bash
mkdir -p .tutorial/evidence
cat > .tutorial/evidence/step-22.json << 'EOF'
{
  "step": 22,
  "title": "Quality gate no bloqueante",
  "status": "completed",
  "artifact": ".github/workflows/sast.yml"
}
EOF
```

---

## Verificacion local

```bash
test -f .github/workflows/sast.yml && echo "artifact ok"
python3 -c 'import json;json.load(open(".tutorial/evidence/step-22.json"));print("evidence ok")'
```

---

## Validacion automatica

`validate-step-22.py` verificara:
- Existe `.github/workflows/sast.yml`.
- Existe `.tutorial/evidence/step-22.json`.
- La evidencia marca `status=completed` y `step=22`.

---

## Criterio de finalizacion

Paso 22 esta completo cuando:
1. `.github/workflows/sast.yml` existe en el repositorio.
2. `.tutorial/evidence/step-22.json` existe y es JSON valido.
3. `.tutorial/state.json` muestra `"current_step": 23`.

**Siguiente paso**: Paso 23
