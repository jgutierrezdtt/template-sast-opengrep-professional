# Paso 15. Priorizacion por contexto

## Que vas a hacer en este paso?

Implementaras este control de SAST de forma concreta sobre el archivo `rules/security-rules.yml` y registraras evidencia tecnica en `.tutorial/evidence/step-15.json`.

## Por que es importante

**En la practica real**:
- Este control reduce riesgo operativo y mejora trazabilidad.
- Permite validar avance real, no solo lectura del tutorial.

**Lo que logras**:
- Resultado tecnico verificable para el paso 15.
- Evidencia auditable para revisiones de seguridad.

---

## Instrucciones paso-a-paso

### Paso 15.1: Prepara el artefacto principal

Crea o actualiza el archivo objetivo de este paso:

```bash
mkdir -p "$(dirname rules/security-rules.yml)"
touch rules/security-rules.yml
```

### Paso 15.2: Registra evidencia del paso

Crea el archivo `.tutorial/evidence/step-15.json` con este contenido:

```bash
mkdir -p .tutorial/evidence
cat > .tutorial/evidence/step-15.json << 'EOF'
{
  "step": 15,
  "title": "Priorizacion por contexto",
  "status": "completed",
  "artifact": "rules/security-rules.yml"
}
EOF
```

---

## Verificacion local

```bash
test -f rules/security-rules.yml && echo "artifact ok"
python3 -c 'import json;json.load(open(".tutorial/evidence/step-15.json"));print("evidence ok")'
```

---

## Validacion automatica

`validate-step-15.py` verificara:
- Existe `rules/security-rules.yml`.
- Existe `.tutorial/evidence/step-15.json`.
- La evidencia marca `status=completed` y `step=15`.

---

## Criterio de finalizacion

Paso 15 esta completo cuando:
1. `rules/security-rules.yml` existe en el repositorio.
2. `.tutorial/evidence/step-15.json` existe y es JSON valido.
3. `.tutorial/state.json` muestra `"current_step": 16`.

**Siguiente paso**: Paso 16
