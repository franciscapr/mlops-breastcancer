from flask import Flask, request, jsonify
from .model import ModelService

def create_app():
    app = Flask(__name__)
    model_service = ModelService()

    @app.route("/", methods=["GET"])
    def home():
        return jsonify({"message": "API Breast Cancer Classifier is running."})

    @app.route("/predict", methods=["POST"])
    def predict():
        try:
            payload = request.get_json()
            result = model_service.predict_from_json(payload)
            return jsonify(result)
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    return app

# Para ejecutar directamente
if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
