\# A2 – Data Cleaning and Normalisation



\## 1. Introduction



Data cleaning is the process of identifying and correcting inaccurate, incomplete and inconsistent data. Normalisation transforms numerical values into a common scale for easier comparison and analysis.



In the City Air-Quality Monitoring Network, raw sensor data may contain missing values, duplicate readings, invalid measurements and inconsistent temperature units.



\## 2. Data Cleaning Techniques



The following techniques are proposed:



\### A. Handling Missing Values



\- Check every column for missing values.

\- For missing PM2.5 and PM10 readings, use the median of valid readings from the same station when sufficient data is available.

\- For missing temperature and humidity, use the station's median value.

\- If a reliable replacement cannot be calculated, mark the reading as unavailable rather than inventing a value.



\### B. Handling Invalid Values



\- Reject negative PM2.5 and PM10 concentrations.

\- Check humidity values are between 0 and 100%.

\- Check temperature readings against a documented valid range.

\- Flag AQI values that fall outside the selected AQI standard.

\- Correct invalid records only when the original value can be verified.



\### C. Removing Duplicate Records



A duplicate is identified using the station ID and timestamp.



Only one valid record should be retained for each station and timestamp combination. Conflicting duplicate measurements should be flagged for review.



\## 3. Temperature Unit Conversion



Some sensors may report temperature in Fahrenheit instead of Celsius.



The conversion formula is:



Celsius = (Fahrenheit - 32) × 5/9



Example:



If the temperature is 86°F:



Celsius = (86 - 32) × 5/9



Celsius = 30°C



All valid temperature readings will be converted into Celsius before storage and analysis.



The original unit should be identified from sensor metadata or source documentation. It should not be guessed from the temperature value alone.



\## 4. Min-Max Normalisation



Min-Max normalisation scales values into a range between 0 and 1.



Formula:



X\_normalised = (X - X\_min) / (X\_max - X\_min)



Where:



\- X = Original value

\- X\_min = Minimum value

\- X\_max = Maximum value



Example:



If the minimum PM2.5 value is 10 and the maximum is 110, for an observed value of 60:



X\_normalised = (60 - 10) / (110 - 10)



X\_normalised = 0.5



\### Advantages



\- Converts values into a common scale.

\- Easy to understand and interpret.

\- Useful for comparing different numerical features.



\### Limitation



Extreme values can strongly affect the minimum and maximum values.



\## 5. Z-Score Normalisation



Z-score normalisation standardises values using the mean and standard deviation.



Formula:



Z = (X - Mean) / Standard Deviation



Where:



\- X = Original value

\- Mean = Average of the feature

\- Standard Deviation = Measure of data spread



Example:



If a reading is 60, the mean is 50 and the standard deviation is 10:



Z = (60 - 50) / 10



Z = 1



\### Advantages



\- Shows how far a value is from the average.

\- Useful for identifying unusually high or low measurements.

\- Less dependent on fixed minimum and maximum limits.



\### Limitation



The resulting values are not restricted to the range 0 to 1.



If standard deviation is zero, the feature contains no variation and must be handled separately.



\## 6. Data Cleaning Pseudocode



```text

BEGIN



&#x20;   LOAD raw air-quality dataset



&#x20;   CHECK missing values



&#x20;   FOR each record



&#x20;       IF PM2.5 or PM10 is negative

&#x20;           FLAG record as invalid

&#x20;       END IF



&#x20;       IF humidity is outside 0 to 100

&#x20;           FLAG record as invalid

&#x20;       END IF



&#x20;       IF temperature unit is Fahrenheit

&#x20;           CONVERT temperature to Celsius

&#x20;       END IF



&#x20;       CHECK duplicate station ID and timestamp



&#x20;       HANDLE missing values using valid station data



&#x20;   END FOR



&#x20;   REMOVE or quarantine invalid records



&#x20;   APPLY Min-Max normalisation



&#x20;   APPLY Z-score normalisation



&#x20;   SAVE cleaned dataset



END

```



\## 7. Comparison of Normalisation Methods



| Feature | Min-Max | Z-Score |

|---|---|---|

| Output range | Usually 0 to 1 | No fixed range |

| Uses | Minimum and maximum | Mean and standard deviation |

| Extreme values | Highly affected | Also affected |

| Main purpose | Scale data | Standardise data |

| Interpretation | Relative position in range | Distance from mean |



\## 8. Conclusion



Data cleaning improves the reliability of air-quality information by handling missing values, invalid readings, duplicate records and inconsistent temperature units. Min-Max and Z-score normalisation help prepare numerical data for comparison and analysis. These techniques make the dataset more suitable for database storage, visualisation and further analysis.

