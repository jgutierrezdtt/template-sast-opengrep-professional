# SAST OpenGrep Professional

Tutorial profesional de analisis estatico con OpenGrep.

## Que aprenderas

| Paso | Tema | Herramienta | Nivel |
|------|------|-------------|-------|
| 0 | Introduccion | — | Base |
| 1 | Aplicacion vulnerable base | Python / Node | Base |
| 2 | Primer escaneo con OpenGrep | OpenGrep | Base |
| 3 | Interpretacion de resultados | SARIF | Base |
| 4 | Reglas por defecto | OpenGrep rulesets | Medio |
| 5 | Primera regla custom | OpenGrep YAML | Medio |
| 6 | Regla con metavariables | OpenGrep patterns | Medio |
| 7 | Regla con exclusiones | OpenGrep paths | Medio |
| 8 | Falso positivo documentado | nosemgrep | Avanzado |
| 9 | Gestion de excepciones | exceptions.yml | Avanzado |
| 10 | Excepciones con caducidad | exceptions.yml | Avanzado |
| 11 | Excepciones con owner | exceptions.yml | Avanzado |
| 12 | Excepciones con justificacion | exceptions.yml | Avanzado |
| 13 | Baseline inicial | OpenGrep baseline | Avanzado |
| 14 | Deteccion de nuevas vulnerabilidades | OpenGrep diff | Avanzado |
| 15 | Priorizacion por contexto | CVSS + contexto | Avanzado |
| 16 | Severidad tecnica vs severidad contextual | Risk scoring | Avanzado |
| 17 | Confianza del hallazgo | Confidence levels | Avanzado |
| 18 | Inventario de repositorios | GitHub API | Experto |
| 19 | Escaneo organizativo simulado | OpenGrep multi-repo | Experto |
| 20 | GitHub Actions | GitHub Actions | Experto |
| 21 | Exportacion SARIF | SARIF | Experto |
| 22 | Quality gate no bloqueante | GitHub Actions | Experto |
| 23 | Quality gate bloqueante por criticidad | GitHub Actions | Experto |
| 24 | Reglas prohibidas por organizacion | Policy as code | Experto |
| 25 | Revision de excepciones vencidas | Governance | Experto |
| 26 | Metricas | Dashboards | Experto |
| 27 | Reporting ejecutivo | Markdown reports | Experto |
| 28 | Reporting tecnico | SARIF + JSON | Experto |
| 29 | Afinacion de reglas | OpenGrep tuning | Experto |
| 30 | Medalla final SAST Professional | — | Experto |

## Como funciona

Completas una tarea en el repositorio → GitHub Actions lo detecta → el README se actualiza → avanzas al siguiente paso.

## Empezar

1. Haz clic en **"Use this template"** → **"Create a new repository"**
2. En tu nuevo repositorio, ve a la pestana **Actions**
3. Si ves el aviso *"Workflows aren't being run"*, haz clic en **"I understand my workflows, enable them"**
4. En el panel izquierdo haz clic en **"Step 0: Empezar tutorial"**
5. Haz clic en **"Run workflow"** → **"Run workflow"**

El README se actualizara con el Paso 1 en unos segundos.

[![Usar este template](https://img.shields.io/badge/Usar%20este%20template-0b69ff?style=for-the-badge&logo=github&logoColor=white)](https://github.com/new?template_name=template-sast-opengrep-professional&template_owner=jgutierrezdtt)

> Usa **"Use this template"** para crear tu copia. No hagas fork directo.

## Referencias

- [OpenGrep](https://github.com/opengrep/opengrep)
- [GitHub Actions](https://docs.github.com/actions)
- [SARIF](https://sarifweb.azurewebsites.net/)
