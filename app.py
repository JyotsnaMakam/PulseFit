import streamlit as st

st.title("🏃 Activity Tracker")

# Activity data (Calories per minute)
burn_rates = {
    "Walking": 4,
    "Running": 11,
    "Cycling": 8,
    "Yoga": 3
}

activity = st.selectbox("What did you do today?", list(burn_rates.keys()))
duration = st.number_input("Duration (minutes)", min_value=1, max_value=480, value=30)

if st.button("Calculate Burn"):
    calories = duration * burn_rates[activity]
    st.metric(label="Estimated Calories Burned", value=f"{calories} kcal")
    st.success(f"Great job! You burned approximately {calories} calories doing {activity}.")