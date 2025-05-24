# pyelotl-demos
Demos que muestran funcionalidad de pyelotl con el paquete de prototipado streamlit  

## Instalación

### 1. Instalar uv

**Windows:**
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS y Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

📖 **Documentación completa de instalación**: [docs.astral.sh/uv/getting-started/installation](https://docs.astral.sh/uv/getting-started/installation/)

### 2. Configurar el proyecto

```bash
# Crear entorno virtual e instalar dependencias
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
uv pip install -r pyproject.toml
```

## Uso

```bash
streamlit run app.py
```

## Documentación útil

- **Guía de uv**: [docs.astral.sh/uv](https://docs.astral.sh/uv/)
- **Streamlit**: [docs.streamlit.io](https://docs.streamlit.io/)
- **uv para proyectos Python**: [docs.astral.sh/uv/guides/projects](https://docs.astral.sh/uv/guides/projects/)
