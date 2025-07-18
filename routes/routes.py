from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from config.schemas import PrediccionSchema
from services.predictor import predecir_calidad_vida, obtener_variables_test_pred
from services.tablacomparativa import read_resultados_tablacomparativa
from services.dataRealPredic import data_real_predic_csv_path
from services.graficas import grafica_educacionpadres_vs_ingreso_hogar, grafica_educacionpresencia_madre_vs_ingreso_hogar, grafica_educacionpresencia_padre_vs_ingreso_hogar, grafica_ingreso_hogar_edad_segun_satisfaccioncontrabajo, grafica_ingreso_hogar_edadpromedio_segun_satisfaccioncontrabajo, grafica_ingreso_hogar_satisfaccioncontrabajo_genero, grafica_presenciapadres_vs_ingreso_hogar

main = Blueprint('main', __name__)

schema = PrediccionSchema()

@main.route("/", methods=["GET"])
def hola():
    """
    Test de la API
    ---
    tags:
      - Test
    responses:
      200:
        description: Metodo get sencillo para probar la conexión a la API
    """
    return jsonify({"message": "Hola, recibes una respuesta de la API"})

@main.route("/predict", methods=["POST"])
def predict():
    """
    Realiza una predicción usando uno de los modelos disponibles
    ---
    tags:
      - Predicción
    parameters:
      - name: model
        in: query
        type: string
        required: true
        description: Nombre del modelo a usar ( LightGBM, GradientBoosting, XGBoost, MlpRegressor)
      - in: body
        name: input
        required: true
        schema:
          $ref: '#/definitions/Preguntas'
    responses:
      200:
        description: Predicción obtenida
    """
    try:
        #capturando el modelo
        model_name = request.args.get("model")
        if not model_name:
            return jsonify({"error": "Falta el nombre del modelo"}), 400
        
        #capturando los datos
        input_data = request.get_json()

        validated_data  = schema.load(input_data) # Validar los datos usando Marshmallow

        resultado = predecir_calidad_vida(validated_data, model_name)
        
        return jsonify({
            "message": "Validación exitosa", 
            "modelo": model_name, 
            "prediccion": resultado["prediccion"],
            "importancia": resultado["importancia"]
        }), 200

    except ValidationError as err:
        return jsonify({
            "error": "Error de validación", 
            "details": err.messages
        }), 400
    
    except Exception as e:
        return jsonify({
            "error": "Error interno del servidor", 
            "details": str(e)
        }), 500

@main.route("/datacomparativa", methods=["GET"])
def dataPrediciva():
    """
    Obtenemos los datos para poder calificar los algorimos segun su rendimiento
    ---
    tags:
      - DatosComparativos:
    responses:
      200:
        description: Json con todos sus valores
    """
    data = read_resultados_tablacomparativa()
    return jsonify({"mensaje": "ok" , "data":data})

# get para obterner la datapkl
@main.route("/trainAndpredict", methods=["GET"])
def data():
    """
    Obtenemos los datos con los que se entrenó el modelo y sus predicciones
    ---
    tags:
      - Datos
    responses:
      200:
        description: Json con los datos de entrada
    """
    data = obtener_variables_test_pred()
    return jsonify({"mensaje": "ok", "data": data})

@main.route("/data_real_predic/csv", methods=["GET"])
def data_real_predic_csv():
  """
  Obtenemos los datos reales y su predicción segun el modelo seleccionado
  ---
  tags:
    - Datos
  parameters:
    - name: model
      in: query
      type: string
      required: true
      description: Nombre del modelo a usar ( LightGBM, GradientBoosting, XGBoost, MlpRegressor)
  responses:
    200:
      description: Json con los datos reales y su predicción
  """
  try:
    print("Entrando a data_real_predic")
    model_name = request.args.get("model")
    if not model_name:
      return jsonify({"error": "Falta el nombre del modelo"}), 400

    data = data_real_predic_csv_path(model_name)
    return jsonify({"mensaje": "ok", "data": data})

  except Exception as e:
    return jsonify({
        "error": "Error interno del servidor", 
        "details": str(e)
    }), 500

@main.route("/grafica/presenciapadresvsingreso", methods=["GET"])
def grafica_presencia_padres_vs_ingreso_hogar():
    """
    Endpoint para obtener la gráfica de presencia de padres vs ingreso del hogar
    ---
    tags:
      - Gráficas
    responses:
      200:
        description: Gráfica de presencia de padres vs ingreso del hogar
    """
    try:
      data = grafica_presenciapadres_vs_ingreso_hogar()

      return jsonify(data)
    
    except Exception as e:
        return jsonify({
            "error": "Error interno del servidor", 
            "details": str(e)
        }), 500
    
