from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    jsonify,
    send_file,
    flash
)

import sqlite3
import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime
from reportlab.pdfgen import canvas



# ============================
# FLASK CONFIGURATION
# ============================

app = Flask(__name__)

app.secret_key = "medicalassistant123"


latest_report = {}
# ==========================
# Disease Knowledge Base
# ==========================

DISEASE_INFO = {

    "Fungal infection": {
        "description": "A fungal infection is caused by fungi affecting the skin, nails, or internal organs.",
        "precautions": [
            "Keep affected area clean and dry.",
            "Maintain proper hygiene.",
            "Avoid sharing towels or clothing.",
            "Consult a dermatologist if symptoms worsen."
        ]
    },

    "Allergy": {
        "description": "An allergy occurs when the immune system reacts to substances that are normally harmless.",
        "precautions": [
            "Avoid known allergens.",
            "Stay hydrated.",
            "Use prescribed antihistamines.",
            "Consult your doctor if symptoms become severe."
        ]
    },

    "GERD": {
        "description": "GERD is a digestive disorder where stomach acid frequently flows back into the esophagus.",
        "precautions": [
            "Avoid spicy food.",
            "Eat smaller meals.",
            "Do not lie down immediately after eating.",
            "Consult a gastroenterologist if symptoms persist."
        ]
    },

    "Common Cold": {
        "description": "A viral infection affecting the upper respiratory tract.",
        "precautions": [
            "Drink plenty of fluids.",
            "Get enough rest.",
            "Take warm beverages.",
            "Seek medical advice if symptoms worsen."
        ]
    }
}



# ============================
# DATABASE PATH
# ============================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_PATH = os.path.join(
    BASE_DIR,
    "user.db"
)

print(DB_PATH)



# ============================
# HOME
# ============================

@app.route("/")
def home():

    return redirect("/login")



# ============================
# DASHBOARD
# ============================

@app.route("/dashboard")
def dashboard():

    # User must be logged in
    if "user_id" not in session:
        flash("Please login first.", "error")
        return redirect("/login")

    username = session.get("name", "User")

    hour = datetime.now().hour

    if hour < 12:
        greeting = "Good Morning"
    elif hour < 17:
        greeting = "Good Afternoon"
    elif hour < 21:
        greeting = "Good Evening"
    else:
        greeting = "Good Night"

    return render_template(
        "dashboard.html",
        username=username,
        greeting=greeting
    )



