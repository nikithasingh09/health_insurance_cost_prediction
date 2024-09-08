import streamlit as st

# Set the title of the app
st.title("Insurance Information Form")

# Ask for age
age = st.number_input("Age", min_value=0, max_value=120, step=1, format="%d")

# Ask for BMI
bmi = st.number_input("BMI", min_value=0.0, max_value=50.0, step=0.1, format="%.1f")

# Ask for gender
gender = st.selectbox("Gender", ["Male", "Female", "Other"])

# Ask for number of children
children = st.number_input("Number of Children", min_value=0, max_value=10, step=1, format="%d")

# Ask for smoking status
smoker = st.selectbox("Smoker", ["Yes", "No"])

# Ask for region
region = st.selectbox("Region", ["Northeast", "Southeast", "Southwest", "Northwest"])

# Display the input data
st.write("## Input Data")
st.write(f"**Age:** {age}")
st.write(f"**BMI:** {bmi}")
st.write(f"**Gender:** {gender}")
st.write(f"**Number of Children:** {children}")
st.write(f"**Smoker:** {smoker}")
st.write(f"**Region:** {region}")
