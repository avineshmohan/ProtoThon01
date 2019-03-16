from itertools import permutations

import xlrd

filelocation ="C:\\Users\\Avinesh\\Desktop\\Protothon\\Program5\\word.xlsx"


workbook = xlrd.open_workbook(filelocation)

sheet = workbook.sheet_by_index(0)


filelocation = ""

a="ProtoSem"

x=permutations(a)

# print(x)

total_rows = sheet.nrows


for i in x:
    str = ''.join(i)
    # print
    for j in range(total_rows):
        if str.lower() == sheet.cell_value(j,0):
            print(str)




