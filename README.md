# ⚡ EV Charging Optimization using AI

## 📌 Overview

This project presents an **AI-based decision-making system** for optimizing **Electric Vehicle (EV) charging**. Instead of only predicting outcomes, the system **evaluates multiple charging strategies** and **recommends the optimal charging current and time** that maximize charging efficiency while reducing battery stress.

The solution is deployed as an **interactive Streamlit application**, demonstrating an end-to-end ML workflow from data modeling to real-time recommendations.

---

## 🎯 Problem Statement

Unoptimized EV charging (e.g., aggressive fast charging at high temperatures) can cause:

* Accelerated battery degradation
* Reduced charging efficiency
* Increased thermal stress and safety risks

The objective of this project is to design an **intelligent charging optimization approach** that balances charging speed and battery health using machine learning.

---

## 🧠 Methodology

1. **Data Preparation**: Created a realistic charging dataset representing different SOC, temperature, current, and charging-time scenarios.
2. **Modeling**: Trained a **Random Forest Regressor** to learn the non-linear relationship between charging parameters and efficiency.
3. **Optimization Logic**: For a given SOC and temperature, the system evaluates multiple candidate charging strategies and selects the one with the **highest predicted efficiency**.
4. **Deployment**: Integrated the trained model into a **Streamlit dashboard** for interactive use.

---

## 📊 Dataset Description

**Input Features**

* State of Charge (SOC %)
* Battery Temperature (°C)
* Charging Current (A)
* Charging Time (minutes)

**Target Variable**

* Charging Efficiency (%)

> 📌 *Note*: Due to limited availability of public real-world charging optimization datasets, a **synthetic but realistic dataset** was generated based on EV battery behavior reported in literature. This approach is commonly used in academic prototypes.

---

## 🤖 Machine Learning Model

* **Algorithm**: Random Forest Regressor
* **Rationale**:

  * Captures non-linear battery behavior
  * Robust to noise and small datasets
  * Provides stable performance without heavy tuning

The trained model is serialized using **joblib** and reused during deployment to ensure fast and consistent inference.

---

## ⚡ Optimization Strategy

For a given battery state:

* Multiple charging currents and durations are simulated
* Each scenario is evaluated using the trained ML model
* The strategy with the **maximum predicted efficiency** is recommended

This mimics the behavior of an **intelligent EV charging controller** in real-world systems.

---

## 🖥️ Deployment (Streamlit)

The application is deployed using **Streamlit**, providing:

* Sidebar-based user inputs (SOC, temperature)
* Real-time optimal charging recommendations
* Interactive visualizations for data insight

### ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 📈 Visualizations

* **Efficiency vs Charging Current**
* **Efficiency vs SOC**

These plots help analyze how charging parameters influence efficiency and support model interpretability.

---

## 🚀 Future Scope

* Reinforcement Learning–based adaptive charging control
* SOH-aware charging optimization
* Integration with real-time EV Battery Management Systems (BMS)

---

## 👤 Author

**Aftab Ahmed**
AI & Machine Learning | EV Energy Optimization

---

## ⭐ Key Takeaway

This project demonstrates how **AI can be applied to intelligent energy optimization in EVs**, combining **machine learning, optimization logic, visualization, and deployment** into a single end-to-end system.
