import os
import pandas as pd
import pickle

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
RESULTADOS_PATH = os.path.join(BASE_DIR, "resultados")


def data_real_predic_csv_path(modelo_nombre: str) -> str:
    """
    Genera la ruta del archivo CSV de resultados reales vs predicciones.
    """
    nombre_resultados = nombre_archivo_real_predic(modelo_nombre)
    if not os.path.exists(os.path.join(RESULTADOS_PATH, f"{nombre_resultados}.csv")):
        raise FileNotFoundError(f"No se encontró el archivo {nombre_resultados}.csv en {RESULTADOS_PATH}")
    df = pd.read_csv(os.path.join(RESULTADOS_PATH, f"{nombre_resultados}.csv"))

    return df.to_dict(orient="records")

def cargar_real_predic_pkl(modelo_nombre: str) -> dict:
    """
    Carga los datos reales y sus predicciones desde un archivo .pkl.
    Retorna un diccionario con los datos.
    """
    nombre_archivo = nombre_archivo_real_predic(modelo_nombre)
    if not os.path.exists(os.path.join(RESULTADOS_PATH, f"{nombre_archivo}.pkl")):
        raise FileNotFoundError(f"No se encontró el archivo {nombre_archivo}.pkl en {RESULTADOS_PATH}")
    
    with open(os.path.join(RESULTADOS_PATH, f"{nombre_archivo}.pkl"), "rb") as f:
        data = pickle.load(f)
    if isinstance(data, pd.DataFrame):
        return data.to_dict(orient="records")
    else:
        return data

def nombre_archivo_real_predic(modelo_nombre: str) -> str:
    """
    Genera el nombre del archivo de resultados real vs predicho basado en el nombre del modelo.
    """
    if modelo_nombre == "RandomForestX3":
        return "resultadosRealPredX3_rf"
    elif modelo_nombre == "XGBoostX3":
        return "resultadosRealPredX3_xgb"
    elif modelo_nombre == "GradientBoostingX3":
        return "resultadosRealPredX3_gbr"
    elif modelo_nombre == "MlpRegressorX3":
        return "resultadosRealPredX3_mlp"