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

def nombre_archivo_real_predic(modelo_nombre: str) -> str:
    """
    Genera el nombre del archivo de resultados real vs predicho basado en el nombre del modelo.
    """
    if modelo_nombre == "LightGBM":
        return "resultadosRealPred_lgb"
    elif modelo_nombre == "XGBoost":
        return "resultadosRealPred_xgb"
    elif modelo_nombre == "GradientBoosting":
        return "resultadosRealPred_gbr"
    elif modelo_nombre == "MlpRegressor":
        return "resultadosRealPred_mlp"