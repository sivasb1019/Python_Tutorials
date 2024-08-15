import xlrd

loc = "C:\\Users\\sivab\\OneDrive\\Desktop\\Book1.xlsx"
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
print()
