import streamlit as st

st.title("🥗 Nutrition Log")

target = 2000
calories = st.number_input("Calories consumed today", min_value=0)

# SAFE COMPARISON: Comparing one integer to another integer
if calories > target:
 st.warning(f"You are {calories - target} calories over your limit.")
elif calories > 0:
 st.success(f"You have {target - calories} calories remaining!")