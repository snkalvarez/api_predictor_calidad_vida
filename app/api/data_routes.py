from flask import Blueprint, jsonify, request
from app.services.data_service import read_resultados_tablacomparativa, obtener_variables_test_pred, data_real_predic_csv_path


data_bp = Blueprint('data_bp', __name__)

@data_bp.route('/datacomparativa', methods=['GET'])
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

@data_bp.route('/trainAndpredict', methods=['GET'])
def trainAndpredict():
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

@data_bp.route('/data_real_predic/csv', methods=['GET'])
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