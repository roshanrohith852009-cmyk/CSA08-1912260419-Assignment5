
import csv
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
TEST_DIR = BASE_DIR / "data" / "adversarial"
TEST_DIR.mkdir(parents=True, exist_ok=True)

print("B2 - ADVERSARIAL DATA TESTING")
print("=" * 45)


# Test 1: Wrong delimiter
print("\nTEST 1: Wrong CSV delimiter")

wrong_file = TEST_DIR / "wrong_delimiter.csv"

with open(wrong_file, "w", newline="") as file:
    file.write(
        "station_id;timestamp;pm25;pm10\n"
        "ST001;2026-11-01 08:00;45;80\n"
    )

try:
    with open(wrong_file, newline="") as file:
        reader = csv.DictReader(file)
        first_row = next(reader)

        if "station_id" not in first_row:
            print("PASS: Wrong delimiter detected.")
        else:
            print("Unexpected format.")
except (StopIteration, csv.Error) as error:
    print("PASS: Invalid CSV handled:", error)


# Test 2: Empty CSV
print("\nTEST 2: Empty CSV file")

empty_file = TEST_DIR / "empty.csv"
empty_file.write_text("", encoding="utf-8")

try:
    with open(empty_file, newline="") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames is None:
            print("PASS: Empty file detected safely.")
except csv.Error as error:
    print("PASS: Empty CSV handled:", error)


# Test 3: Invalid numeric values
print("\nTEST 3: Invalid numeric values")

invalid_file = TEST_DIR / "invalid_values.csv"

with open(invalid_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["station_id", "pm25"])
    writer.writerow(["ST001", "not-a-number"])
    writer.writerow(["ST002", "-500"])
    writer.writerow(["ST003", "45"])

with open(invalid_file, newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        try:
            value = float(row["pm25"])

            if value < 0:
                print(row["station_id"], "- PASS: Negative value rejected.")
            else:
                print(row["station_id"], "- Valid value:", value)

        except ValueError:
            print(row["station_id"], "- PASS: Invalid number rejected.")


# Test 4: SQL injection-style text
print("\nTEST 4: SQL injection-style input")

database = TEST_DIR / "security_test.db"

connection = sqlite3.connect(database)
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS complaints (
        id INTEGER PRIMARY KEY,
        complaint TEXT
    )
""")

malicious_input = "'; DROP TABLE complaints; --"

# Parameterised query treats input as data
cursor.execute(
    "INSERT INTO complaints (complaint) VALUES (?)",
    (malicious_input,)
)

cursor.execute("SELECT complaint FROM complaints")
result = cursor.fetchone()

cursor.execute("""
    SELECT name FROM sqlite_master
    WHERE type='table' AND name='complaints'
""")

table_exists = cursor.fetchone() is not None

if table_exists and result[0] == malicious_input:
    print("PASS: SQL injection-style text stored safely as data.")
else:
    print("FAIL: Database safety test failed.")

connection.close()


# Final summary
print("\n" + "=" * 45)
print("B2 ADVERSARIAL TESTING COMPLETED")
print("Test files saved in:", TEST_DIR)
