import xlsxwriter
import xlrd

def TurnNumbersIntoExcelCells(Day, Ship):
    Letters = ['B', 'C', 'D', 'E', 'F', 'G']
    OutPutDay = Letters[Day]
    OutPutShip = str(Ship + 1)
    FinalOutPut = OutPutDay + OutPutShip
    return FinalOutPut

def ExportToExcel(SessionOfShips, ShaotYamShips, Info, sheet):
    Printovisch = sheet.cell_value(0, 0)
    
    workbook = xlsxwriter.Workbook('Looz916.xlsx')
    worksheet = workbook.add_worksheet()
    
    format1 = workbook.add_format({'bg_color': 'FFCCCC', 'font_color': '#000000'})
    format2 = workbook.add_format({'bg_color': 'BBBBBB', 'font_color': '#000000'})
    format3 = workbook.add_format({'bg_color': '000000', 'font_color': '#000000'})
    
    for i in range(1, 9):
        worksheet.write(i, 0, sheet.cell_value(i, 3))
    
    worksheet.write(0, 0, "ספינה")
    worksheet.write(0, 1, "שני")
    worksheet.write(0, 2, "שלישי")
    worksheet.write(0, 3, "רביעי")
    worksheet.write(0, 4, "חמישי")
    worksheet.write(0, 5, "שישי")
    worksheet.write(0, 6, "שבת")
    worksheet.write(0, 7, "ראשון")

    row = 1
    col = 1
    try:
        for a, b, c, d, e, f, g in SessionOfShips:
            worksheet.write(row, col, a)
            worksheet.write(row, col + 1, b)
            worksheet.write(row, col + 2, c)
            worksheet.write(row, col + 3, d)
            worksheet.write(row, col + 4, e)
            worksheet.write(row, col + 5, f)
            worksheet.write(row, col + 6, g)
            row += 1
    except:
        exit

    worksheet.write(0, 8, "שעות ים השבוע")
    for i in range(1, 9):
        worksheet.write(i, 8, ShaotYamShips[i - 1])

    worksheet.write(15, 15, Printovisch)

    conditions = [
        ('"תמי"', format1),
        ('"רוני"', format1),
        ('"גל"', format1),
        ('"אורלי"', format1),
        ('"מיידי"', format2),
        ('"דניאלה"', format2),
        ('"חוף"', format3),
    ]
    
    for condition, format_style in conditions:
        worksheet.conditional_format('A1:K12', {'type': 'cell', 'criteria': '==', 'value': condition, 'format': format_style})

    workbook.close()

def load_excel_file(filepath):
    wb = xlrd.open_workbook(filepath)
    return wb.sheet_by_index(0)

