# 🩺 AI Medical Assistant
## Intelligent Healthcare Prediction & Conversational AI Platform

<p align="center">

<img src="https://img.shields.io/badge/AI-Medical%20Assistant-2E7D32?style=for-the-badge&logo=health" />

<img src="https://img.shields.io/badge/Machine%20Learning-Random%20Forest-orange?style=for-the-badge&logo=scikitlearn" />

<img src="https://img.shields.io/badge/Backend-Flask-black?style=for-the-badge&logo=flask" />

<img src="https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS%20%7C%20JavaScript-blue?style=for-the-badge&logo=javascript" />

<img src="https://img.shields.io/badge/Python-3.14-yellow?style=for-the-badge&logo=python" />

</p>


<p align="center">

An AI-powered healthcare assistant that combines Machine Learning, Web Development, and Conversational AI to provide intelligent disease prediction and health support.

</p>


---

# Project Overview

AI Medical Assistant is an end-to-end healthcare AI application designed to assist users in understanding their symptoms through machine learning-based disease prediction.

The system analyzes user-provided symptoms, converts them into machine-readable features, and uses trained classification models to predict possible diseases.

Along with prediction capabilities, the application provides:

-  AI disease prediction
-  Interactive medical chatbot
-  Automated medical reports
-  Health analytics dashboard
-  User profile management
-  Application settings


The project demonstrates the complete AI development lifecycle:

Data Collection
↓
Exploratory Data Analysis
↓
Data Preprocessing
↓
Machine Learning Training
↓
Model Evaluation
↓
Model Deployment
↓
Interactive Web Application


The AI Medical Assistant is a Flask-based web application that predicts diseases from user-selected symptoms using a machine learning model. Users can create an account, log in securely, enter their symptoms, and receive an AI-generated disease prediction along with a confidence score. Every prediction is stored in a SQLite database, allowing users to review previous reports and download them as PDF documents. The application also includes health analytics and an AI assistant that answers common medical questions. The machine learning model was trained using a disease–symptom dataset, and Joblib is used to efficiently load the trained model and LabelEncoder during deployment.




#  Project Objectives

The main objectives of this project are:

- Build an intelligent symptom-based disease prediction system
- Compare multiple machine learning algorithms
- Select the best-performing model
- Deploy the model through a Flask web application
- Create a professional healthcare dashboard
- Provide users with an interactive AI assistant experience



#  System Architecture

                              USER
                                |
                                |
                                ↓
                    ┌──────────────────────┐
                    │   Web Interface      │
                    │ HTML / CSS / JS      │
                    └──────────────────────┘
                                |
                                |
                                ↓
                    ┌──────────────────────┐
                    │   Flask Application  │
                    │      Backend         │
                    └──────────────────────┘
                                |
              ┌─────────────────┼─────────────────┐
              |                 |                 |
              ↓                 ↓                 ↓
 ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
 │ Disease          │  │ AI Medical       │  │ User Management  │
 │ Prediction       │  │ Assistant        │  │ & Reports        │
 │ Module           │  │ Module           │  │ Module           │
 └──────────────────┘  └──────────────────┘  └──────────────────┘
              |                 |                 |
              ↓                 ↓                 ↓
 ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
 │ Symptom Input    │  │ Chat Interface   │  │ SQLite Database  │
 │ Processing       │  │ & Responses      │  │                  │
 └──────────────────┘  └──────────────────┘  └──────────────────┘
              |
              |
              ↓
        ┌─────────────────────────────┐
        │ Machine Learning Pipeline   │
        └─────────────────────────────┘
                         |
                         ↓
        ┌─────────────────────────────┐
        │ Data Preprocessing          │
        │                             │
        │ - Cleaning                  │
        │ - Feature Encoding          │
        │ - Label Encoding            │
        └─────────────────────────────┘
                         |
                         ↓
        ┌─────────────────────────────┐
        │ Trained ML Models           │
        │                             │
        │ - Decision Tree             │
        │ - Random Forest             │
        │ - Naive Bayes               │
        │ - SVM                       │
        └─────────────────────────────┘
                         |
                         ↓
        ┌─────────────────────────────┐
        │ Model Evaluation            │
        │                             │
        │ - Accuracy                  │
        │ - Precision                 │
        │ - Recall                    │
        │ - F1 Score                  │
        │ - Confusion Matrix          │
        └─────────────────────────────┘

                         |
                         ↓
        ┌─────────────────────────────┐
        │ Final Selected Model        │
        │                             │
        │ Random Forest Classifier    │
        │ best_model.pkl              │
        └─────────────────────────────┘
                         |
                         ↓
        ┌─────────────────────────────┐
        │ Prediction Engine           │
        │                             │
        │ Symptoms → Vector → Disease │
        │ + Confidence Score          │
        └─────────────────────────────┘
                         |
                         ↓
        ┌─────────────────────────────┐
        │ Medical Report Generation   │
        │                             │
        │ - Patient Information       │
        │ - Predicted Disease         │
        │ - Confidence Level          │
        │ - Selected Symptoms         │
        └─────────────────────────────┘



