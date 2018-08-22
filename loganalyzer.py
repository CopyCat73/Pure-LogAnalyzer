from lxml import etree
from xlrd import open_workbook
import xlwt
import sys
import re
import os
reload(sys)

sys.setdefaultencoding("ISO-8859-1")

if len (sys.argv) != 2 :
    print "Usage: python loganalyzer.py inputfile"
    sys.exit (1)

inputfile = sys.argv[1]
outputfile = "converted " + inputfile
outputfile = outputfile.replace('.xlsx','.xls')

if os.path.isfile(outputfile):
    print "\noutputfile \'" + outputfile + "\' already exists, deleting.\nPlease close the file in excel if you still have it open.\n"
    os.remove(outputfile)


input_wb = open_workbook(inputfile)
output_wb = xlwt.Workbook()
info_sheet = output_wb.add_sheet("INFO")
warn_sheet = output_wb.add_sheet("WARN")
error_sheet = output_wb.add_sheet("ERROR")

info_sheet.write(0, 0, "Created")
info_sheet.write(0, 1, "Updated")
info_sheet.write(0, 2, "Retired")
info_sheet.write(0, 3, "Job total")
info_sheet.write(0, 4, "Script total")
warn_sheet.write(0, 0, "Unique warnings")
warn_sheet.write(0, 1, "Split terms on semicolon")
error_sheet.write(0, 0, "Unique errors")
error_sheet.write(0, 1, "Split terms on semicolon")
ccount = ucount = rcount = 1
wmcount = emcount = 0

type_Dict = {}
status_Dict = {}
warn_Dict = {}
error_Dict = {}

for status in "creating", "updating", "retiring":
    status_Dict[status] = []


def find_ids(line):
    ids = []
    line = line.replace(",",":")
    tempids = re.split(r":", line)
    for id in tempids:
        id = id.strip()
        if id!="WARN" and id!="ERROR":
            ids.append(id)
    return ids

for type in "INFO", "WARN", "ERROR":

    in_sheet = input_wb.sheet_by_name(type)

    type_Dict[type] = []

    for row in range(in_sheet.nrows)[0:]:
        message = (in_sheet.cell(row,1).value)
        lc = 0
        for line in message.splitlines():
            lc +=1
            if lc == 1:
                id = re.findall('\d+', line)
                for status in "creating", "updating", "retiring":
                    if line.lower().startswith(status):
                        if id not in status_Dict[status]: status_Dict[status].append(id)
            if type == "INFO" and "found" in line.lower() and "required" in line.lower():
                jcount = re.search('INFO: (.*) found', line).group(1)
                info_sheet.write(1, 3 ,jcount)
            if type == "WARN" and type + ":" in line:
                warn_Dict[line] = find_ids(line)
            if type == "ERROR" and type + ":" in line:
                error_Dict[line] = find_ids(line)


for line in status_Dict["creating"]:
    if line in status_Dict["updating"] or line in status_Dict["retiring"]: print "yes"
    info_sheet.write(ccount, 0 ,line)
    ccount +=1
for line in status_Dict["updating"]:
    info_sheet.write(ucount, 1 ,line)
    ucount +=1
for line in status_Dict["retiring"]:
    info_sheet.write(rcount, 2 ,line)
    rcount +=1

# for person log the script count is always +1 to what the log states?
info_sheet.write(1, 4 , len(status_Dict["creating"]) + len(status_Dict["updating"]) + len(status_Dict["retiring"]))

for line in warn_Dict:
    wmcount +=1
    warn_sheet.write(wmcount, 0, line)
    idc = 1
    for id in warn_Dict[line]:
        warn_sheet.write(wmcount, 0+idc, id)
        idc+=1
for line in error_Dict:
    emcount +=1
    error_sheet.write(emcount, 0, line)
    idc = 1
    for id in error_Dict[line]:
        error_sheet.write(emcount, 0+idc, id)
        idc+=1

output_wb.save(outputfile)
