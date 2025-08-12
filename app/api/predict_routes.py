from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.schemas import PrediccionSchema
from app.services.predictor_service import predecir_calidad_vida

predict_bp = Blueprint('predict', __name__, url_prefix='/predict')

schema = PrediccionSchema()

@predict_bp.route('', methods=['POST'])
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
        description: Nombre del modelo a usar ( LightGBM, GradientBoosting, XGBRegressor, MlpRegressor)
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
        model_name = request.args.get("model")
        if not model_name:
            return jsonify({"error": "Falta el nombre del modelo"}), 400

        input_data = request.get_json()
        validated_data = schema.load(input_data)

        resultado = predecir_calidad_vida(validated_data, model_name)
        
        return jsonify({
            "message": "Validación exitosa", 
            "modelo": model_name, 
            "prediccion": resultado["prediccion"],
            "importancia": resultado["importancia"]
        }), 200

    except ValidationError as err:
        return jsonify({"error": "Error de validación", "details": err.messages}), 400

    except Exception as e:
        return jsonify({"error": "Error interno del servidor", "details": str(e)}), 500