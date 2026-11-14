
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_FILE = BASE_DIR / "data" / "raw" / "air_quality_raw.csv"
CLEAN_FILE = BASE_DIR / "data" / "cleaned" / "air_quality_cleaned.csv"
DB_FILE = BASE_DIR / "outputs" / "air_quality.db"
CHART_DIR = BASE_DIR / "outputs" / "charts"

CHART_DIR.mkdir(parents=True, exist_ok=True)
CLEAN_FILE.parent.mkdir(parents=True, exist_ok=True)

print("B1 - AIR QUALITY CLEANING PIPELINE")
print("-" * 45)

# 1. Load raw dataset
df = pd.read_csv(RAW_FILE)
print("Raw records:", len(df))

# 2. Remove duplicate records
df = df.drop_duplicates(subset=["station_id", "timestamp"])

# 3. Convert columns to numeric
numeric_columns = [
    "pm25", "pm10", "temperature", "humidity", "aqi"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# 4. Replace impossible values with missing values
df.loc[df["pm25"] < 0, "pm25"] = None
df.loc[df["pm10"] < 0, "pm10"] = None
df.loc[~df["humidity"].between(0, 100), "humidity"] = None
df.loc[~df["aqi"].between(0, 500), "aqi"] = None

# Convert Fahrenheit temperatures to Celsius
fahrenheit_rows = df["temperature"] > 60
df.loc[fahrenheit_rows, "temperature"] = (
    df.loc[fahrenheit_rows, "temperature"] - 32
) * 5 / 9

# Flag unrealistic temperature readings
df.loc[
    ~df["temperature"].between(-50, 60),
    "temperature"
] = None

# 5. Fill missing values using column medians
for column in numeric_columns:
    median_value = df[column].median()
    if pd.notna(median_value):
        df[column] = df[column].fillna(median_value)

# Remove records that still have missing values
df = df.dropna(subset=numeric_columns)

# 6. Min-Max normalisation
for column in ["pm25", "pm10", "temperature", "humidity"]:
    minimum = df[column].min()
    maximum = df[column].max()

    if maximum != minimum:
        df[column + "_normalised"] = (
            (df[column] - minimum) / (maximum - minimum)
        )
    else:
        df[column + "_normalised"] = 0.0

# 7. Z-score normalisation
for column in ["pm25", "pm10"]:
    standard_deviation = df[column].std()

    if standard_deviation != 0 and pd.notna(standard_deviation):
        df[column + "_zscore"] = (
            df[column] - df[column].mean()
        ) / standard_deviation
    else:
        df[column + "_zscore"] = 0.0

# 8. Save cleaned CSV
df.to_csv(CLEAN_FILE, index=False)

# 9. Store cleaned data in SQLite
connection = sqlite3.connect(DB_FILE)

df.to_sql(
    "air_quality",
    connection,
    if_exists="replace",
    index=False
)

connection.close()

# 10. Generate PM2.5 chart
plt.figure(figsize=(10, 5))
plt.bar(df["station_id"], df["pm25"])
plt.title("PM2.5 Levels by Monitoring Station")
plt.xlabel("Station ID")
plt.ylabel("PM2.5")
plt.tight_layout()
plt.savefig(CHART_DIR / "pm25_by_station.png")
plt.close()

# 11. Generate AQI chart
plt.figure(figsize=(10, 5))
plt.plot(df["station_id"], df["aqi"], marker="o")
plt.title("Air Quality Index by Monitoring Station")
plt.xlabel("Station ID")
plt.ylabel("AQI")
plt.tight_layout()
plt.savefig(CHART_DIR / "aqi_by_station.png")
plt.close()

# 12. Daily summary
df["timestamp"] = pd.to_datetime(df["timestamp"])

summary = df.groupby(
    df["timestamp"].dt.date
).agg(
    average_pm25=("pm25", "mean"),
    average_pm10=("pm10", "mean"),
    average_aqi=("aqi", "mean")
)

print("\nDaily Summary:")
print(summary)

print("\nCleaned records:", len(df))
print("Cleaned CSV:", CLEAN_FILE)
print("SQLite database:", DB_FILE)
print("Charts saved in:", CHART_DIR)

print("\nB1 CLEANING PIPELINE COMPLETED SUCCESSFULLY!")
