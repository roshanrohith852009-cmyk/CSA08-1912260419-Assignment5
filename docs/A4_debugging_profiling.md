\# A4 – Debugging and Profiling



\## 1. Introduction



Debugging is the process of finding and correcting errors in a program. Profiling measures program performance, including execution time and resource usage.



In the City Air-Quality Monitoring Network, debugging ensures reliable data processing, while profiling helps identify performance bottlenecks when processing large datasets.



\## 2. Logging



Logging records important events during program execution.



The system will use different logging levels:



| Level | Purpose |

|---|---|

| DEBUG | Detailed information for troubleshooting |

| INFO | Normal processing information |

| WARNING | Unexpected situations |

| ERROR | Processing errors |

| CRITICAL | Serious failures |



Example log messages:



\- INFO: CSV file loaded successfully.

\- WARNING: Missing PM2.5 value detected.

\- ERROR: Invalid timestamp found.

\- INFO: Cleaned data saved to SQLite.



\## 3. Assertions



Assertions check whether important conditions are true.



Examples:



```python

assert pm25 >= 0

assert 0 <= humidity <= 100

assert station\_id is not None

```



Assertions help detect invalid assumptions during development. They should not replace normal input validation.



\## 4. Python Debugger (pdb)



The Python debugger allows developers to inspect program execution step by step.



Useful commands:



| Command | Purpose |

|---|---|

| `break` | Set a breakpoint |

| `next` | Execute the next line |

| `step` | Enter a function |

| `continue` | Continue execution |

| `print` | Display variable values |

| `quit` | Exit the debugger |



Pseudocode:



```text

BEGIN DEBUGGING



&#x20;   SET breakpoint in cleaning function



&#x20;   RUN program



&#x20;   INSPECT current variable values



&#x20;   EXECUTE statements step by step



&#x20;   IDENTIFY incorrect values



&#x20;   CORRECT the error



&#x20;   CONTINUE program



END DEBUGGING

```



\## 5. Performance Profiling with cProfile



cProfile is a built-in Python profiling tool. It measures how much time functions spend executing.



It can identify:



\- Functions taking the most execution time.

\- Frequently called functions.

\- Potential performance bottlenecks.



Proposed command:



```powershell

python -m cProfile -s cumulative src/cleaning\_pipeline.py

```



The output can be saved for later examination.



\## 6. Profiling Plan



The system will be tested using different dataset sizes.



| Dataset Size | Purpose |

|---|---|

| 1,000 records | Small dataset performance |

| 10,000 records | Medium dataset performance |

| 100,000 records | Large dataset performance |



The following measurements will be collected:



1\. Total execution time.

2\. Time spent in individual functions.

3\. Memory usage.

4\. Number of records processed.



\## 7. Debugging and Profiling Pseudocode



```text

BEGIN



&#x20;   CONFIGURE logging



&#x20;   LOAD air-quality dataset



&#x20;   VALIDATE input records



&#x20;   USE assertions for important conditions



&#x20;   IF an error occurs

&#x20;       RECORD error in log

&#x20;       INSPECT using debugger

&#x20;       CORRECT the problem

&#x20;   END IF



&#x20;   START performance profiling



&#x20;   EXECUTE data processing



&#x20;   RECORD execution time



&#x20;   ANALYSE profiling results



&#x20;   IDENTIFY bottlenecks



&#x20;   SAVE profiling report



END

```



\## 8. Conclusion



Logging, assertions and debugging tools improve program reliability. cProfile helps identify functions that consume significant execution time. Combining these techniques makes the air-quality monitoring system easier to troubleshoot, maintain and optimise.

