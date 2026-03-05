import streamlit as st
import requests # You might need to run 'pip install requests' in your venv
if 'total_calories' not in st.session_state:
    st.session_state['total_calories'] = 0
def get_nutrition_data(query):
 api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
# Replace the text below with your actual API Key
 headers = {'X-Api-Key':'iSNPL2eyrSff8nedAKuMzpS3fLNu6ejJd8zMHPIs'}
 try:
   response = requests.get(api_url + query, headers=headers)
 #return response.json()

   if response.status_code == 200:
    return response.json() # This returns a list of food items
   else:
    print(f"Error: {response.status_code} - {response.text}")
    return None
 except Exception as e:
    print(f"Exception occurred: {e}")
    return None
st.title("🥗 Personalized Nutrition & Hydration")
# 2. THE SEARCH UI (Place it here!)
st.subheader("🔍 Quick Log")
food_input = st.text_input("What did you eat?", placeholder="e.g., 2 slices of pizza")
if st.button("Log Food"):
 if food_input:
# This is where the 'Real-Time' magic happens
  data = get_nutrition_data(food_input)
  if data and isinstance(data, list) and len(data) > 0:
     try:
       new_cals=sum(float(item.get('calories', 0)) for item in data if isinstance(item,dict) and 'calories' in item)
# logic to update session_state...
       st.session_state['total_calories'] += int(new_cals)
       st.success(f"Successfully logged {food_input} ({int(new_cals)}kcal)")
       st.write(f"Added {int(new_cals)} calories to your daily total.") # Adds a nice visual line to separate the search from the summary
       st.rerun()
     except Exception as e:
       st.error(f"Logic error:{e}")
  elif data==[]:
       st.warning(f"Sorry, we couldn't find that food item '{food_input}'. Try 'pizza' or '1 apple' for better results.")  
  else:  
    st.error("Please type a valid food item.")
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
st.session_state['total_calories']=int(total_cals)
manual_cals = int(total_cals)
grand_total=st.session_state['total_calories']+manual_cals
st.metric("Total Calories", f"{int(grand_total)} / {int(tdee)} kcal")