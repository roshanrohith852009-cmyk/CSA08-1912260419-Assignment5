\# A3 – Data Analysis and Visualisation



\## 1. Introduction



Data analysis helps convert cleaned air-quality readings into meaningful information. Data visualisation presents this information through charts and graphs, making it easier to identify pollution patterns and changes over time.



The City Air-Quality Monitoring Network uses statistical summaries and visualisations to understand air pollution across different monitoring stations.



\## 2. Types of Charts and Their Uses



\### A. Line Chart



Purpose: To display changes in PM2.5 or AQI over time.



\- X-axis: Date and time

\- Y-axis: PM2.5 concentration or AQI

\- Use: Identifies pollution trends and sudden increases.



\### B. Bar Chart



Purpose: To compare pollution levels between monitoring stations.



\- X-axis: Station ID

\- Y-axis: Average PM2.5 concentration

\- Use: Identifies stations with higher average pollution.



\### C. Histogram



Purpose: To understand the distribution of PM2.5 readings.



\- X-axis: PM2.5 concentration ranges

\- Y-axis: Number of observations

\- Use: Shows how frequently different pollution levels occur.



\### D. Scatter Plot



Purpose: To examine the relationship between temperature and PM2.5.



\- X-axis: Temperature in Celsius

\- Y-axis: PM2.5 concentration

\- Use: Helps identify possible relationships between environmental conditions and pollution.



\## 3. Daily Summary Table



The system generates a daily summary for each monitoring station.



| Field | Description |

|---|---|

| Date | Date of observation |

| Station ID | Monitoring station |

| Average PM2.5 | Daily mean PM2.5 |

| Maximum PM2.5 | Highest PM2.5 reading |

| Average PM10 | Daily mean PM10 |

| Average AQI | Daily mean AQI |

| Reading Count | Number of valid readings |



This table helps compare daily pollution levels and identify stations requiring further investigation.



\## 4. Data Analysis Pseudocode



```text

BEGIN



&#x20;   LOAD cleaned air-quality dataset



&#x20;   GROUP records by date and station ID



&#x20;   FOR each group



&#x20;       CALCULATE average PM2.5



&#x20;       CALCULATE maximum PM2.5



&#x20;       CALCULATE average PM10



&#x20;       CALCULATE average AQI



&#x20;       COUNT valid readings



&#x20;   END FOR



&#x20;   DISPLAY daily summary table



&#x20;   CREATE line chart for pollution trends



&#x20;   CREATE bar chart for station comparison



&#x20;   CREATE histogram for PM2.5 distribution



&#x20;   CREATE scatter plot for temperature and PM2.5



&#x20;   SAVE charts as image files



END

```



\## 5. Choosing the Correct Visualisation



| Analysis Question | Recommended Chart | Reason |

|---|---|---|

| How does pollution change over time? | Line chart | Displays trends |

| Which station has higher pollution? | Bar chart | Compares categories |

| What is the distribution of PM2.5? | Histogram | Shows frequency distribution |

| Is temperature related to PM2.5? | Scatter plot | Shows possible correlation |



\## 6. Expected Benefits



1\. Identifies pollution trends over time.

2\. Compares air quality across monitoring stations.

3\. Helps identify unusually high readings.

4\. Makes large datasets easier to understand.

5\. Supports evidence-based environmental decisions.



\## 7. Conclusion



Data analysis and visualisation transform cleaned air-quality readings into useful information. Daily summary tables and appropriate charts help identify pollution patterns, compare monitoring stations and understand environmental trends. These outputs support better monitoring and decision-making.

