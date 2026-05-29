# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Comandos principales

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
python main.py

# Ejecutar todas las pruebas
pytest tests/ -v

# Ejecutar una sola prueba
pytest tests/test_main.py::TestCalcularEstadisticas::test_media_correcta -v

# Ejecutar pruebas por nombre (patrón)
pytest tests/ -k "lista_vacia" -v
```

## Arquitectura

El proyecto es un script Python de cálculo de estadísticas descriptivas con una suite de pruebas unitarias y un pipeline de CI/CD en GitHub Actions.

- **[main.py](main.py)** — única función de negocio: `calcular_estadisticas(datos)` recibe una secuencia de números y retorna un dict con `minimo`, `maximo`, `media`, `mediana` y `desviacion_estandar`. Usa NumPy para todos los cálculos.
- **[tests/test_main.py](tests/test_main.py)** — 10 pruebas unitarias agrupadas en `TestCalcularEstadisticas`. Cubren casos normales, edge cases (un elemento, negativos) y la excepción `ValueError` para lista vacía.
- **[.github/workflows/ci.yml](.github/workflows/ci.yml)** — pipeline de GitHub Actions que se dispara en push/PR a `main`: configura Python 3.12, instala dependencias, corre `pytest tests/ -v` y luego `python main.py`.

## Dependencias

- `numpy==2.2.6` — cálculos estadísticos
- `pytest==8.3.5` — framework de pruebas
