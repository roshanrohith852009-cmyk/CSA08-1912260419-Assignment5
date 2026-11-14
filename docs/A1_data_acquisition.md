\# A1 – Data Acquisition



\## 1. Introduction



The City Air-Quality Monitoring Network collects air-quality information from multiple monitoring stations. The collected data includes station ID, date, time, PM2.5, PM10, temperature, humidity and AQI.



The purpose of data acquisition is to collect raw information from CSV files, inspect its structure and identify possible data-quality problems before processing.



\## 2. CSV File Structure



The system uses CSV (Comma-Separated Values) files to store the raw air-quality readings.



\### Expected columns



| Column | Description | Data Type |

|---|---|---|

| station\_id | Unique monitoring station ID | Text |

| timestamp | Date and time of reading | DateTime |

| pm25 | PM2.5 concentration | Float |

| pm10 | PM10 concentration | Float |

| temperature | Temperature reading | Float |

| humidity | Relative humidity | Float |

| aqi | Air Quality Index | Integer |



\### Possible Data Errors



1\. Missing values in PM2.5 or PM10 readings.

2\. Negative pollutant concentrations.

3\. Incorrect temperature units such as Fahrenheit instead of Celsius.

4\. Duplicate station readings.

5\. Invalid date and time formats.

6\. AQI values outside the expected range.

7\. Incorrect or missing station IDs.



\## 3. Data Acquisition Pseudocode



```text

BEGIN



&#x20;   DEFINE input CSV file path



&#x20;   CHECK whether the CSV file exists



&#x20;   IF file does not exist

&#x20;       DISPLAY error message

&#x20;       STOP

&#x20;   END IF



&#x20;   OPEN CSV file



&#x20;   READ column headers



&#x20;   VALIDATE required columns



&#x20;   READ all records



&#x20;   COUNT total records



&#x20;   DISPLAY first five records



&#x20;   IDENTIFY missing values



&#x20;   IDENTIFY duplicate records



&#x20;   IDENTIFY invalid values



&#x20;   STORE raw data for further processing



END

```



\## 4. SQLite Database Schema



SQLite is selected to store the cleaned air-quality readings.



\### Table: air\_quality



```sql

CREATE TABLE air\_quality (

&#x20;   id INTEGER PRIMARY KEY AUTOINCREMENT,

&#x20;   station\_id TEXT NOT NULL,

&#x20;   timestamp TEXT NOT NULL,

&#x20;   pm25 REAL,

&#x20;   pm10 REAL,

&#x20;   temperature REAL,

&#x20;   humidity REAL,

&#x20;   aqi INTEGER

);

```



\### Database Design Explanation



\- `id` uniquely identifies every database record.

\- `station\_id` identifies the monitoring station.

\- `timestamp` stores the date and time of measurement.

\- `pm25` and `pm10` store particulate matter readings.

\- `temperature` stores temperature in Celsius after cleaning.

\- `humidity` stores relative humidity.

\- `aqi` stores the Air Quality Index.



\## 5. CSV vs SQL Comparison



| Feature | CSV | SQLite |

|---|---|---|

| Storage | Plain text file | Structured database |

| Data searching | Requires file processing | Supports SQL queries |

| Relationships | Not supported directly | Supports relationships |

| Data validation | Limited | Constraints available |

| Large datasets | Less efficient for repeated queries | Better for structured queries |

| Best use | Raw data collection | Cleaned data storage and analysis |



\## 6. Conclusion



CSV files provide a simple method for collecting raw air-quality readings. However, they may contain missing, duplicate and invalid values. SQLite provides structured storage and supports efficient data retrieval. Therefore, the proposed system uses CSV for initial data acquisition and SQLite for storing cleaned data.

