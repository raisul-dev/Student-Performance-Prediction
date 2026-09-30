import streamlit as st
import pandas as pd
import joblib


# Load trained model
model = joblib.load("student_performance_model.pkl")


# Page configuration
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)


# Custom CSS
st.markdown("""
<style>

.main-title {
    text-align: center;
    font-size: 38px;
    font-weight: 700;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #777;
    font-size: 16px;
    margin-bottom: 30px;
}

.result-box {
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    margin-top: 25px;
}

.score {
    font-size: 42px;
    font-weight: 700;
}

.label {
    font-size: 17px;
    color: #666;
}

</style>
""", unsafe_allow_html=True)


# Header
st.markdown(
    '<div class="main-title">🎓 Student Performance Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Predict a student\'s total score using a Machine Learning model.'
    '</div>',
    unsafe_allow_html=True
)


# Input section
st.subheader("Student Information")


weekly_self_study_hours = st.number_input(
    "📚 Weekly Self Study Hours",
    min_value=0.0,
    max_value=100.0,
    value=8.0,
    step=1.0
)


attendance_percentage = st.number_input(
    "📅 Attendance Percentage",
    min_value=0.0,
    max_value=100.0,
    value=90.0,
    step=1.0
)


class_participation = st.number_input(
    "🙋 Class Participation",
    min_value=0.0,
    max_value=100.0,
    value=85.0,
    step=1.0
)


# Prediction button
st.write("")

if st.button(
    "🎯 Predict Total Score",
    use_container_width=True
):

    # Create input DataFrame
    new_student = pd.DataFrame(
        [[
            weekly_self_study_hours,
            attendance_percentage,
            class_participation
        ]],
        columns=[
            "weekly_self_study_hours",
            "attendance_percentage",
            "class_participation"
        ]
    )

    # Prediction
    prediction = model.predict(new_student)

    predicted_score = prediction[0]


    # Performance message
    if predicted_score >= 80:
        message = "Excellent predicted performance! 🌟"

    elif predicted_score >= 70:
        message = "Good predicted performance! 👍"

    elif predicted_score >= 60:
        message = "Average predicted performance. 📚"

    else:
        message = "More improvement may be needed. 💪"


    # Result
    st.markdown(
        f"""
        <div class="result-box">
            <div class="label">Predicted Total Score</div>
            <div class="score">{predicted_score:.2f}</div>
            <div>{message}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


st.write("")

st.caption(
    "Built with Python, Scikit-learn and Streamlit"
)