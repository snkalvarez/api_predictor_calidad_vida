from flask import Blueprint, jsonify
from app.services.graficas_service import grafica_presenciapadres_vs_ingreso_hogar, grafica_educacionpadres_vs_ingreso_hogar, grafica_educacionpresencia_padre_vs_ingreso_hogar, grafica_educacionpresencia_madre_vs_ingreso_hogar, grafica_ingreso_hogar_edad_segun_satisfaccioncontrabajo, grafica_ingreso_hogar_edadpromedio_segun_satisfaccioncontrabajo, grafica_ingreso_hogar_satisfaccioncontrabajo_genero

graficas_bp = Blueprint('graficas', __name__, url_prefix='/grafica')

@graficas_bp.route('/presenciapadresvsingreso', methods=['GET'])
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
        return jsonify({"error": "Error interno del servidor", "details": str(e)}), 500
    

@graficas_bp.route('/educacionpadresvsingreso', methods=['GET'])
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
        return jsonify({"error": "Error interno del servidor", "details": str(e)}), 500
    
@graficas_bp.route('/educacionpresenciapadrevsingreso', methods=['GET'])
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
        return jsonify({"error": "Error interno del servidor", "details": str(e)}), 500
    
@graficas_bp.route('/educacionpresenciamadrevsingreso', methods=['GET'])
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
        return jsonify({"error": "Error interno del servidor", "details": str(e)}), 500
    
@graficas_bp.route('/ingresoedadsegunsatisfacciontrabajo', methods=['GET'])
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
    

@graficas_bp.route('/ingresoedadpromediosegunsatisfacciontrabajo', methods=['GET'])
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
@graficas_bp.route("/ingresosatisfacciontrabajogenero", methods=["GET"])
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