import os
import pandas as pd

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
RUTA_ARCHIVO = os.path.join(BASE_DIR, "resultados/resultadosTablaComparativa.csv")

def read_resultados_tablacomparativa():
    """
    Carga el modelo desde el archivo local.
    """
    if not os.path.exists(RUTA_ARCHIVO):
        raise FileNotFoundError("El archivo de resultados de comparacion no existe, Debes cargarlo primero.")
    
    ## leer el csv y enviarlo
    df = pd.read_csv(RUTA_ARCHIVO)
    modelo = df.to_dict(orient='records')  # Convertir DataFrame a lista de diccionarios

    return modelo