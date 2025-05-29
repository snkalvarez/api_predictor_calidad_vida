import os
import pickle
import gdown

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
RUTA_TABLA= os.path.join(BASE_DIR,"models/resultados.pkl")
FILE_ID= '1EXB0z_F2GFwPGUvXgyF-0ZyZaJdhBkCl'
DRIVE_URL= f'https://drive.google.com/uc?export=download&id={FILE_ID}'

def descargar_modelo_si_no_existe(reemplazar=False):
    """
    Descargar el archivo resultados.pkl desde google drive si no existe localmente o si se especifica reemplazar=True
    """
    # si ya existe y no queremos reemplazarlo, salimos
    if os.path.exists(RUTA_TABLA) and not reemplazar:
        print("Modelo ya descargado. Usando archivo llocal.")
        return
    
    #Crear carpeta si no existe
    os.makedirs(os.path.dirname(RUTA_TABLA), exist_ok=True)

    print("descargando modelo desde Google Drive")
    gdown.download(DRIVE_URL, RUTA_TABLA, quiet=False)
    print("Descarga completa.")


def cargar_modelo():
    """
    Carga el modelo edsde el archivo local.
    """
    if not os.path.exists(RUTA_TABLA):
        raise FileNotFoundError("El archivo del modelo no existe, Debes cargarlo primero.")
    
    with open(RUTA_TABLA, 'rb') as f:
        modelo = pickle.load(f)
    return modelo