import streamlit as st

st.title("🥗 Diet & Nutrition")

st.subheader("Daily Macros")
col1, col2, col3 = st.columns(3)

with col1:
 protein = st.number_input("Protein (g)", 0)
with col2:
 carbs = st.number_input("Carbs (g)", 0)
with col3:
 fats = st.number_input("Fats (g)", 0)

# Water Tracker
st.divider()
st.subheader("💧 Water Intake")
glasses = st.slider("How many glasses of water?", 0, 12, 0)
progress = glasses / 8 # Assuming 8 is the goal
st.progress(min(progress, 1.0))

if glasses >= 8:
 st.balloons()
 st.write("Target reached! You are well hydrated.")