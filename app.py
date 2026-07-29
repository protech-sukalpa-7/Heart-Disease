from pathlib import Path

import joblib
import pandas as pd
from flask import Flask, render_template, request

BASE_DIR = Path(__file__).resolve().parent

app = Flask(__name__)

MODEL_PATH = BASE_DIR / "heart_disease_stacking_model.pkl"
SCALER_PATH = BASE_DIR / "scaler.pkl"
ENCODER_PATH = BASE_DIR / "encoder.pkl"

FEATURE_COLUMNS = [
    "age",
    "sex",
    "dataset",
    "cp",
    "trestbps",
    "chol",
    "fbs",
    "restecg",
    "thalch",
    "exang",
    "oldpeak",
    "slope",
    "ca",
    "thal",
]

CATEGORICAL_COLUMNS = ["sex", "dataset", "cp", "fbs", "restecg", "exang", "slope", "thal"]
NUMERIC_COLUMNS = ["age", "trestbps", "chol", "thalch", "oldpeak", "ca"]

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)
encoders = joblib.load(ENCODER_PATH)


def preprocess_input(form_data: dict) -> pd.DataFrame:
    input_frame = pd.DataFrame([form_data], columns=FEATURE_COLUMNS)

    for column in CATEGORICAL_COLUMNS:
        encoder = encoders[column]
        encoded_values = []
        for value in input_frame[column]:
            text_value = str(value).strip()
            if text_value in encoder.classes_:
                encoded_values.append(text_value)
            else:
                encoded_values.append(encoder.classes_[0])
        input_frame[column] = [encoder.transform([value])[0] for value in encoded_values]

    for column in NUMERIC_COLUMNS:
        input_frame[column] = pd.to_numeric(input_frame[column], errors="coerce").fillna(0)

    return scaler.transform(input_frame[FEATURE_COLUMNS])


@app.route("/", methods=["GET", "POST"])
def index():
    prediction_text = None
    probability = None
    categories = {column: encoders[column].classes_.tolist() for column in CATEGORICAL_COLUMNS}

    if request.method == "POST":
        form_data = {column: request.form.get(column, "") for column in FEATURE_COLUMNS}
        prepared_input = preprocess_input(form_data)
        prediction = int(model.predict(prepared_input)[0])

        if hasattr(model, "predict_proba"):
            probability = round(float(model.predict_proba(prepared_input)[0, 1]) * 100, 1)

        if prediction == 1:
            prediction_text = "High risk of heart disease"
        else:
            prediction_text = "Low risk of heart disease"

    return render_template(
        "index.html",
        prediction_text=prediction_text,
        probability=probability,
        categories=categories,
        form_data=request.form,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860, debug=False)
