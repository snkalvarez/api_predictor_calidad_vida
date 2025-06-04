import os
import pickle
import joblib

CACHED_MODELS = {}
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MODELS_PATH = os.path.join(BASE_DIR, "models_pickle")
CACHED_MODELS = {}

def cargar_modelos(nombre: str):
    """Carga y cachea el modelo ML."""
    if nombre not in CACHED_MODELS:
        modelo_path = os.path.join(MODELS_PATH, f"{nombre}.pkl")
        if not os.path.exists(modelo_path):
            raise FileNotFoundError(f"Modelo '{nombre}' no encontrado en '{modelo_path}'")
        CACHED_MODELS[nombre] = joblib.load(modelo_path)
    return CACHED_MODELS[nombre]

# metodo para recorrer los modelos y sacar sus importances y guardarlas en un plk
def guardar_importancias_modelos():
    """Recorre los modelos y guarda sus importancias en un archivo pickle."""
    modelos = ["RandomForest", "GradientBoosting", "XGBoost", "MlpRegressor"]
    importancias = {}

    for modelo_nombre in modelos:
        modelo = cargar_modelos(modelo_nombre)
        if hasattr(modelo, "feature_importances_"):
            importancias[modelo_nombre] = {
                #"importancia": modelo.feature_importances_.tolist()
                feature: float(importance)
                for feature, importance in zip(modelo.feature_names_in_, modelo.feature_importances_)
            }

    with open(os.path.join(os.path.join(BASE_DIR, "models"), "importances.pkl"), "wb") as f:
        pickle.dump(importancias, f)

# metodo para retornar las importances en un json
def cargar_importancias():
    """Carga las importancias de los modelos desde un archivo pickle."""
    importances_path = os.path.join(BASE_DIR, "models", "importances.pkl")
    if not os.path.exists(importances_path):
        guardar_importancias_modelos()
    
    with open(importances_path, "rb") as f:
        return pickle.load(f)
    