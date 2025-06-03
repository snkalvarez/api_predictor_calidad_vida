from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from models.schemas import PrediccionSchema
from services.predictor import predecir_calidad_vida
from services.tablacomparativa import cargar_modelo

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
        description: Nombre del modelo a usar ( RandomForest, GradientBoosting, XGBoost, MplRegressor )
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
    data = cargar_modelo()
    return jsonify({"mensaje": "ok" , "data":data})