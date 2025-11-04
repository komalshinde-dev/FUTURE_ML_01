# -------------------------------------------
# FUTURE INTERNS – MACHINE LEARNING TASK 1
# AI-POWERED SALES FORECASTING DASHBOARD
# -------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet
import urllib.request
import os

# ----------------------------
# STEP 1: Load or download dataset
# ----------------------------
file_path = "sales.csv"
if not os.path.exists(file_path):
    print("🔽 Downloading sample dataset...")
    url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv"
    urllib.request.urlretrieve(url, file_path)
    print("✅ Dataset downloaded successfully as 'sales.csv'")

# Load dataset
data = pd.read_csv(file_path)
print("\n📊 Data Preview:")
print(data.head())

# Rename columns for Prophet compatibility
data.columns = ['Month', 'Sales']
data['Month'] = pd.to_datetime(data['Month'])
df = data.rename(columns={'Month': 'ds', 'Sales': 'y'})

# ----------------------------
# STEP 2: Build and train Prophet model
# ----------------------------
print("\n⚙️ Training Prophet model...")
model = Prophet()
model.fit(df)

# ----------------------------
# STEP 3: Make future predictions
# ----------------------------
future = model.make_future_dataframe(periods=12, freq='M')  # forecast 12 months ahead
forecast = model.predict(future)

# ----------------------------
# STEP 4: Visualize the forecast
# ----------------------------
print("\n📈 Generating forecast plot...")
fig1 = model.plot(forecast)
plt.title("AI-Powered Sales Forecast")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# Optional: Show trend and seasonality plots
model.plot_components(forecast)
plt.show()

# ----------------------------
# STEP 5: Save forecast results
# ----------------------------
output_file = "forecast_results.csv"
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv(output_file, index=False)
print(f"\n✅ Forecast results saved to '{output_file}'")

# ----------------------------
# STEP 6: Print key predictions
# ----------------------------
print("\n🔮 Next 5 predicted months:")
print(forecast[['ds', 'yhat']].tail(5))
