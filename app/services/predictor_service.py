import os, joblib, json
import pandas as pd

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MODELS_PATH = os.path.join(BASE_DIR, "models")
COLUMNS_FILE = os.path.join(MODELS_PATH, "columnas_usadas.json")
SCALER_FILE = os.path.join(MODELS_PATH, "scaler_X.joblib")
CATEGORICAL_COLUMNS = ["mother_education_level", "father_education_level", "cognitive_ability", "general_health_status","hand_grip_ability", "self_care_ability", "speech_ability", "mobility_ability","hearing_ability", "vision_ability", "mother_lives_household", "father_lives_household","health_insurance_affiliation", "gender", "health_issue_last_30_days", "has_chronic_disease","student_health_insurance", "eps_complementary_health_plan", "other_health_services","private_health_insurance", "hospitalization_surgery_policy"]
CACHED_MODELS = {}

def predecir_calidad_vida(datos: dict, modelo_nombre: str) -> dict:
    """
    Predice la calidad de vida a partir de los datos ingresados y el modelo especificado.
    Retorna la predicción y la importancia de variables (si aplica).
    """
    modelo = cargar_modelo(modelo_nombre)
    datos_preprocesados = procesar_datos(datos)
    prediccion = modelo.predict(datos_preprocesados)
    importancias = cargar_importancias_csv(modelo_nombre)
    return {
        "prediccion": float(prediccion[0]),  # ✅ también aquí
        "importancia": importancias
    }

def cargar_modelo(nombre: str):
    """Carga y cachea el modelo ML."""
    if nombre not in CACHED_MODELS:
        modelo_path = os.path.join(MODELS_PATH, f"{nombre}.joblib")
        if not os.path.exists(modelo_path):
            raise FileNotFoundError(f"Modelo '{nombre}' no encontrado en '{modelo_path}'")
        CACHED_MODELS[nombre] = joblib.load(modelo_path)
    return CACHED_MODELS[nombre]

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

def cargar_importancias_csv(modelo_nombre: str) -> dict:
    """
    Carga las importancias de un modelo específico.
    Retorna un diccionario con las importancias de las variables.
    """
    nombre_archivo = nombre_archivo_importances(modelo_nombre) 
    importances_path = os.path.join(BASE_DIR, "resultados", f"{nombre_archivo}.csv")
    if not os.path.exists(importances_path) :
        return {}
    importances = pd.read_csv(importances_path).set_index("Feature")["Importance"].to_dict()

    return importances

def cargar_columnas(path: str = COLUMNS_FILE):
    """Carga las columnas esperadas por el modelo."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Archivo de columnas no encontrado en '{path}'")
    with open(path, "r") as f:
        columnas = json.load(f)
    return columnas

def cargar_scaler(path: str = SCALER_FILE):
    """Carga el objeto de escalado preentrenado."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Scaler no encontrado en '{path}'")
    return joblib.load(path)

def nombre_archivo_importances(modelo_nombre: str) -> str:
    """
    Genera el nombre del archivo de importancias basado en el nombre del modelo.
    """
    if modelo_nombre == "LightGBM":
        return "importances_lgb"
    elif modelo_nombre == "XGBRegressor":
        return "importances_xgb"
    elif modelo_nombre == "GradientBoosting":
        return "importances_gbr"