# Paso 28. Reporting tecnico

## Que vas a hacer en este paso?

Implementaras este control de SAST de forma concreta sobre el archivo `docs/sast-programa.md` y registraras evidencia tecnica en `.tutorial/evidence/step-28.json`.

## Por que es importante

**En la practica real**:
- Este control reduce riesgo operativo y mejora trazabilidad.
- Permite validar avance real, no solo lectura del tutorial.

**Lo que logras**:
- Resultado tecnico verificable para el paso 28.
- Evidencia auditable para revisiones de seguridad.

---

## Instrucciones paso-a-paso

### Paso 28.1: Prepara el artefacto principal

Crea o actualiza el archivo objetivo de este paso:

```bash
mkdir -p "$(dirname docs/sast-programa.md)"
touch docs/sast-programa.md
```

### Paso 28.2: Registra evidencia del paso

Crea el archivo `.tutorial/evidence/step-28.json` con este contenido:

```bash
mkdir -p .tutorial/evidence
cat > .tutorial/evidence/step-28.json << 'EOF'
{
  "step": 28,
  "title": "Reporting tecnico",
  "status": "completed",
  "artifact": "docs/sast-programa.md"
}
EOF
```

---

## Verificacion local

```bash
test -f docs/sast-programa.md && echo "artifact ok"
python3 -c 'import json;json.load(open(".tutorial/evidence/step-28.json"));print("evidence ok")'
```

---

## Validacion automatica

`validate-step-28.py` verificara:
- Existe `docs/sast-programa.md`.
- Existe `.tutorial/evidence/step-28.json`.
- La evidencia marca `status=completed` y `step=28`.

---

## Criterio de finalizacion

Paso 28 esta completo cuando:
1. `docs/sast-programa.md` existe en el repositorio.
2. `.tutorial/evidence/step-28.json` existe y es JSON valido.
3. `.tutorial/state.json` muestra `"current_step": 29`.

**Siguiente paso**: Paso 29
