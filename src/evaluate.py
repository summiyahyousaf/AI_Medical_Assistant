import os
import joblib
import matplotlib.pyplot as plt

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)

from preprocess import preprocess_data


# ==============================
# Project Paths
# ==============================

BASE_DIR = os.path.dirname(__file__)

MODELS_DIR = os.path.join(BASE_DIR, "..", "models")

IMAGES_DIR = os.path.join(BASE_DIR, "..", "images")

os.makedirs(IMAGES_DIR, exist_ok=True)


# ==============================
# Evaluation Function
# ==============================

def evaluate_model(model_name, model_filename):

    # Load data
    _, X_test, _, y_test = preprocess_data()

    # Load model
    model_path = os.path.join(MODELS_DIR, model_filename)

    model = joblib.load(model_path)

    # Prediction
    y_pred = model.predict(X_test)

    # Metrics
    accuracy = accuracy_score(y_test, y_pred)

    precision = precision_score(
        y_test,
        y_pred,
        average="weighted"
    )

    recall = recall_score(
        y_test,
        y_pred,
        average="weighted"
    )

    f1 = f1_score(
        y_test,
        y_pred,
        average="weighted"
    )

    report = classification_report(
        y_test,
        y_pred
    )

    matrix = confusion_matrix(
        y_test,
        y_pred
    )

    # ==============================
    # Confusion Matrix
    # ==============================

    display = ConfusionMatrixDisplay(
        confusion_matrix=matrix
    )

    display.plot(cmap="Blues")

    plt.title(f"{model_name} Confusion Matrix")

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            IMAGES_DIR,
            f"{model_name.lower().replace(' ', '_')}_confusion_matrix.png"
        )
    )

    plt.close()

    # ==============================
    # Print Results
    # ==============================

    print("\n" + "=" * 60)

    print(f"{model_name} Evaluation")

    print("=" * 60)

    print(f"Accuracy : {accuracy:.4f}")

    print(f"Precision: {precision:.4f}")

    print(f"Recall   : {recall:.4f}")

    print(f"F1 Score : {f1:.4f}")

    print("\nClassification Report\n")

    print(report)

    print("\nConfusion Matrix\n")

    print(matrix)

    return {
        "Model": model_name,
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1": f1
    }


# ==============================
# Main
# ==============================

if __name__ == "__main__":

    results = []

    results.append(
        evaluate_model(
            "Decision Tree",
            "decision_tree_model.pkl"
        )
    )

    results.append(
        evaluate_model(
            "Random Forest",
            "random_forest_model.pkl"
        )
    )

    results.append(
        evaluate_model(
            "Naive Bayes",
            "naive_bayes_model.pkl"
        )
    )

    results.append(
        evaluate_model(
            "SVM",
            "svm_model.pkl"
        )
    )

    # ==============================
    # Accuracy Comparison Graph
    # ==============================

    models = [r["Model"] for r in results]

    accuracies = [r["Accuracy"] for r in results]

    plt.figure(figsize=(8, 5))

    plt.bar(models, accuracies)

    plt.title("Models Accuracy Comparison")

    plt.xlabel("Models")

    plt.ylabel("Accuracy")

    plt.ylim(0.95, 1.01)

    plt.grid(axis="y", linestyle="--", alpha=0.7)

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            IMAGES_DIR,
            "model_accuracy_comparison.png"
        )
    )

    plt.show()

    # ==============================
    # Comparison Table
    # ==============================

    print("\n")

    print("=" * 90)

    print(
        f"{'Model':20}"
        f"{'Accuracy':12}"
        f"{'Precision':12}"
        f"{'Recall':12}"
        f"{'F1 Score'}"
    )

    print("=" * 90)

    for result in results:

        print(
            f"{result['Model']:20}"
            f"{result['Accuracy']:.4f}      "
            f"{result['Precision']:.4f}      "
            f"{result['Recall']:.4f}      "
            f"{result['F1']:.4f}"
        )

    print("=" * 90)