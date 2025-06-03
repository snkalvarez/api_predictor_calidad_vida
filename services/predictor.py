import os
import pandas as pd
import joblib
import pickle
import xgboost as xgb

 # version sklearn:
from sklearn import __version__ as sklearn_version
from xgboost import __version__ as xgb_version

# ===============================
# Configuración y constantes
# ===============================

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MODELS_PATH = os.path.join(BASE_DIR, "models_pickle")
CACHED_MODELS = {}

CATEGORICAL_COLUMNS = ["mother_education_level", "father_education_level", "cognitive_ability", "general_health_status","hand_grip_ability", "self_care_ability", "speech_ability", "mobility_ability","hearing_ability", "vision_ability", "mother_lives_household", "father_lives_household","health_insurance_affiliation", "gender", "health_issue_last_30_days", "has_chronic_disease","student_health_insurance", "eps_complementary_health_plan", "other_health_services","private_health_insurance", "hospitalization_surgery_policy"]

COLUMNS_FILE = os.path.join(MODELS_PATH, "columnas_modelo.pkl")
SCALER_FILE = os.path.join(MODELS_PATH, "scaler_X.pkl")

# ===============================
# Utilidades de Carga
# ===============================

def cargar_modelo(nombre: str):
    """Carga y cachea el modelo ML."""
    if nombre not in CACHED_MODELS:
        modelo_path = os.path.join(MODELS_PATH, f"{nombre}.pkl")
        if not os.path.exists(modelo_path):
            raise FileNotFoundError(f"Modelo '{nombre}' no encontrado en '{modelo_path}'")
        CACHED_MODELS[nombre] = joblib.load(modelo_path)
    return CACHED_MODELS[nombre]


def cargar_scaler(path: str = SCALER_FILE):
    """Carga el objeto de escalado preentrenado."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Scaler no encontrado en '{path}'")
    return joblib.load(path)


def cargar_columnas(path: str = COLUMNS_FILE):
    """Carga las columnas esperadas por el modelo."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Archivo de columnas no encontrado en '{path}'")
    with open(path, "rb") as f:
        return pickle.load(f)

# ===============================
# Preprocesamiento
# ===============================

def procesar_datos(datos: dict) -> pd.DataFrame:
    """Preprocesa los datos del usuario para el modelo."""
    df = pd.DataFrame([datos])

    for col in CATEGORICAL_COLUMNS:
        if col in df.columns:
            df[col] = df[col].astype("category")

    df = pd.get_dummies(df, columns=CATEGORICAL_COLUMNS, drop_first=False)

    columnas_modelo = cargar_columnas()
    df = df.reindex(columns=columnas_modelo, fill_value=0)

    scaler = cargar_scaler()
    df_scaled = pd.DataFrame(scaler.transform(df), columns=columnas_modelo)

    return df_scaled

# ===============================
# Predicción
# ===============================

def predecir_calidad_vida(datos: dict, modelo_nombre: str) -> dict:
    """
    Predice la calidad de vida a partir de los datos ingresados y el modelo especificado.
    Retorna la predicción y la importancia de variables (si aplica).
    """
    modelo = cargar_modelo(modelo_nombre)
    datos_preprocesados = procesar_datos(datos)
    prediccion = modelo.predict(datos_preprocesados)

    importances = None
    feature_names = datos_preprocesados.columns.tolist()

    if hasattr(modelo, "feature_importances_"):
        importances = {
            feature: float(importance)  # ✅ convertimos a float nativo
            for feature, importance in zip(feature_names, modelo.feature_importances_)
        }

    return {
        "prediccion": float(prediccion[0]),  # ✅ también aquí
        "importancia": importances
    }
