import streamlit as st

st.set_page_config(page_title="PulseFit Home", layout="wide")

# Initialize Session State if it doesn't exist
if 'total_calories' not in st.session_state:
 st.session_state['total_calories'] = 0
if 'water_liters' not in st.session_state:
 st.session_state['water_liters'] = 0.0

st.title("🚀 PulseFit Dashboard")

# Display real-time metrics from other pages
col1, col2 = st.columns(2)
col1.metric("Food Intake", f"{st.session_state['total_calories']} kcal")
col2.metric("Hydration", f"{st.session_state['water_liters']} L")

st.write("Go to the sidebar to update your daily logs!")