
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE = BASE_DIR / "outputs" / "air_quality.db"

print("B4 - SCALING AND AI APPLICATION")
print("=" * 50)

# 1. Rule-based sentiment analysis

positive_words = [
    "clean", "good", "excellent", "improved",
    "fresh", "better"
]

negative_words = [
    "pollution", "smoke", "dust", "unhealthy",
    "bad", "harmful", "smell", "dirty"
]


def analyse_sentiment(complaint):
    words = complaint.lower().split()

    score = 0

    for word in words:
        word = word.strip(".,!?;:")

        if word in positive_words:
            score += 1
        elif word in negative_words:
            score -= 1

    if score > 0:
        sentiment = "Positive"
    elif score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return score, sentiment


complaints = [
    "The air is clean and fresh today",
    "Smoke and pollution make the air unhealthy",
    "The monitoring station is working today",
    "The air quality is better now",
    "Bad smell and dust are affecting our area"
]

print("\n1. CITIZEN COMPLAINT SENTIMENT ANALYSIS")
print("-" * 50)

for complaint in complaints:
    score, sentiment = analyse_sentiment(complaint)

    print("\nComplaint:", complaint)
    print("Sentiment Score:", score)
    print("Classification:", sentiment)


# 2. SQLite database indexing

print("\n2. DATABASE INDEXING")
print("-" * 50)

connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

# Create an index for faster station searches
cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_station_id
    ON air_quality(station_id)
""")

# Create an index for timestamp searches
cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_timestamp
    ON air_quality(timestamp)
""")

connection.commit()

# Display created indexes
cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type = 'index'
    AND name NOT LIKE 'sqlite_%'
""")

indexes = cursor.fetchall()

print("Database indexes created:")

for index in indexes:
    print("-", index[0])


# 3. Test indexed database query

print("\n3. INDEXED DATABASE QUERY")
print("-" * 50)

cursor.execute("""
    SELECT station_id, AVG(pm25)
    FROM air_quality
    GROUP BY station_id
    ORDER BY station_id
""")

rows = cursor.fetchall()

for row in rows:
    print(
        "Station:", row[0],
        "| Average PM2.5:", round(row[1], 2)
    )

connection.close()


# 4. Scaling recommendation

print("\n4. SCALING RECOMMENDATION")
print("-" * 50)

recommendations = [
    "Use database indexes for faster data retrieval.",
    "Process large datasets in batches.",
    "Use Pandas for data analysis.",
    "Use a central database for multiple stations.",
    "Monitor database performance regularly.",
    "Back up collected air-quality data."
]

for number, recommendation in enumerate(
    recommendations, start=1
):
    print(f"{number}. {recommendation}")


print("\nB4 SCALING AND AI APPLICATION COMPLETED!")
