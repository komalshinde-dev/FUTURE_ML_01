# 📈 FUTURE INTERNS – MACHINE LEARNING TASK 1  
## 💡 AI-Powered Sales Forecasting Dashboard

### 🎯 Project Objective
Develop an **AI-powered dashboard** that predicts future sales trends using historical retail data.  
This helps businesses forecast demand, identify growth patterns, and make data-driven decisions.

---

## 📦 Dataset

**Source:** [Airline Passengers Dataset (Monthly Sales Example)](https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv)

- Contains monthly passenger (sales) data from 1949-1960.  
- Columns: `Month`, `Sales`  
- Used as a stand-in for a retail sales dataset.  

File used in project: `sales.csv`  
If not found, the script automatically downloads it.

---

## ⚙️ Tech Stack

| Category | Tools / Libraries |
|-----------|-------------------|
| Language | Python 3 |
| Libraries | pandas, numpy, matplotlib, prophet |
| Dashboard Framework | Streamlit (optional) |
| Environment | VS Code / Google Colab / Jupyter Notebook |

---

## 🧠 Skills Gained
- Time-series forecasting  
- Regression & trend analysis  
- Prophet model training and tuning  
- Data cleaning & visualization  
- Dashboard building with Streamlit  

---

## 🧩 Project Workflow

1. **Data Collection**  
   - Loads or downloads sales dataset automatically.  

2. **Preprocessing**  
   - Renames columns for Prophet format (`ds`, `y`).  
   - Converts date columns to datetime objects.  

3. **Model Training**  
   - Trains a `Prophet` forecasting model on sales data.  

4. **Forecast Generation**  
   - Predicts sales for the next 12 months.  

5. **Visualization**  
   - Plots trends, seasonality, and forecasted sales using Matplotlib.  

6. **Output Storage**  
   - Saves forecast results to `forecast_results.csv`.

---

## 🚀 How to Run This Project

### 🔹 Step 1 – Install Dependencies
```bash
pip install pandas numpy matplotlib prophet
