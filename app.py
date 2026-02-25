import streamlit as st

# Must be the first line to prevent errors
st.set_page_config(page_title="PulseFit Dashboard", layout="wide")

st.title("🏃‍♂️ PulseFit: Your Personal Health Hub")
st.write("Welcome! Tracking your daily activity is the first step to a healthier you.")

# Dashboard Metrics
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Daily Step Goal", value="10,000", delta="800 to go")
with col2:
    st.metric(label="Hydration", value="2.1L", delta="Target: 3L")

st.divider()
st.info("Use the sidebar on the left to log your Workouts or Meals.")