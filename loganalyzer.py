from lxml import etree
from xlrd import open_workbook
import xlwt
import sys
import re
reload(sys)

sys.setdefaultencoding("ISO-8859-1")

if len (sys.argv) != 2 :
    print "Usage: python loganalyzer.py inputfile"
    sys.exit (1)

inputfile = sys.argv[1]
outputfile = "converted " + inputfile


input_wb = open_workbook(inputfile)
output_wb = xlwt.Workbook()

count = 0
start_line = 0
if fist_line_contains_row_labels:
    start_line = 1

type_Dict = {}

for type in "INFO", "WARN", "ERROR", "FATAL":
    type_Dict[type] = []
    in_sheet = input_wb.sheet_by_name(type)

    for row in range(in_sheet.nrows)[start_line:]:
        message = (in_sheet.cell(row,1).value)
        for line in message.splitlines():
            if type + ":" in line:
                if line not in type_Dict[type]:
                    type_Dict[type].append(line)
    out_sheet = output_wb.add_sheet(type)
    row = 0
    for line in type_Dict[type]:
        row +=1
        out_sheet.write(row, 0, line)

output_wb.save(outputfile)
