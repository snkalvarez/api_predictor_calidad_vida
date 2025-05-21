from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
from routes.routes import main as main_blueprint
from config.swagger_config import swagger_template


def create_app() -> Flask:
    """
    Crea y configura la instancia principal de Flask.
    """
    app = Flask(__name__)
    
    # Habilitar CORS
    CORS(app)
    
    # Documentación Swagger
    Swagger(app, template=swagger_template)
    
    # Registrar Blueprints
    app.register_blueprint(main_blueprint)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5000)
