from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
from .config.swagger_config import swagger_template
from app.api import api_v1  as main_blueprint

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,  # incluye todas las rutas
            "model_filter": lambda tag: True,  # incluye todos los modelos
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/"  # ← volver al viejo endpoint si prefieres
}

def create_app() -> Flask:
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})
    Swagger(app, template=swagger_template, config=swagger_config )
    app.register_blueprint(main_blueprint)
    return app
