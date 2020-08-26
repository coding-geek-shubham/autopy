# importing openpyxl python lib as elios xl
import openpyxl as xl
# Opening xl workbook
wb = xl.load_workbook('transaction.xlsx')
sheet = wb['Sheet1']
cell = sheet['a1']
cell = sheet.cell(1,1)  # Returns the exact same cell
print(cell.value)