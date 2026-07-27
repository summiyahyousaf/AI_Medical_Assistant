from datetime import datetime
import json
import os


# Load JSON files
def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


descriptions = load_json("../data/disease_descriptions.json")
symptoms_info = load_json("../data/disease_symptoms.json")
precautions = load_json("../data/disease_precautions.json")
medications = load_json("../data/disease_medications.json")
general_advice = load_json("../data/disease_general_advice.json")
specialists = load_json("../data/disease_specialists.json")
hospitals = load_json("../data/recommended_hospitals.json")
risk_levels = load_json("../data/risk_levels.json")
emergency_diseases = load_json("../data/emergency_disease.json")
urgency_messages = load_json("../data/urgency_messages.json")



# Generate Medical Report
def generate_report(result):

    # Get prediction result
    disease = result["disease"]
    confidence = result["confidence"]
    recognized = result["recognized"]
    ignored = result["ignored"]
    entered = result["entered"]


    # Date and time
    now = datetime.now()

    current_date = now.strftime("%d %B %Y")
    current_time = now.strftime("%I:%M %p")
    report_id = now.strftime("AI-%Y%m%d-%H%M%S")


    # Risk level
    risk = risk_levels.get(disease, "Unknown")


    # Create reports folder
    os.makedirs("../reports", exist_ok=True)

    report_file = f"../reports/{report_id}.txt"



    # Save report
    with open(report_file, "w", encoding="utf-8") as file:

        file.write(
f"""
============================================================
                  MEDICAL REPORT
============================================================

Date:
{current_date}

Time:
{current_time}

Report ID:
{report_id}


Symptoms Entered:
{", ".join(entered)}


Recognized Symptoms:
{", ".join(recognized)}


Ignored Symptoms:
{", ".join(ignored)}


Predicted Disease:
{disease}


Risk Level:
{risk}


Confidence:
{confidence:.2f}%


Description:
{descriptions.get(disease, "Information not available.")}


Precautions:
{precautions.get(disease, [])}


Medications:
{medications.get(disease, [])}


General Advice:
{general_advice.get(disease, [])}


Specialist:
{specialists.get(disease, "Information not available.")}


Recommended Hospitals:
{hospitals.get(disease, [])}



DISCLAIMER:

This prediction is generated using a Machine Learning model
and is intended for educational purposes only.

It is NOT a substitute for professional medical diagnosis.

Always consult a qualified healthcare professional before
taking medication or making health decisions.


============================================================
                 ~ Summiya Yousaf
============================================================
"""
        )


    print(f"\nReport saved successfully!")
    print(f"Location: {report_file}")



    # Terminal Report

    print("\n")
    print("=" * 60)
    print(" MEDICAL REPORT")
    print("=" * 60)


    print(f"Date : {current_date}")
    print(f"Time : {current_time}")
    print(f"Report ID : {report_id}")



    print("\nSymptoms Entered:")
    print(", ".join(entered))


    print("\nRecognized Symptoms:")
    if recognized:
        print(", ".join(recognized))
    else:
        print("None")


    print("\nIgnored Symptoms:")
    if ignored:
        print(", ".join(ignored))
    else:
        print("None")



    print("\n" + "=" * 60)
    print("PREDICTED DISEASE")
    print("=" * 60)

    print(disease)



    # Emergency warning

    if disease in emergency_diseases:

        print("\n" + "=" * 60)
        print("🚨 EMERGENCY WARNING")
        print("=" * 60)

        print(
            urgency_messages.get(
                "Emergency",
                "Seek immediate medical attention."
            )
        )



    print("\n" + "=" * 60)
    print("RISK ASSESSMENT")
    print("=" * 60)

    print(f"Risk Level : {risk}")

    print("\nUrgent Action:")

    print(
        urgency_messages.get(
            risk,
            "Consult a healthcare professional."
        )
    )



    print("\n" + "=" * 60)
    print("PREDICTION CONFIDENCE")
    print("=" * 60)

    print(f"{confidence:.2f}%")



    if confidence >= 90:
        print("Prediction Reliability : Very High")

    elif confidence >= 75:
        print("Prediction Reliability : High")

    elif confidence >= 60:
        print("Prediction Reliability : Moderate")

    else:
        print("Prediction Reliability : Low")



    print("\n" + "=" * 60)
    print("DESCRIPTION")
    print("=" * 60)

    print(
        descriptions.get(
            disease,
            "Information not available."
        )
    )



    print("\n" + "=" * 60)
    print("SYMPTOMS")
    print("=" * 60)


    for item in symptoms_info.get(disease, []):
        print(f"• {item}")



    print("\n" + "=" * 60)
    print("PRECAUTIONS")
    print("=" * 60)


    for item in precautions.get(disease, []):
        print(f"• {item}")



    print("\n" + "=" * 60)
    print("MEDICATIONS")
    print("=" * 60)


    for item in medications.get(disease, []):
        print(f"• {item}")



    print("\n" + "=" * 60)
    print("GENERAL HEALTH ADVICE")
    print("=" * 60)


    for item in general_advice.get(disease, []):
        print(f"• {item}")



    print("\n" + "=" * 60)
    print("SPECIALIST CONSULTATION")
    print("=" * 60)

    print(
        specialists.get(
            disease,
            "Information not available."
        )
    )



    print("\n" + "=" * 60)
    print("RECOMMENDED HOSPITALS")
    print("=" * 60)


    for item in hospitals.get(disease, []):
        print(f"• {item}")



    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)


    print(f"Disease       : {disease}")
    print(f"Risk Level    : {risk}")
    print(f"Confidence    : {confidence:.2f}%")



    print("\n" + "=" * 60)
    print("DISCLAIMER")
    print("=" * 60)


    print(
        "This prediction is generated using a Machine Learning model "
        "and is intended for educational purposes only."
    )

    print(
        "It is NOT a substitute for professional medical diagnosis."
    )

    print(
        "Always consult a qualified healthcare professional before "
        "taking any medication or making health-related decisions."
    )


    print("=" * 60)


    # Signature

    print()
    print(f"{'~ Summiya Yousaf':>60}")
    print("=" * 60)