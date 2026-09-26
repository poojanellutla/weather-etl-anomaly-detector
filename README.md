# Real-Time Weather Data Pipeline & Anomaly Detection

An automated ETL (Extract, Transform, Load) pipeline built with Python and PostgreSQL that ingests live weather data, stores historic metrics, and detects temperature anomalies using statistical thresholds (Z-Score).

## 📌 Features
- **Data Ingestion**: Fetches live weather metrics (temperature, windspeed) via Open-Meteo REST API.
- **Relational Storage**: Persists continuous records into a PostgreSQL database.
- **Anomaly Detection**: Uses Pandas to calculate statistical metrics (Mean, Standard Deviation, Z-Score) and flags extreme environmental conditions.

## 🛠️ Tech Stack
- **Language**: Python 3.13
- **Database**: PostgreSQL / pgAdmin 4
- **Libraries**: `requests`, `pandas`, `psycopg2-binary`, `sqlalchemy`

## 🚀 How to Run
1. Run the ingestion script:
   ```bash
   python fetch_weather.py
