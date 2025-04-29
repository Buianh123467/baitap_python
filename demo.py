import requests
import pandas as pd

# 1. Lấy dữ liệu từ API
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 52.52,
    "longitude": 13.41,
    "past_days": 10,
    "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m"
}

response = requests.get(url, params=params)
data = response.json()

# 2. Tạo DataFrame từ dữ liệu
latitude = data["latitude"]
longitude = data["longitude"]
hourly = data["hourly"]

df = pd.DataFrame({
    "time": hourly["time"],
    "temperature_2m": hourly["temperature_2m"],
    "relative_humidity_2m": hourly["relative_humidity_2m"],
    "wind_speed_10m": hourly["wind_speed_10m"]
})

df["latitude"] = latitude
df["longitude"] = longitude
df = df[["latitude", "longitude", "time", "temperature_2m", "relative_humidity_2m", "wind_speed_10m"]]

# 3. Lưu ra file CSV
df.to_csv("weather_data.csv", index=False)
print("✅ File đã lưu: weather_data.csv")

# 4. Tính tổng các giá trị đến ngày 29-04
df["time"] = pd.to_datetime(df["time"])
df_filtered = df[df["time"] < "2025-04-30"]

print("Tổng temperature_2m:", df_filtered["temperature_2m"].sum())
print("Tổng relative_humidity_2m:", df_filtered["relative_humidity_2m"].sum())
print("Tổng wind_speed_10m:", df_filtered["wind_speed_10m"].sum())
