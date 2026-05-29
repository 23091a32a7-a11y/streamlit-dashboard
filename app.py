import streamlit as st
import requests

st.set_page_config(page_title="Real-Time Dashboard", layout="wide")

st.title("🌐 Real-Time Data Dashboard")

# ---------------------------
# 1. HYDERABAD WEATHER
# ---------------------------
st.header("🌤 Hyderabad Weather")

weather_url = "https://api.open-meteo.com/v1/forecast?latitude=17.3850&longitude=78.4867&current_weather=true"

weather_res = requests.get(weather_url).json()

if "current_weather" in weather_res:
    temp = weather_res["current_weather"]["temperature"]
    wind = weather_res["current_weather"]["windspeed"]

    st.metric("Temperature (°C)", temp)
    st.metric("Wind Speed", wind)
else:
    st.error("Weather data not available")


# ---------------------------
# 2. BITCOIN PRICE
# ---------------------------
st.header("₿ Bitcoin Price")

btc_url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

btc_res = requests.get(btc_url).json()

st.metric("BTC/USDT Price", btc_res["price"])


# ---------------------------
# 3. RANDOM USER
# ---------------------------
st.header("👤 Random User")

user_url = "https://randomuser.me/api/"

user_res = requests.get(user_url).json()["results"][0]

col1, col2 = st.columns(2)

with col1:
    st.image(user_res["picture"]["large"])

with col2:
    st.write("**Name:**", user_res["name"]["first"], user_res["name"]["last"])
    st.write("**Email:**", user_res["email"])
    st.write("**Country:**", user_res["location"]["country"])