# ============================
# LOGIN
# ============================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "GET":
        session.pop('_flashes', None)
        return render_template("login.html")

    session.clear()

    email = request.form["email"]
    password = request.form["password"]

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM users
        WHERE email=? AND password=?
    """, (email, password))

    user = cursor.fetchone()

    print("USER FROM DATABASE:", user)

    conn.close()

    if user:

        session["user_id"] = user[0]
        session["name"] = user[1]
        session["email"] = user[2]

        print("SESSION NAME:", session["name"])
        print("SESSION EMAIL:", session["email"])

        return redirect("/dashboard")

    else:

        flash("Invalid Email or Password", "error")
        return redirect("/login")

# ============================
# SIGNUP PAGE
# ============================

@app.route("/signup")

def signup():

    return render_template(
        "signup.html"
    )





# ============================
# REGISTER USER
# ============================

@app.route("/register", methods=["POST"])
def register():

    name = request.form["name"].strip()
    email = request.form["email"].strip()
    password = request.form["password"]

    try:

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Check if email already exists
        cursor.execute(
            "SELECT * FROM users WHERE email=?",
            (email,)
        )

        existing_user = cursor.fetchone()

        if existing_user:

            conn.close()

            flash(
                "Email already registered. Please login or use another email.",
                "error"
            )

            return redirect("/signup")

        # Insert new user
        cursor.execute(
            """
            INSERT INTO users
            (name,email,password)
            VALUES (?,?,?)
            """,
            (name, email, password)
        )

        conn.commit()
        conn.close()

        flash(
            "Account created successfully! Please login.",
            "success"
        )

        return redirect("/login")

    except sqlite3.Error as e:

        try:
            conn.close()
        except:
            pass

        print("Database Error:", e)

        flash(
            "Something went wrong. Please try again.",
            "error"
        )

        return redirect("/signup")


def get_medical_advice(disease):

    disease = disease.lower()

    advice = {
        "flu": [
            "- Get plenty of rest.",
            "- Drink plenty of fluids.",
            "- Monitor your temperature regularly.",
            "- Visit a doctor if symptoms worsen."
        ],

        "common cold": [
            "- Stay hydrated.",
            "- Take adequate rest.",
            "- Increase Vitamin C intake.",
            "- Avoid close contact with others."
        ],

        "diabetes": [
            "- Monitor blood sugar regularly.",
            "- Maintain a healthy diet.",
            "- Exercise daily.",
            "- Follow your doctor's treatment plan."
        ],

        "hypertension": [
            "- Reduce salt intake.",
            "- Exercise regularly.",
            "- Monitor blood pressure.",
            "- Take prescribed medicines on time."
        ],

        "heart attack": [
            "- Seek emergency medical attention immediately.",
            "- Call emergency services.",
            "- Do not delay professional treatment."
        ],

        "migraine": [
            "- Rest in a quiet dark room.",
            "-Stay hydrated.",
            "- Reduce caffeine intake.",
            "- Consult a neurologist if frequent."
        ]
    }

    return advice.get(
        disease,
        [
            "- Drink enough water.",
            "- Eat a balanced diet.",
            "- Get enough rest.",
            "- Consult a healthcare professional."
        ]
    )

# ============================
# DISEASE PREDICTION
# ============================


@app.route(
    "/predict",
    methods=["GET","POST"]
)

def predict():



    MODEL_DIR = os.path.join(

        BASE_DIR,

        "models"

    )



    symptoms = joblib.load(

        os.path.join(
            MODEL_DIR,
            "symptoms.pkl"
        )

    )



    model = joblib.load(

        os.path.join(
            MODEL_DIR,
            "random_forest_model.pkl"
        )

    )



    label_encoder = joblib.load(

        os.path.join(
            MODEL_DIR,
            "label_encoder.pkl"
        )

    )





    if request.method == "GET":


        return render_template(

            "predict.html",

            symptoms=symptoms

        )




    # --------------------------
    # PATIENT DATA
    # --------------------------


    name = request.form["name"]

    age = request.form["age"]

    gender = request.form["gender"]



    other_symptoms = request.form.get(

        "other_symptoms",

        ""

    )





    # --------------------------
    # CREATE FEATURE VECTOR
    # --------------------------


    input_data = []

    selected_symptoms = []




    for symptom in symptoms:


        value = request.form.get(symptom)



        if value is not None:


            input_data.append(1)

            selected_symptoms.append(symptom)



        else:


            input_data.append(0)






    print(
        "Input Vector Length:",
        len(input_data)
    )

    print(
        "Selected Symptoms:",
        selected_symptoms
    )





    # --------------------------
    # MODEL PREDICTION
    # --------------------------


    prediction = model.predict(

        [input_data]

    )



    disease = label_encoder.inverse_transform(

        prediction

    )[0]

    medical_advice = get_medical_advice(disease)
    info = DISEASE_INFO.get(
    disease,
    {
        "description": "No detailed medical description available for this disease.",
        "precautions": [
            "Consult a qualified healthcare professional.",
            "Maintain a healthy lifestyle.",
            "Stay hydrated.",
            "Follow medical advice."
        ]
    }
)



    probability = model.predict_proba(

        [input_data]

    )



    confidence = round(

        max(probability[0]) * 100,

        2

    )

    global latest_report



    latest_report = {


        "name":name,

        "age":age,

        "gender":gender,

        "disease":disease,

        "confidence":confidence,

        "other_symptoms":other_symptoms

    }
    current_date = datetime.now().strftime("%d %B %Y")

    current_time = datetime.now().strftime("%I:%M %p")

    return render_template(
    "report.html",
    name=name,
    age=age,
    gender=gender,
    disease=disease,
    confidence=confidence,
    other_symptoms=other_symptoms,
    selected_symptoms=selected_symptoms,
    medical_advice=medical_advice
)

    
# ============================
# PDF MEDICAL REPORT
# ============================


@app.route("/download_pdf")
def download_pdf():


    pdf_path = "Medical_Report.pdf"



    c = canvas.Canvas(pdf_path)



    c.setFont(
        "Helvetica-Bold",
        18
    )


    c.drawString(
        180,
        800,
        "AI Medical Report"
    )



    c.setFont(
        "Helvetica",
        12
    )



    c.drawString(
        50,
        760,
        f"Name: {latest_report.get('name','')}"
    )


    c.drawString(
        50,
        735,
        f"Age: {latest_report.get('age','')}"
    )


    c.drawString(
        50,
        710,
        f"Gender: {latest_report.get('gender','')}"
    )


    c.drawString(
        50,
        685,
        f"Disease: {latest_report.get('disease','')}"
    )


    c.drawString(
        50,
        660,
        f"Confidence: {latest_report.get('confidence','')}%"
    )


    c.drawString(
        50,
        635,
        f"Symptoms: {latest_report.get('other_symptoms','')}"
    )



    c.save()



    return send_file(
        pdf_path,
        as_attachment=True
    )






# ============================
# PREVIOUS REPORTS
# ============================


@app.route("/reports")
def reports():



    if "user_id" not in session:

        return redirect("/login")




    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()



    cursor.execute(

        """
        SELECT *
        FROM reports
        ORDER BY report_date DESC
        """

    )


    reports = cursor.fetchall()



    conn.close()



    return render_template(

        "previousreports.html",

        reports=reports

    )


# ============================
# PROFILE
# ============================


@app.route("/profile")
def profile():



    if "user_id" not in session:

        return redirect("/login")



    return render_template(

        "profile.html",

        name=session["name"],

        email=session["email"]

    )


# ============================
# SETTINGS
# ============================


@app.route("/settings")
def settings():



    if "user_id" not in session:

        return redirect("/login")



    return render_template(

        "settings.html",

        name=session["name"],

        email=session["email"]

    )


# ============================
# ANALYTICS
# ============================


@app.route("/analytics")
def analytics():



    conn = sqlite3.connect(DB_PATH)



    df = pd.read_sql_query(

        "SELECT * FROM reports",

        conn

    )



    conn.close()




    if len(df)==0:


        return render_template(

            "analytics.html",

            total_predictions=0

        )




    total_predictions = len(df)



    most_common = (

        df["disease"]

        .value_counts()

        .idxmax()

    )



    average_confidence = round(

        df["confidence"].mean(),

        2

    )

    os.makedirs(

        "static/charts",

        exist_ok=True

    )





    # Disease Pie Chart


    disease_counts = df["disease"].value_counts()



    plt.figure(
        figsize=(6,6)
    )


    plt.pie(

        disease_counts,

        labels=disease_counts.index,

        autopct="%1.1f%%"

    )


    plt.title(
        "Disease Distribution"
    )



    pie_path = "static/charts/disease_pie.png"



    plt.savefig(
        pie_path
    )


    plt.close()






    # Disease Bar Chart


    plt.figure(
        figsize=(8,5)
    )



    disease_counts.plot(
        kind="bar"
    )


    plt.title(
        "Top Predicted Diseases"
    )


    plt.xlabel(
        "Disease"
    )


    plt.ylabel(
        "Patients"
    )


    plt.xticks(
        rotation=45
    )


    plt.tight_layout()



    bar_path = "static/charts/disease_bar.png"



    plt.savefig(
        bar_path
    )


    plt.close()




    return render_template(

        "analytics.html",

        total_predictions=total_predictions,

        most_common=most_common,

        average_confidence=average_confidence,

        pie_chart=pie_path,

        bar_chart=bar_path

    )






# ============================
# AI ASSISTANT PAGE
# ============================


@app.route("/assistant")
def assistant():

    return render_template(
        "assistant.html"
    )






# ============================
# FLOATING CHAT API
# ============================


@app.route(
    "/chat",
    methods=["POST"]
)

def chat():



    data = request.get_json()



    message = data["message"].lower()




    if "fever" in message:


        reply = """

        Fever may happen because your body is
        fighting an infection.

        Drink water, rest and monitor your temperature.

        """



    elif "cough" in message:


        reply = """

        Cough can occur due to infection,
        allergy or irritation.

        Persistent cough should be checked by a doctor.

        """



    elif "diabetes" in message:


        reply = """

        Diabetes affects blood glucose levels.

        Healthy diet, exercise and medical guidance
        are important.

        """



    elif "headache" in message:


        reply = """

        Headache can happen due to stress,
        dehydration or lack of sleep.

        """



    else:


        reply = """

        I can help explain symptoms,
        diseases and healthcare information.

        For diagnosis please consult a healthcare professional.

        """





    return jsonify({

        "reply":reply

    })


# ============================
# LOGOUT
# ============================


@app.route("/logout")
def logout():


    if "user_id" not in session:

        return redirect("/login")



    return render_template(
        "logout.html"
    )



@app.route("/confirm_logout")
def confirm_logout():


    session.clear()



    flash(

        "You have been logged out successfully.",

        "success"

    )



    return render_template(

        "logout_success.html"

    )



# ============================
# EDIT PROFILE
# ============================


@app.route("/edit_profile")
def edit_profile():


    if "user_id" not in session:

        return redirect("/login")



    return render_template(

        "edit_profile.html",

        name=session["name"],

        email=session["email"]

    )




@app.route(
    "/update_profile",
    methods=["POST"]
)

def update_profile():



    if "user_id" not in session:

        return redirect("/login")




    new_name = request.form["name"]

    new_email = request.form["email"]




    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()



    cursor.execute(

        """

        UPDATE users

        SET name=?, email=?

        WHERE id=?

        """,

        (

            new_name,

            new_email,

            session["user_id"]

        )

    )



    conn.commit()

    conn.close()




    session["name"] = new_name

    session["email"] = new_email




    flash(

        "Profile updated successfully!",

        "success"

    )



    return redirect("/profile")


# ============================
# AI ASSISTANT CHAT
# ============================

@app.route("/assistant_chat", methods=["POST"])
def assistant_chat():

    data = request.get_json()

    message = data["message"].lower()


    if "hello" in message or "hi" in message:

        reply = "👋 Hello! How can I help you today?"

    elif "fever" in message:

        reply = """
Fever is a temporary increase in body temperature,
usually caused by an infection.

• Drink plenty of water.
• Get enough rest.
• Monitor your temperature.
• Consult a doctor if fever lasts more than 2–3 days or becomes very high.
"""

    elif "diabetes" in message:

        reply = """
Diabetes is a condition where blood sugar remains high.

• Eat a balanced diet.
• Exercise regularly.
• Avoid excessive sugar.
• Follow your doctor's medication plan.
"""

    elif "cough" in message:

        reply = """
A cough may occur because of:

• Viral infection
• Allergy
• Dust
• Cold

If it lasts more than 2 weeks, visit a doctor.
"""

    elif "headache" in message:

        reply = """
Headaches may occur because of:

• Stress
• Dehydration
• Lack of sleep

Drink water and rest.
"""

    else:

        reply = """
I'm here to help explain diseases, symptoms,
healthy lifestyle habits and medical information.

For diagnosis, always consult a qualified doctor.
"""

    return jsonify({
        "reply": reply
    })







# ============================
# RUN APPLICATION
# ============================


if __name__ == "__main__":


    app.run(
        debug=True
    )