@main.route("/grafica/educacionpadresvsingreso", methods=["GET"])
def grafica_educacion_padres_vs_ingreso_hogar():
    """
    Endpoint para obtener la gráfica de nivel educativo de padres vs ingreso del hogar
    ---
    tags:
      - Gráficas
    responses:
      200:
        description: Gráfica de nivel educativo de padres vs ingreso del hogar
    """
    try:
      data = grafica_educacionpadres_vs_ingreso_hogar()

      return jsonify(data)
    
    except Exception as e:
        return jsonify({
            "error": "Error interno del servidor", 
            "details": str(e)
        }), 500
    
@main.route("/grafica/educacionpresenciapadrevsingreso", methods=["GET"])
def grafica_educacion_presencia_padre_vs_ingreso_hogar():
    """
    Endpoint para obtener la gráfica de educacion y presencia de padres vs ingreso del hogar
    ---
    tags:
      - Gráficas
    responses:
      200:
        description: Gráfica de educacion y presencia de padres vs ingreso del hogar
    """
    try:
      data = grafica_educacionpresencia_padre_vs_ingreso_hogar()

      return jsonify(data)
    
    except Exception as e:
        return jsonify({
            "error": "Error interno del servidor", 
            "details": str(e)
        }), 500
    
@main.route("/grafica/educacionpresenciamadrevsingreso", methods=["GET"])
def grafica_educacion_presencia_madre_vs_ingreso_hogar():
    """
    Endpoint para obtener la gráfica de educacion y presencia de madre vs ingreso del hogar
    ---
    tags:
      - Gráficas
    responses:
      200:
        description: Gráfica de educacion y presencia de madre vs ingreso del hogar
    """
    try:
      data = grafica_educacionpresencia_madre_vs_ingreso_hogar()

      return jsonify(data)
    
    except Exception as e:
        return jsonify({
            "error": "Error interno del servidor", 
            "details": str(e)
        }), 500
    
@main.route("/grafica/ingresoedadsegunsatisfacciontrabajo", methods=["GET"])
def ingreso_hogar_edad_segun_satisfaccioncontrabajo():
    """
    Endpoint para obtener la gráfica de ingreso del hogar y edad según satisfacción con el trabajo
    ---
    tags:
      - Gráficas
    responses:
      200:
        description: Gráfica de ingreso del hogar y edad según satisfacción con el trabajo
    """
    try:
        data = grafica_ingreso_hogar_edad_segun_satisfaccioncontrabajo()
        return jsonify(data)
    
    except Exception as e:
        return jsonify({
            "error": "Error interno del servidor", 
            "details": str(e)
        }), 500
    
# metodo para ingreso_edadpromedio_satisfaccion_trabajo
@main.route("/grafica/ingresoedadpromediosegunsatisfacciontrabajo", methods=["GET"])
def ingreso_hogar_edadpromedio_segun_satisfaccioncontrabajo():
    """
    Endpoint para obtener la gráfica de ingreso del hogar y edad promedio según satisfacción con el trabajo
    ---
    tags:
      - Gráficas
    responses:
      200:
        description: Gráfica de ingreso del hogar y edad promedio según satisfacción con el trabajo
    """
    try:
        data = grafica_ingreso_hogar_edadpromedio_segun_satisfaccioncontrabajo()
        return jsonify(data)
    
    except Exception as e:
        return jsonify({
            "error": "Error interno del servidor", 
            "details": str(e)
        }), 500
    
#ruta para grafica_ingreso_hogar_satisfaccioncontrabajo_genero
@main.route("/grafica/ingresosatisfacciontrabajogenero", methods=["GET"])
def ingreso_hogar_satisfaccioncontrabajo_genero():
    """
    Endpoint para obtener la gráfica de ingreso del hogar y satisfacción con el trabajo según género
    ---
    tags:
      - Gráficas
    responses:
      200:
        description: Gráfica de ingreso del hogar y satisfacción con el trabajo según género
    """
    try:
        data = grafica_ingreso_hogar_satisfaccioncontrabajo_genero()
        return jsonify(data)
    
    except Exception as e:
        return jsonify({
            "error": "Error interno del servidor", 
            "details": str(e)
        }), 500