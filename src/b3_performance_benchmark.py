
import time
import sqlite3
import pandas as pd
import random
import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

RESULT_FILE = OUTPUT_DIR / "b3_benchmark_results.csv"
DATABASE = OUTPUT_DIR / "b3_benchmark.db"

print("B3 - PERFORMANCE BENCHMARKING")
print("=" * 55)

# Dataset sizes
DATASET_SIZES = [1000, 10000, 100000]

results = []

for size in DATASET_SIZES:

    print(f"\nTesting dataset size: {size:,}")

    random.seed(42)

    data = [
        {
            "station_id": f"ST{random.randint(1, 100):03}",
            "pm25": random.uniform(5, 150),
            "pm10": random.uniform(10, 250)
        }
        for _ in range(size)
    ]

    # Method 1: Plain Python loops
    start = time.perf_counter()

    total = 0
    for row in data:
        total += row["pm25"]

    python_average = total / len(data)

    python_time = time.perf_counter() - start

    # Method 2: Pandas
    start = time.perf_counter()

    df = pd.DataFrame(data)
    pandas_average = df["pm25"].mean()

    pandas_time = time.perf_counter() - start

    # Method 3: SQLite
    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS benchmark")
    cursor.execute("""
        CREATE TABLE benchmark (
            station_id TEXT,
            pm25 REAL,
            pm10 REAL
        )
    """)

    start = time.perf_counter()

    cursor.executemany(
        "INSERT INTO benchmark VALUES (?, ?, ?)",
        [
            (row["station_id"], row["pm25"], row["pm10"])
            for row in data
        ]
    )

    cursor.execute("SELECT AVG(pm25) FROM benchmark")
    sql_average = cursor.fetchone()[0]

    sql_time = time.perf_counter() - start

    connection.close()

    # Save benchmark results
    results.append({
        "dataset_size": size,
        "python_loop_seconds": python_time,
        "pandas_seconds": pandas_time,
        "sql_seconds": sql_time,
        "python_average": python_average,
        "pandas_average": pandas_average,
        "sql_average": sql_average
    })

    print(f"Python loop: {python_time:.6f} seconds")
    print(f"Pandas:      {pandas_time:.6f} seconds")
    print(f"SQLite:      {sql_time:.6f} seconds")

# Save results
result_df = pd.DataFrame(results)
result_df.to_csv(RESULT_FILE, index=False)

print("\nBENCHMARK SUMMARY")
print(result_df.to_string(index=False))

print("\nResults saved to:", RESULT_FILE)
print("B3 PERFORMANCE BENCHMARKING COMPLETED!")
