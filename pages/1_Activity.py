import streamlit as st

st.title("👟 Activity Tracker")

# Using a form prevents the app from "re-running" every time you type a letter
with st.form("activity_form"):
 activity_type = st.selectbox("Activity", ["Walking", "Running", "Cycling"])
 duration = st.number_input("Duration (minutes)", min_value=1)
 submit = st.form_submit_button("Log Activity")

if submit:
 st.success(f"Great job! You logged {duration} minutes of {activity_type}.")