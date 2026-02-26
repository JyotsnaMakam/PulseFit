import streamlit as st

st.title("🥗 Personalized Nutrition Logic")

# 1. Get User Physical Data
col_phys1, col_phys2, col_phys3 = st.columns(3)
with col_phys1:
 weight = st.number_input("Weight (kg)", min_value=40.0, value=70.0)
with col_phys2:
 height = st.number_input("Height (cm)", min_value=100.0, value=170.0)
with col_phys3:
 age = st.number_input("Age", min_value=15, value=25)

# 2. Calculate BMR (Mifflin-St Jeor Equation)
# For this example, we'll use the Male formula; you can add a gender toggle later
bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
tdee = bmr * 1.2 # Assuming sedentary activity level

# 3. Calculate Target Macros (Standard 30/40/30 split)
target_protein = (tdee * 0.30) / 4
target_carbs = (tdee * 0.40) / 4
target_fats = (tdee * 0.30) / 9

st.info(f"Your Daily Target: {int(target_protein)}g Protein | {int(target_carbs)}g Carbs | {int(target_fats)}g Fats")

# 4. Input Current Consumption
st.subheader("What have you eaten today?")
c1, c2, c3 = st.columns(3)
p_in = c1.number_input("Protein In (g)", 0)
c_in = c2.number_input("Carbs In (g)", 0)
f_in = c3.number_input("Fats In (g)", 0)

# 5. The Comparison Message
if st.button("Check My Progress"):
# Check Protein
 if p_in < target_protein - 10:
  st.warning(f"You need {int(target_protein - p_in)}g more Protein.")
 elif p_in > target_protein + 10:
  st.error("You are exceeding your Protein goal.")
 else:
  st.success("Protein intake is perfect!")

# Check Carbs/Fats similarly...
 st.write(f"Total Calories Consumed: {int((p_in*4)+(c_in*4)+(f_in*9))} / {int(tdee)} kcal")