from flask import Blueprint

from .predict_routes import predict_bp
from .graficas_routes import graficas_bp
from .data_routes import data_bp

api_v1 = Blueprint('api_v1', __name__)
api_v1.register_blueprint(predict_bp)
api_v1.register_blueprint(graficas_bp)
api_v1.register_blueprint(data_bp)
