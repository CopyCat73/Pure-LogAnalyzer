# Pure-LogAnalyzer
Convert pure job logs to a more concise format

Usage:

This script is for Python 2.7.X. 

Install the excel libraries xlrd and xlwt (i.e. pip install xlrd, pip install xlwt)

In the Pure admin tab open job log, open a log entry and make sure the dropdown says "all log entries". Click the "Export log entries as MS Excel" button. 

Put the python script and excel file in the same folder and run:

python loganalyzer.py yourlogfile.xlsx

Tested on person and organization sync logs. 
