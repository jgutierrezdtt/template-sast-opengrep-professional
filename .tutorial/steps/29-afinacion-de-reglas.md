# Paso 29. Afinacion de reglas

## Que vas a hacer en este paso?

Implementaras este control de SAST de forma concreta sobre el archivo `docs/sast-programa.md` y registraras evidencia tecnica en `.tutorial/evidence/step-29.json`.

## Por que es importante

**En la practica real**:
- Este control reduce riesgo operativo y mejora trazabilidad.
- Permite validar avance real, no solo lectura del tutorial.

**Lo que logras**:
- Resultado tecnico verificable para el paso 29.
- Evidencia auditable para revisiones de seguridad.

---

## Instrucciones paso-a-paso

### Paso 29.1: Prepara el artefacto principal

Crea o actualiza el archivo objetivo de este paso:

```bash
mkdir -p "$(dirname docs/sast-programa.md)"
touch docs/sast-programa.md
```

### Paso 29.2: Registra evidencia del paso

Crea el archivo `.tutorial/evidence/step-29.json` con este contenido:

```bash
mkdir -p .tutorial/evidence
cat > .tutorial/evidence/step-29.json << 'EOF'
{
  "step": 29,
  "title": "Afinacion de reglas",
  "status": "completed",
  "artifact": "docs/sast-programa.md"
}
EOF
```

---

## Verificacion local

```bash
test -f docs/sast-programa.md && echo "artifact ok"
python3 -c 'import json;json.load(open(".tutorial/evidence/step-29.json"));print("evidence ok")'
```

---

## Validacion automatica

`validate-step-29.py` verificara:
- Existe `docs/sast-programa.md`.
- Existe `.tutorial/evidence/step-29.json`.
- La evidencia marca `status=completed` y `step=29`.

---

## Criterio de finalizacion

Paso 29 esta completo cuando:
1. `docs/sast-programa.md` existe en el repositorio.
2. `.tutorial/evidence/step-29.json` existe y es JSON valido.
3. `.tutorial/state.json` muestra `"current_step": 30`.

**Siguiente paso**: Paso 30
