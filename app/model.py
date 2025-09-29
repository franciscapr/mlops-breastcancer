import joblib
import os
import json
import pandas as pd

MODEL_PATH = os.getenv("MODEL_PATH", "models/model.joblib")
FEATURES_PATH = os.getenv("FEATURES_PATH", "models/features.json")

class ModelService:
    def __init__(self):
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Model not found at {MODEL_PATH}")
        if not os.path.exists(FEATURES_PATH):
            raise FileNotFoundError(f"Features file not found at {FEATURES_PATH}")

        self.model = joblib.load(MODEL_PATH)
        with open(FEATURES_PATH, "r") as f:
            self.feature_names = json.load(f)

    def predict_from_json(self, payload):
        df = pd.DataFrame(payload["instances"])
        
        # Verificar columnas faltantes
        missing_cols = set(self.feature_names) - set(df.columns)
        if missing_cols:
            raise ValueError(f"Faltan columnas: {missing_cols}")
        
        # Reordenar columnas
        df = df[self.feature_names]

        preds = self.model.predict(df)
        preds_proba = self.model.predict_proba(df)

        response = []
        for p, prob in zip(preds, preds_proba):
            response.append({
                "prediction": int(p),
                "probability": prob.tolist()
            })

        return {"predictions": response}
