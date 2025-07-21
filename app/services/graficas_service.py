import os, json

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_PATH = os.path.join(BASE_DIR, 'data')

def grafica_presenciapadres_vs_ingreso_hogar():
    with open(os.path.join(DATA_PATH, 'presencia_padres.json'), 'r') as f:
        datos = json.load(f)
    
    # Estructurar datos para el frontend
    response_data = {
        'padres': datos['father_data'],
        'madres': datos['mother_data'],
        'metadata': datos['metadata']
    }

    return response_data

def grafica_educacionpadres_vs_ingreso_hogar():
    with open(os.path.join(DATA_PATH, 'educacionPadres_vs_ingresos.json'), 'r') as f:
        datos = json.load(f)

    return datos

def grafica_educacionpresencia_padre_vs_ingreso_hogar():
    with open(os.path.join(DATA_PATH, 'educacion_presencia_padre.json'), 'r') as f:
        datos = json.load(f)

    return datos

def grafica_educacionpresencia_madre_vs_ingreso_hogar():
    with open(os.path.join(DATA_PATH, 'educacion_presencia_madre.json'), 'r') as f:
        datos = json.load(f)

    return datos

def grafica_ingreso_hogar_edad_segun_satisfaccioncontrabajo():
    with open(os.path.join(DATA_PATH, 'ingreso_edad_satisfaccion.json'), 'r') as f:
        datos = json.load(f)

    return datos

def grafica_ingreso_hogar_edadpromedio_segun_satisfaccioncontrabajo():
    with open(os.path.join(DATA_PATH, 'ingreso_edadpromedio_satisfaccion_trabajo.json'), 'r') as f:
        datos = json.load(f)

    return datos

def grafica_ingreso_hogar_satisfaccioncontrabajo_genero():
    with open(os.path.join(DATA_PATH, 'ingreso_satisfaccion_trabajo_genero.json'), 'r') as f:
        datos = json.load(f)

    return datos