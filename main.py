from collections.abc import Sequence

import numpy as np


def calcular_estadisticas(datos: Sequence[float]) -> dict:
    """Calcula estadísticas descriptivas básicas de una lista de números."""
    if not datos:
        raise ValueError("La lista de datos no puede estar vacía")

    arreglo = np.array(datos)
    return {
        "minimo": float(np.min(arreglo)),
        "maximo": float(np.max(arreglo)),
        "media": float(np.mean(arreglo)),
        "mediana": float(np.median(arreglo)),
        "desviacion_estandar": float(np.std(arreglo)),
    }


if __name__ == "__main__":
    datos = [10, 25, 3, 47, 8, 33, 19, 52, 6, 41]

    print("Datos de entrada:", datos)

    resultado = calcular_estadisticas(datos)

    print("\nEstadísticas descriptivas:")
    for clave, valor in resultado.items():
        print(f"  {clave:<22}: {valor:.2f}")