# Data Processing


## 1. Data Loading

Dataset is loaded using:

- Pandas
- NumPy


## 2. Exploratory Data Analysis


Performed analysis:

- Dataset structure inspection
- Missing value checking
- Duplicate detection
- Disease distribution analysis
- Symptom analysis


Visualization tools:

- Matplotlib
- Seaborn


## 3. Feature Engineering


Symptoms are converted into numerical vectors.

Example:

The model receives a 132-dimensional feature vector and are converted into numerical values using label encoding.



# Machine Learning Models


Multiple classification algorithms were trained and evaluated:


|      Model                 |         Description          |


|     Decision Tree          | Rule-based classifier        |
|     Random Forest          | Ensemble learning classifier |
|       Naive Bayes          | Probabilistic classifier     |
|     Support Vector Machine | Margin-based classifier      |


Evaluation metrics:


- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix



#  Final Model Selection


After evaluating different algorithms, the final deployed model selected was:


##  Random Forest Classifier


Reasons for selection:


✅ Handles complex symptom relationships  
✅ Better generalization capability  
✅ Reduces overfitting compared to individual decision trees  
✅ Works efficiently with structured medical datasets  
✅ Provides probability estimates for predictions  


Saved model:

models/
└── best_model.pkl



#  Application Features


##  Healthcare Dashboard


A professional dashboard that provides users with centralized access to all healthcare services.


- User-friendly navigation
- Disease prediction access
- Medical reports
- Health analytics
- Profile management
- Settings



#  Disease Prediction Module


Workflow:
          
          User Symptoms
              ↓
          Symptom Processing
              ↓
          Feature Vector Generation
              ↓
          Random Forest Classification Model
              ↓
          Disease Prediction
              ↓
          Confidence Score
              ↓
          Medical Report
              ↓
          Savce Medical Report / Download as PDF


Generated report contains:


- Patient information
- Predicted disease
- Confidence level
- Selected symptoms
- Input vector information



#  AI Medical Assistant


The application includes an interactive AI assistant.


Features:


- Floating chatbot interface
- Real-time conversation
- Health-related questions
- User-friendly chat experience
- Responsive design


---

#  Technology Stack


## Programming Language

Python


## Machine Learning

- Scikit-learn
- Pandas
- NumPy
- Joblib


## Backend

- Flask


## Frontend

- HTML5
- CSS3
- JavaScript


## Database

- SQLite


## Data Visualization

- Matplotlib
- Seaborn


---

# Project Structure

AI_Medical_Assistant/
│
├── app.py
│
├── src/
│ ├── data_loader.py
│ ├── eda.py
│ ├── preprocess.py
│ ├── train.py
│ ├── evaluate.py
│ ├── predict.py
│ ├── report.py
│
├── models/
│ ├── random_forest_model.pkl
│ └── best_model.pkl
│
├── static/
│ ├── css/
│ ├── js/
│ └── images/
│
├── templates/
│ ├── dashboard.html
│ ├── predict.html
│ ├── reports.html
│ ├── assistant.html
│
├── requirements.txt
└── README.md



# Installation

Clone repository:


```bash
git clone https://github.com/yourusername/AI-Medical-Assistant.git


Navigate:
cd AI-Medical-Assistant


Create virtual environment:
python -m venv venv


Activate environment:
Windows:
venv\Scripts\activate


Install dependencies:
pip install -r requirements.txt


Running Application
Start Flask server:

     python app.py

Open browser:

    http://127.0.0.1:5000


 Model Evaluation

The system generates:

Accuracy comparison graph
Confusion matrices
Classification reports

Evaluation metrics:
Accuracy

Precision

Recall

F1 Score


 Future Improvements:

-Artificial Intelligence Improvements
-Deep Learning disease prediction
-Neural network-based classification
-Large Language Model healthcare assistant
-Explainable AI integration
-Healthcare Features
-Voice-based medical assistant
-Medical document analysis
-Personalized health recommendations
-Doctor recommendation system
-Appointment management
-Machine Learning Improvements
-Larger medical datasets
-Better confidence calibration
-SHAP model explanations
-Continuous learning pipeline





⚠️ Medical Disclaimer

This application is developed for educational and research purposes only.
The predictions generated by this system should not replace professional medical advice, diagnosis, or treatment.
Always consult qualified healthcare professionals for medical decisions.



Markdown

Developer
Summiya Yousaf

Bachelor of Science in Artificial Intelligence
Air University Islamabad


Areas of Interest:

Artificial Intelligence
Machine Learning
Healthcare AI
Computer Vision
NLP

Version:
AI Medical Assistant v1.0


⭐ If you found this project interesting, consider giving it a star!
