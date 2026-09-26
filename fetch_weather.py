import requests
import psycopg2

# 1. Fetch live weather data for London from Open-Meteo API
url = "https://api.open-meteo.com/v1/forecast?latitude=51.5074&longitude=-0.1278&current_weather=true"
response = requests.get(url).json()

current_temp = response["current_weather"]["temperature"]
wind_speed = response["current_weather"]["windspeed"]

# 2. Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="weather_db",
    user="postgres",
    password="Pooja2002",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# 3. Insert record into PostgreSQL
query = """
INSERT INTO weather_metrics (city, temperature_c, windspeed_kmh) 
VALUES (%s, %s, %s);
"""
cursor.execute(query, ("London", current_temp, wind_speed))

conn.commit()
cursor.close()
conn.close()

print(f"✅ Successfully inserted: London | {current_temp}°C | {wind_speed} km/h")
