import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os
import json

DATA_PATH = "data/data.csv"
MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, "model.joblib")
FEATURES_PATH = os.path.join(MODEL_DIR, "features.json")

def load_data(path=DATA_PATH):
    df = pd.read_csv(path)
    if "id" in df.columns:
        df = df.drop(columns=["id"])
    df = df.loc[:, ~df.columns.str.contains("^Unnamed")]
    df["target"] = df["diagnosis"].map({"M":1, "B":0})
    X = df.drop(columns=["diagnosis", "target"])
    y = df["target"]
    return X, y

def train():
    X, y = load_data()
    feature_names = X.columns.tolist()
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("clf", RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=-1))
    ])

    pipeline.fit(X_train, y_train)
    preds = pipeline.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print("Accuracy:", acc)
    print(classification_report(y_test, preds))

    os.makedirs(MODEL_DIR, exist_ok=True)
    joblib.dump(pipeline, MODEL_PATH)
    with open(FEATURES_PATH, "w") as f:
        json.dump(feature_names, f)
    print(f"Model saved to {MODEL_PATH} with features {FEATURES_PATH}")

if __name__ == "__main__":
    train()
