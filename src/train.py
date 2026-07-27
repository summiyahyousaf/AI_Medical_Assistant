import joblib

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

from preprocess import preprocess_data


def train_model():

    X_train, X_test, y_train, y_test = preprocess_data()

    # ==========================
    # Decision Tree
    # ==========================

    decision_tree = DecisionTreeClassifier(
        random_state=42
    )

    decision_tree.fit(X_train, y_train)

    joblib.dump(
        decision_tree,
        "../models/decision_tree_model.pkl"
    )

    print("Decision Tree trained successfully.")

    # ==========================
    # Random Forest
    # ==========================

    random_forest = RandomForestClassifier(
        n_estimators=300,
        random_state=42,
        max_depth=None,
        min_samples_split=2,
        min_samples_leaf=1
    )

    random_forest.fit(X_train, y_train)

    joblib.dump(
        random_forest,
        "../models/random_forest_model.pkl"
    )

    print("Random Forest trained successfully.")

    # ==========================
    # Naive Bayes
    # ==========================

    naive_bayes = GaussianNB()

    naive_bayes.fit(X_train, y_train)

    joblib.dump(
        naive_bayes,
        "../models/naive_bayes_model.pkl"
    )

    print("Naive Bayes trained successfully.")

    # ==========================
    # SVM
    # ==========================

    svm = SVC(
        kernel="rbf",
        probability=True,
        random_state=42
    )

    svm.fit(X_train, y_train)

    joblib.dump(
        svm,
        "../models/svm_model.pkl"
    )

    print("SVM trained successfully.")

    # ==========================
    # Production Model
    # ==========================

    joblib.dump(
        random_forest,
        "../models/best_model.pkl"
    )

    print("Best model (Random Forest) saved successfully.")


if __name__ == "__main__":
    train_model()