import streamlit as st
import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="EV Charging Optimization",
    page_icon="⚡",
    layout="wide"
)

# -----------------------------
# Load Model & Data
# -----------------------------
model = joblib.load('model.pkl')
data = pd.read_csv('data/charging_data.csv')

# -----------------------------
# Sidebar Inputs
# -----------------------------
st.sidebar.title("🔧 Battery Parameters")

soc = st.sidebar.slider("Current SOC (%)", 0, 100, 40)
temperature = st.sidebar.slider("Battery Temperature (°C)", 20, 60, 35)

optimize_btn = st.sidebar.button("⚡ Optimize Charging")

# -----------------------------
# Main Title
# -----------------------------
st.title("⚡ EV Charging Optimization using AI")
st.markdown(
    """
This application uses **Machine Learning** to recommend an **optimal EV charging strategy**
that maximizes efficiency and reduces battery stress.
"""
)

# -----------------------------
# Optimization Logic
# -----------------------------
def recommend_optimal_charging(soc, temp):
    best_eff = 0
    best_plan = None

    for current in [20, 30, 40, 50]:
        for time in [30, 45, 60]:
            eff = model.predict([[soc, temp, current, time]])[0]
            if eff > best_eff:
                best_eff = eff
                best_plan = (current, time, eff)

    return best_plan

# -----------------------------
# Result Section
# -----------------------------
st.subheader("🔋 Optimal Charging Recommendation")

if optimize_btn:
    current, time, efficiency = recommend_optimal_charging(soc, temperature)

    st.success("✅ Optimal Charging Strategy Found")
    st.write(f"**Charging Current:** {current} A")
    st.write(f"**Charging Time:** {time} minutes")
    st.write(f"**Expected Efficiency:** {efficiency:.2f} %")
else:
    st.info("ℹ️ Adjust values in the sidebar and click **Optimize Charging**")

# -----------------------------
# Visualization Section
# -----------------------------
st.subheader("📊 Charging Data Insights")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Efficiency vs Charging Current**")
    fig1, ax1 = plt.subplots()
    ax1.scatter(data['Charging_Current'], data['Efficiency'])
    ax1.set_xlabel("Charging Current (A)")
    ax1.set_ylabel("Efficiency (%)")
    ax1.grid(True)
    st.pyplot(fig1)

with col2:
    st.markdown("**Efficiency vs SOC**")
    fig2, ax2 = plt.subplots()
    ax2.scatter(data['SOC'], data['Efficiency'])
    ax2.set_xlabel("SOC (%)")
    ax2.set_ylabel("Efficiency (%)")
    ax2.grid(True)
    st.pyplot(fig2)

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.markdown(
    """
**Developed by Aftab Ahmed**  
AI for EV Energy Optimization  

🔹 *Future Scope*: Reinforcement Learning-based charging control, real-time EV integration
"""
)
