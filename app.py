import streamlit as st
import pickle
import os
import pandas as pd

@st.cache_resource
def load_model():
    model_path = os.path.join(os.path.dirname(__file__), "scripts", "dtree_model.pkl")
    with open(model_path, "rb") as f:
        obj = pickle.load(f)

    # Handle both (model, dv) or just model
    if isinstance(obj, tuple):
        model, dv = obj
    else:
        model, dv = obj, None
    return model, dv

model, dv = load_model()

st.set_page_config(page_title="Student Performance Prediction")

st.title("Student Performance Prediction App")
st.write("Enter the student's information below to predict their final grade.")

school = st.selectbox("School", ["GP", "MS"])
gender = st.selectbox("Gender", ["M", "F"])
age = st.number_input("Age", min_value=15, max_value=22, value=17)
address = st.selectbox("Address", ["U", "R"])
famsize = st.selectbox("Family Size", ["LE3", "GT3"])
pstatus = st.selectbox("Parental Status", ["T", "A"])
medu = st.selectbox("Mother's Education", ["none", "primary education (4th grade)", "5th to 9th grade", "secondary education", "higher education"])
fedu = st.selectbox("Father's Education", ["none", "primary education (4th grade)", "5th to 9th grade", "secondary education", "higher education"])
mjob = st.selectbox("Mother's Job", ["teacher", "health", "services", "at_home", "other"])
fjob = st.selectbox("Father's Job", ["teacher", "health", "services", "at_home", "other"])
reason = st.selectbox("Reason for Choosing School", ["home", "reputation", "course", "other"])
guardian = st.selectbox("Guardian", ["mother", "father", "other"])
travel_time = st.selectbox("Travel Time", ["<15 min", "15 to 30 min", "30 min to 1 hour", ">1 hour"])
study_time = st.selectbox("Study Time", ["<2 hours", "2 to 5 hours", "5 to 10 hours", ">10 hours"])
failures = st.number_input("Number of Past Failures", min_value=0, max_value=4, value=0)
schoolsup = st.selectbox("School Support", ["yes", "no"])
famsup = st.selectbox("Family Support", ["yes", "no"])
paid = st.selectbox("Paid Classes", ["yes", "no"])
activities = st.selectbox("Extracurricular Activities", ["yes", "no"])
nursery = st.selectbox("Attended Nursery", ["yes", "no"])
higher = st.selectbox("Wants Higher Education", ["yes", "no"])
internet = st.selectbox("Internet Access at Home", ["yes", "no"])
romantic = st.selectbox("In a Romantic Relationship", ["yes", "no"])
famrel = st.selectbox("Family Relationship Quality", ["very bad", "bad", "average", "good", "excellent"])
freetime = st.selectbox("Free Time After School", ["very low", "low", "average", "high", "very high"])
goout = st.selectbox("Going Out with Friends", ["very low", "low", "average", "high", "very high"])
dalc = st.selectbox("Workday Alcohol Consumption", ["very low", "low", "average", "high", "very high"])
walc = st.selectbox("Weekend Alcohol Consumption", ["very low", "low", "average", "high", "very high"])
health = st.selectbox("Current Health Status", ["very bad", "bad", "average", "good", "very good"])
absences = st.number_input("Number of Absences", min_value=0, max_value=100, value=4)
g1 = st.number_input("First Period Grade (G1)", min_value=0, max_value=20, value=10)
g2 = st.number_input("Second Period Grade (G2)", min_value=0, max_value=20, value=10)

# --- Predict Button ---
if st.button("Predict Final Grade (G3)"):
    # Convert user input
    data = {
        "school": school,
        "sex": gender,
        "age": age,
        "address": address,
        "famsize": famsize,
        "pstatus": pstatus,
        "medu": medu,
        "fedu": fedu,
        "mjob": mjob,
        "fjob": fjob,
        "reason": reason,
        "guardian": guardian,
        "travel_time": travel_time,
        "study_time": study_time,
        "failures": failures,
        "schoolsup": schoolsup,
        "famsup": famsup,
        "paid": paid,
        "activities": activities,
        "nursery": nursery,
        "higher": higher,
        "internet": internet,
        "romantic": romantic,
        "famrel": famrel,
        "freetime": freetime,
        "goout": goout,
        "dalc": dalc,
        "walc": walc,
        "health": health,
        "absences": absences,
        "g1": g1,
        "g2": g2
    }

    # Transform if DictVectorizer exists
    if dv is not None:
        X = dv.transform([data])
    else:
        X = pd.DataFrame([data])


    pred = model.predict(X)[0]

    try:
        pred_int = int(pred)
        if pred_int:
            st.success(f"Predicted Final Grade: **{pred_int}**")
    except Exception:
        pass
