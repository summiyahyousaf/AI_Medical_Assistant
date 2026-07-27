from data_loader import load_data
import joblib
from sklearn.preprocessing import LabelEncoder


def preprocess_data():

    train_df, test_df = load_data()

    # Remove unnecessary column
    for df in [train_df, test_df]:
        if "Unnamed: 133" in df.columns:
            df.drop(columns=["Unnamed: 133"], inplace=True)

   # Separate features and target
    X_train = train_df.drop(columns=["prognosis"])

# Save all symptom names
    joblib.dump(X_train.columns.tolist(), "../models/symptoms.pkl")

# Print for checking
    print(X_train.columns.tolist())
    print("Total Symptoms:", len(X_train.columns))

    y_train = train_df["prognosis"] 

    X_test = test_df.drop(columns=["prognosis"])
    y_test = test_df["prognosis"]

    print("X_train Shape:", X_train.shape)
    print("y_train Shape:", y_train.shape)

    print("X_test Shape:", X_test.shape)
    print("y_test Shape:", y_test.shape)

    # Encode labels
    label_encoder = LabelEncoder()

    y_train = label_encoder.fit_transform(y_train)
    y_test = label_encoder.transform(y_test)

    # Save label encoder
    joblib.dump(label_encoder, "../models/label_encoder.pkl")

    print("\nFirst 10 Encoded Training Labels:")
    print(y_train[:10])

    print("\nFirst 10 Encoded Testing Labels:")
    print(y_test[:10])

    return X_train, X_test, y_train, y_test