import streamlit as st
import pickle
import pandas as pd

# Load Model
with open("models/student_performance_model.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="📚"
)

st.sidebar.title("About Project")

st.sidebar.info(
    """
    Student Performance Prediction System

    Built using:
    - Python
    - Pandas
    - Scikit-Learn
    - Streamlit
    """
)

st.title("📚 Student Performance Prediction System")

st.write(
    "Enter student details and predict exam score."
)

# Inputs
hours_studied = st.slider("Hours Studied", 1, 30, 10)
attendance = st.slider("Attendance (%)", 50, 100, 75)
previous_scores = st.slider("Previous Scores", 40, 100, 70)
tutoring_sessions = st.slider("Tutoring Sessions", 0, 10, 2)
sleep_hours = st.slider("Sleep Hours", 4, 10, 7)
physical_activity = st.slider("Physical Activity", 0, 10, 3)

# Dummy values for remaining features
input_data = pd.DataFrame({
    "Hours_Studied": [hours_studied],
    "Attendance": [attendance],
    "Parental_Involvement": [1],
    "Access_to_Resources": [1],
    "Extracurricular_Activities": [1],
    "Sleep_Hours": [sleep_hours],
    "Previous_Scores": [previous_scores],
    "Motivation_Level": [1],
    "Internet_Access": [1],
    "Tutoring_Sessions": [tutoring_sessions],
    "Family_Income": [1],
    "Teacher_Quality": [1],
    "School_Type": [1],
    "Peer_Influence": [1],
    "Physical_Activity": [physical_activity],
    "Learning_Disabilities": [0],
    "Parental_Education_Level": [1],
    "Distance_from_Home": [1],
    "Gender": [1]
})
if st.button("Predict Score"):

    prediction = model.predict(input_data)

    predicted_score = prediction[0]

    st.success(
        f"Predicted Exam Score: {predicted_score:.2f}"
    )

    if predicted_score >= 85:
        st.balloons()
        st.info("Excellent Performance Expected ⭐")

    elif predicted_score >= 70:
        st.info("Good Performance Expected 👍")

    elif predicted_score >= 50:
        st.warning("Average Performance Expected 📚")

    else:
        st.error("Needs Improvement ⚠️")

