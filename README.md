LogReport.py
==
A reporting tool used to analyze log files from a website database

Installation and Usage
====
Copy the LogAnalysis.py and the LogReport.py to your vagrant directory
and run LogReport.py

Modules
==
LogAnalysis.py contains the functions used to connect to the database API and
extract data

Databases
==
Name: news
Tables: Articles, Authors, Log

Views
==
dailyErrors: table containing each day and the percentage of errors per day

Column      |  Type   | Modifiers
-----------------+---------+-----------
 date            | date    |
 errorpercentage | numeric |

PSQL code
create view dailyErrors as select date(time) as date,
ROUND(100.00 * count(case when status like '%404%' then 1 else null end)/count(*),2) as ErrorPercentage
from log group by date;
