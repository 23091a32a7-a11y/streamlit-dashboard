import streamlit as st
import requests
import pandas as pd
import time

st.set_page_config(page_title="Smart Real-Time Dashboard", layout="wide")

st.title("🌐 Smart Real-Time Dashboard")

# ---------------------------
# SIDEBAR
# ---------------------------
st.sidebar.header("⚙️ Controls")

city = st.sidebar.selectbox("Choose City", ["Hyderabad", "Delhi", "Mumbai"])

refresh = st.sidebar.button("🔄 Refresh Now")

# city coordinates
coords = {
    "Hyderabad": (17.3850, 78.4867),
    "Delhi": (28.6139, 77.2090),
    "Mumbai": (19.0760, 72.8777)
}

lat, lon = coords[city]

# ---------------------------
# WEATHER API
# ---------------------------
st.header(f"🌤 Weather - {city}")

weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

weather_res = requests.get(weather_url).json()

temp = weather_res["current_weather"]["temperature"]
wind = weather_res["current_weather"]["windspeed"]

col1, col2 = st.columns(2)
col1.metric("Temperature (°C)", temp)
col2.metric("Wind Speed", wind)

# ---------------------------
# BITCOIN PRICE
# ---------------------------
st.header("₿ Bitcoin Live Price")

btc_url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
btc_res = requests.get(btc_url).json()

price = float(btc_res["price"])
st.metric("BTC/USDT", price)

# ---------------------------
# SIMPLE CHART (FAKE TREND)
# ---------------------------
st.header("📊 Price Trend (Demo)")

data = pd.DataFrame({
    "time": list(range(10)),
    "price": [price + i * 10 for i in range(10)]
})

st.line_chart(data.set_index("time"))

# ---------------------------
# AUTO REFRESH
# ---------------------------
st.caption("Auto-refresh every 10 seconds")

time.sleep(10)
st.rerun()