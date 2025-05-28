![Badge en Desarrollo](https://img.shields.io/badge/STATUS-EN%20DESAROLLO-green)

# Api Predicción calidad de vida

## Introducción
Esta API nos ayuda a predecir la calidad de vida evaluando 29 variables mediante algoritmos de regresión: **RandomForest**, **XGBoost**, **GradientBoosting**, y **MLPRegressor**. Utiliza Flask y está orientada a aplicaciones de ciencia de datos.

<!-- Para abrir el preview en Atom: ^ (control) + shift + M -->

# README
[![platform][windows]][windows]

<!-- Para crear un índice -->
## Table of Contents
- [Api Predicción calidad de vida](#api-predicción-calidad-de-vida)
  - [Introducción](#introducción)
- [README](#readme)
  - [Table of Contents](#table-of-contents)
  - [Requirements](#requirements)
  - [Instalación](#instalación)
  - [Uso](#uso)
  - [Author](#author)
  - [License](#license)
  - [Documentation](#documentation)

## Requirements
|                                         Platform                                         |         Language          |IDE| Librerías Ciencia de Datos |
|:----------------------------------------------------------------------------------------:|:-------------------------:|:---:|:--------------------------:|
| [![platform][windows]][windows] [![platform][linux]][linux] [![platform][docker]][docker] | [![language][Python]][Python] |[![ide][Visual Studio Code]][Visual Studio Code]| `flasgger`, `Flask`, `flask-cors`, `joblib`, `marshmallow`, `numpy`, `pandas`, `scikit-learn`, `xgboost` |

## Instalación
- Clonar el repositorio
~~~bash
git clone <URL-del-repositorio-actual>
~~~

- Crear entorno virtual (opcional)
~~~bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
~~~

- Obtener los archivos de modelo `.pkl`

Debes acceder al siguiente enlace de Colab para generar o descargar los modelos entrenados:

👉 [Google Colab - Generar modelos](https://colab.research.google.com/drive/19eU5cMzaV3OzL52Wu_Yq6O0jCdSplmHU?usp=sharing)

Omite la ejecutión de "Busqueda de hyperparametros" y puedes ejecutar todo. 
Esta lo que hara es demorar mucho el proceso que ya esta al final en "Toma de Rendimiento"

Una vez descargados, colócalos en la carpeta (creala en la raiz con este mismo nombre)`models_pickle/` con los siguientes nombres exactos:

models_pickle/
  ├── GradientBoosting.pkl  
  ├── MplRegressor.pkl  
  ├── RandomForest.pkl  
  ├── XGBoost.pkl  
  ├── columnas_modelo.pkl  
  ├── scaler_X.pkl  
  └── scaler_y.pkl  
> ⚠️ **Importante:** Si estos archivos no están presentes en la carpeta `models_pickle`, la API lanzará errores al momento de realizar predicciones.

- Instalar dependencias
~~~bash
pip install -r requirements.txt
~~~

> Si no tienes el archivo `requirements.txt`, puedes instalar manualmente:

~~~txt
Flask==3.1.1
flasgger==0.9.7.1
flask-cors==6.0.0
joblib==1.5.1
marshmallow==4.0.0
numpy==2.0.2
pandas==2.2.3
scikit-learn===1.6.1
xgboost==3.0.2
~~~

- Configurar el archivo `app.py` (si aplica)
- Ejecutar la aplicación
~~~bash
flask run
~~~

## Uso
La API ofrece endpoints para enviar datos y obtener una predicción del índice de calidad de vida.

Ejemplo básico de request:

~~~json
POST /predict
{
  "edad_promedio": 35,
  "ingreso_mensual": 4200,
  ...
}
~~~

## Author
Julio Alvarez, [linkedin][myLinkedin].
Juan Carlos Ruales, [linkedin][rualesLinkedin].

## License
README is available under the license. See the [LICENSE](LICENSE) file for more info.

## Documentation
La documentación de la API está disponible en el siguiente enlace:
  - Para acceder a la documentación de la API, puedes dar clic aqui [swagger](http://localhost:5000/apidocs). 
  - Asegúrate de que el servidor esté en ejecución antes de intentar acceder a la documentación.
  - Si estás utilizando un puerto diferente, asegúrate de cambiar el puerto en caso de que no sea el 5000 en la misma url.

<!-- Links -->
[myLinkedin]:https://www.linkedin.com/in/julio-alvarez-dev/
[rualesLinkedin]:https://www.linkedin.com/in/juancarlosrualescaicedo/
[java]:https://img.shields.io/badge/Java-≥_17.0-FF2D55.svg?colorA=FF2D55
[Python]:https://img.shields.io/badge/Python-=_3.12-3776AB.svg?colorA=3776AB
[Windows]:https://img.shields.io/badge/Windows-0078D6.svg?colorA=0078D6&logo=windows&logoColor=white
[Linux]:https://img.shields.io/badge/Linux-FCC624.svg?colorA=FCC624&logo=linux&logoColor=black
[Docker]:https://img.shields.io/badge/Docker-2496ED.svg?colorA=2496ED&logo=docker&logoColor=white
[IntelliJ IDEA]: https://img.shields.io/badge/IntelliJ_IDEA-000000.svg?colorA=000000&logo=intellij-idea&logoColor=white
[Visual Studio Code]: https://img.shields.io/badge/Visual_Studio_Code-007ACC.svg?colorA=007ACC&logo=visual-studio-code&logoColor=white
