import pandas as pd
import psycopg2

# 1. Connect to PostgreSQL and fetch stored data
conn = psycopg2.connect(
    dbname="weather_db",
    user="postgres",
    password="Pooja2002",
    host="localhost",
    port="5432"
)

query = "SELECT timestamp, city, temperature_c, windspeed_kmh FROM weather_metrics ORDER BY timestamp ASC;"
df = pd.read_sql(query, conn)
conn.close()

# 2. Check if we have enough data points
if len(df) < 3:
    print("⚠️ Need at least 3 records to run anomaly detection. Run fetch_weather.py a few more times!")
else:
    # Convert numeric columns to float
    df['temperature_c'] = df['temperature_c'].astype(float)
    
    # Calculate statistical metrics (Mean and Standard Deviation)
    mean_temp = df['temperature_c'].mean()
    std_temp = df['temperature_c'].std()
    
    # Avoid division by zero if std is 0
    if std_temp == 0:
        std_temp = 0.001

    # Calculate Z-score for temperature anomaly detection
    df['z_score'] = (df['temperature_c'] - mean_temp) / std_temp
    
    # Flag values as anomalies if Z-score > 2 or < -2 (or static rule > 35°C / < -5°C)
    df['is_anomaly'] = df['temperature_c'].apply(lambda x: True if x > 35 or x < -5 else False)

    print("\n--- WEATHER DATA ANALYSIS ---")
    print(df[['timestamp', 'city', 'temperature_c', 'z_score', 'is_anomaly']])

    # 3. Alert Trigger
    anomalies = df[df['is_anomaly'] == True]
    if not anomalies.empty:
        print("\n🚨 ANOMALY DETECTED! Extreme temperature recorded:")
        print(anomalies[['timestamp', 'city', 'temperature_c']])
    else:
        print("\n✅ All temperature readings are within normal statistical ranges.")