import streamlit as st
import joblib
import numpy as np

model = joblib.load("ml_streamlit_app/beneish_model.pkl")

st.title("Earnings Manipulation Detection System")

st.write("Enter Beneish M-Score Financial Ratios")

DSRI = st.number_input("DSRI – Days Sales in Receivables Index")
GMI  = st.number_input("GMI – Gross Margin Index")
AQI  = st.number_input("AQI – Asset Quality Index")
SGI  = st.number_input("SGI – Sales Growth Index")
DEPI = st.number_input("DEPI – Depreciation Index")
SGAI = st.number_input("SGAI – SG&A Index")
LVGI = st.number_input("LVGI – Leverage Index")
TATA = st.number_input("TATA – Total Accruals to Total Assets")

if st.button("Check Risk"):
    data = np.array([[DSRI,GMI,AQI,SGI,DEPI,SGAI,LVGI,TATA]])
    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("⚠ High Risk of Earnings Manipulation Detected")
    else:
        st.success("✅ Low Risk of Earnings Manipulation")
