# Pure-LogAnalyzer
Convert pure job logs to a more concise and reusable format

## Usage

This script is for Python 2.7.X. 

Install the excel libraries xlrd and xlwt (i.e. pip install xlrd, pip install xlwt)

In the Pure admin tab open job log, open a log entry and make sure the dropdown says "all log entries". Click the "Export log entries as MS Excel" button. 

![save excel](/loganalyzer_screenshot_1.png?raw=true")

Put the python script and excel file in the same folder and run:

python loganalyzer.py yourlogfile.xlsx

The result will be a new xls file starting with "converted". In the new excel there will be three sheets:

![INFO sheet](/loganalyzer_screenshot_2.png?raw=true")
* INFO contains created, updated and retired ids in separate columnns

![WARN and ERROR sheets](/loganalyzer_screenshot_3.png?raw=true")
* WARN and ERROR contain unique warnings and errors reported, and each message is split so that any ids or classifications should be retrievable from separated cells. 

Tested on log types:
* person 
* organization
* external organization
* award
* project
* user
* student thesis
