# MLOps - Breast Cancer prediction

### Descripción del dataset

El dataset **Breast Cancer Wisconsin** (Diagnostic) proviene del UCI Machine Learning Repository y contiene información de 569 muestras de tumores de mama, con 30 característicasnuméricas extraídas de imágenes digitalizadas de células tumorales.
Cada fila representa un tumor y las columnas incluyen:
- ID number: Identificador único de la muestra.
- diagnosis: Etiqueta de diagnóstico (M = maligno, B = benigno).
- Características del tumor: Media (mean): Promedio de medidas como radio, textura, perímetro, área, suavidad, compacidad, concavidad, puntos cóncavos, simetría y dimensión fractal.
- Error estándar (se): Variación de cada medida en la muestra.
- Peor valor (worst): Valor máximo de cada medida en la muestra.

El objetivo del proyecto es entrenar un modelo de Machine Learning que pueda predecir si un tumor es maligno o benigno basado en estas características. Este dataset es ampliamente utilizado para tareas de clasificación binaria y para evaluar técnicas de predicción en entornos de salud.

- [https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data]

**Nota: Verifica la versión de tu python con:**
```bash
python --version

## Requisitos
- Python 3.10
- Docker (opcional si quieres correr en contenedor)

## Instalación local

1. Instalación Entorno Virtual: 
    python -m venv venv

2. Activación Entorno Virtual:
    source venv/Scripts/activate

3. Instalación Dependencias:
    pip install -r requirements.txt
    
4. Entrenar Modelo:
    python train.py

5. Run Server Local (Prueba API local)
    export FLASK_APP=app  (opcion 2) --> set FLASK_APP=app
    flask run --host=0.0.0.0 --port=5000

6. Probar API con curl:
    curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d '{
  "instances": [{
    "radius_mean": 12.45,
    "texture_mean": 20.27,
    "perimeter_mean": 78.88,
    "area_mean": 464.1,
    "smoothness_mean": 0.087,
    "compactness_mean": 0.06,
    "concavity_mean": 0.025,
    "concave points_mean": 0.03,
    "symmetry_mean": 0.188,
    "fractal_dimension_mean": 0.062,
    "radius_se": 0.5,
    "texture_se": 1.2,
    "perimeter_se": 3.1,
    "area_se": 40.0,
    "smoothness_se": 0.007,
    "compactness_se": 0.02,
    "concavity_se": 0.02,
    "concave points_se": 0.01,
    "symmetry_se": 0.02,
    "fractal_dimension_se": 0.003,
    "radius_worst": 14.2,
    "texture_worst": 25.0,
    "perimeter_worst": 95.0,
    "area_worst": 600.0,
    "smoothness_worst": 0.12,
    "compactness_worst": 0.25,
    "concavity_worst": 0.15,
    "concave points_worst": 0.05,
    "symmetry_worst": 0.22,
    "fractal_dimension_worst": 0.08
  }]
}'

7. DOCKER:
    - Contrucción Imagen:
    docker build -t mlops-breastcancer:local .
    
    - Ejecutar Contenedor:
    docker run --rm -p 8000:8000 -v $(pwd)/models:/app/models:ro mlops-breastcancer:local




