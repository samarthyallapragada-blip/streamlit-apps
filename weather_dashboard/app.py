import streamlit as st
import requests

st.title("🌤️ Skyline Weather")
st.caption("Live weather using Open-Meteo API")

city = st.text_input("Enter city:", "London")

geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
geo = requests.get(geo_url).json()

if "results" in geo:
    lat = geo["results"][0]["latitude"]
    lon = geo["results"][0]["longitude"]
    name = geo["results"][0]["name"]

    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
    data = requests.get(weather_url).json()["current"]

    st.subheader(f"Weather in {name}")
    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature", f"{data['temperature_2m']}°C")
    col2.metric("Humidity", f"{data['relative_humidity_2m']}%")
    col3.metric("Wind Speed", f"{data['wind_speed_10m']} km/h")
else:
    st.error("City not found")
