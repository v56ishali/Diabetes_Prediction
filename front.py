# -*- coding: utf-8 -*-
"""front.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zazD1RCN1d8gAoaih0P4Vr0BGmhiXZvK
"""

# Commented out IPython magic to ensure Python compatibility.
# %pip install streamlit

import streamlit as st
import numpy as np
import pickle

# Title
st.title("🩺 Diabetes Prediction App")

# Load the trained model
with open("lr.pkl", "rb") as f:
    model = pickle.load(f)

# Input form
st.header("Enter Patient Information")

insu = st.number_input("Insulin Level", min_value=0)
mass = st.number_input("BMI (Mass)", min_value=0.0)
age = st.number_input("Age", min_value=0)
pres = st.number_input("Blood Pressure", min_value=0)

# Prediction
if st.button("Predict Diabetes Status"):
    input_data = np.array([[insu, mass, age, pres]])
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠ The model predicts: Diabetes Positive")
    else:
        st.success("✅ The model predicts: Diabetes Negative")
