\# A5 – AI Application



\## 1. Introduction



Artificial Intelligence (AI) can help the City Air-Quality Monitoring Network understand citizen complaints and provide quick responses to common questions.



This system uses two basic AI applications:



1\. Rule-based sentiment analysis.

2\. Keyword-based chatbot.



These techniques provide simple automated assistance without requiring complex machine learning models.



\## 2. Rule-Based Sentiment Analysis



Sentiment analysis identifies the emotional tone of a citizen complaint.



The system classifies complaints into three categories:



\- Positive

\- Negative

\- Neutral



\### A. Positive Keywords



Examples:



\- clean

\- good

\- excellent

\- improved

\- fresh

\- better



\### B. Negative Keywords



Examples:



\- pollution

\- smoke

\- dust

\- unhealthy

\- bad

\- harmful

\- smell

\- dirty



\### C. Neutral Classification



If no positive or negative keywords are identified, the complaint is classified as neutral.



\### D. Sentiment Scoring



The system assigns:



\- Positive keyword: +1

\- Negative keyword: -1



The final sentiment is determined using the total score.



| Score | Classification |

|---|---|

| Greater than 0 | Positive |

| Less than 0 | Negative |

| Equal to 0 | Neutral |



Example:



Complaint: "The air pollution is bad and harmful."



Negative keywords detected: pollution, bad, harmful.



Total score = -3.



Result: Negative sentiment.



\## 3. Sentiment Analysis Pseudocode



```text

BEGIN



&#x20;   DEFINE positive keyword list



&#x20;   DEFINE negative keyword list



&#x20;   INPUT citizen complaint



&#x20;   CONVERT complaint to lowercase



&#x20;   SET sentiment score = 0



&#x20;   SPLIT complaint into words



&#x20;   FOR each word



&#x20;       IF word is in positive keyword list

&#x20;           INCREASE score by 1



&#x20;       ELSE IF word is in negative keyword list

&#x20;           DECREASE score by 1



&#x20;       END IF



&#x20;   END FOR



&#x20;   IF score is greater than 0

&#x20;       DISPLAY Positive



&#x20;   ELSE IF score is less than 0

&#x20;       DISPLAY Negative



&#x20;   ELSE

&#x20;       DISPLAY Neutral



&#x20;   END IF



END

```



\## 4. Keyword-Based Chatbot



A keyword-based chatbot responds to common citizen questions using predefined keywords and responses.



It does not require a complex machine learning model.



\### Example Keywords and Responses



| Keyword | Chatbot Response |

|---|---|

| AQI | AQI represents the Air Quality Index. |

| PM2.5 | PM2.5 refers to fine particulate matter in the air. |

| PM10 | PM10 refers to particulate matter with a diameter of up to 10 micrometres. |

| pollution | Pollution refers to harmful substances present in the environment. |

| station | Monitoring stations collect local air-quality readings. |

| health | Check official health guidance when air quality is poor. |



If the chatbot does not recognise a keyword, it displays:



"Sorry, I could not understand your question. Please try asking about AQI, PM2.5, PM10 or pollution."



\## 5. Chatbot Pseudocode



```text

BEGIN



&#x20;   DISPLAY chatbot welcome message



&#x20;   INPUT user question



&#x20;   CONVERT question to lowercase



&#x20;   IF question contains "AQI"

&#x20;       DISPLAY AQI explanation



&#x20;   ELSE IF question contains "PM2.5"

&#x20;       DISPLAY PM2.5 explanation



&#x20;   ELSE IF question contains "PM10"

&#x20;       DISPLAY PM10 explanation



&#x20;   ELSE IF question contains "pollution"

&#x20;       DISPLAY pollution explanation



&#x20;   ELSE IF question contains "station"

&#x20;       DISPLAY monitoring station information



&#x20;   ELSE IF question contains "health"

&#x20;       DISPLAY health guidance message



&#x20;   ELSE

&#x20;       DISPLAY default response



&#x20;   END IF



END

```



\## 6. Advantages of AI Applications



\### Sentiment Analysis



1\. Automatically classifies citizen complaints.

2\. Helps identify negative feedback.

3\. Reduces manual complaint classification.

4\. Supports understanding of public concerns.



\### Keyword-Based Chatbot



1\. Provides quick responses.

2\. Easy to implement and maintain.

3\. Does not require extensive training data.

4\. Helps citizens understand common air-quality terms.



\## 7. Limitations



\- Rule-based sentiment analysis may not understand sarcasm or complex sentences.

\- Keyword matching may miss spelling mistakes and similar words.

\- The chatbot can only answer questions covered by its predefined keywords.

\- Sentiment scores do not fully represent the meaning of a complaint.



\## 8. Conclusion



Rule-based sentiment analysis and a keyword-based chatbot provide simple AI applications for the City Air-Quality Monitoring Network. Sentiment analysis helps classify citizen complaints, while the chatbot provides information about air-quality measurements. These applications improve basic communication and support the monitoring system.

