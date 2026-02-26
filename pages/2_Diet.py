import streamlit as st

st.title("🥗 Personalized Nutrition & Hydration")

# 1. Physical Data Inputs
col_phys1, col_phys2, col_phys3 = st.columns(3)
with col_phys1:
 weight = st.number_input("Weight (kg)", min_value=40.0, value=70.0)
with col_phys2:
 height = st.number_input("Height (cm)", min_value=100.0, value=170.0)
with col_phys3:
 age = st.number_input("Age", min_value=15, value=25)

# 2. Macro Calculations (Mifflin-St Jeor)
bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
tdee = bmr * 1.2 # Daily calorie target
target_protein = (tdee * 0.30) / 4
target_carbs = (tdee * 0.40) / 4
target_fats = (tdee * 0.30) / 9

# 3. Water Calculation (33ml per kg)
water_target_liters = (weight * 0.033)

st.info(f"Targets: {int(target_protein)}g Protein | {int(target_carbs)}g Carbs | {int(target_fats)}g Fats | {water_target_liters:.1f}L Water")

# 4. Nutrition Inputs
st.subheader("Daily Intake")
c1, c2, c3 = st.columns(3)
p_in = c1.number_input("Protein (g)", 0)
c_in = c2.number_input("Carbs (g)", 0)
f_in = c3.number_input("Fats (g)", 0)

# 5. Water Tracker
st.divider()
st.subheader("💧 Water Tracker")

# 1. Create the input for the user
water_consumed = st.number_input("Liters of water consumed today", min_value=0.0, step=0.1)

# 2. Show a progress bar
if water_target_liters > 0:
 progress = min(water_consumed / water_target_liters, 1.0)
 st.progress(progress)

# 3. Display the personalized message
if water_consumed >= water_target_liters:
 st.success(f"✅ Goal Reached! You've had {water_consumed}L.")
else:
 needed = water_target_liters - water_consumed
 st.warning(f"⚠️ You need {needed:.1f}L more to reach your daily goal of {water_target_liters:.1f}L.")

# Final Calorie Check
total_cals = (p_in*4) + (c_in*4) + (f_in*9)
st.metric("Total Calories", f"{int(total_cals)} / {int(tdee)} kcal")