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
target=8
progress = glasses / target # Assuming 8 is the goal
st.progress(min(progress, 1.0))

if glasses >= target:
 st.balloons()
 st.write("Target reached! You are well hydrated.")
else:
    st.write(f"Keep going! {target - glasses} more glasses to reach your goal.") 