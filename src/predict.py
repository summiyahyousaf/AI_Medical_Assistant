import joblib
import pandas as pd

from preprocess import preprocess_data
from symptom_aliases import symptom_aliases
from report import generate_report


def predict_disease():

    # Load trained model
    model = joblib.load("../models/best_model.pkl")

    # Load label encoder
    encoder = joblib.load("../models/label_encoder.pkl")

    # Load symptom columns
    X_train, _, _, _ = preprocess_data()
    symptom_columns = X_train.columns

    # Create empty dataframe
    input_data = pd.DataFrame(0, index=[0], columns=symptom_columns)

    # User input
    user_input = input(
        "\nEnter the symptoms you are facing: "
    ).lower().strip()

    if not user_input:
        print("No symptoms entered.")
        return None

    recognized = []
    ignored = []

    # Replace aliases with dataset symptom names
    for alias, original in symptom_aliases.items():
        if alias in user_input:
            user_input = user_input.replace(alias, original)

    # Detect symptoms from the sentence
    for symptom in symptom_columns:

        if symptom in user_input:
            input_data[symptom] = 1
            recognized.append(symptom)

    # No valid symptoms found
    if not recognized:
        print("\nNo valid symptoms were recognized.")
        print("Please enter symptoms from the supported symptom database.")
        return None

    # Predict disease
    prediction = model.predict(input_data)
    disease = encoder.inverse_transform(prediction)[0]

    # Confidence
    probability = model.predict_proba(input_data)
    confidence = max(probability[0]) * 100

    result = {
        "disease": disease,
        "confidence": confidence,
        "recognized": recognized,
        "ignored": ignored,
        "entered": user_input
    }

    return result


# Main
if __name__ == "__main__":

    result = predict_disease()

    if result:
        generate_report(result)