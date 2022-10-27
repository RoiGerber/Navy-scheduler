import numpy as np
import time
import random
import xlwt
import xlsxwriter
from itertools import permutations
import xlrd
loc = ("C:\\Users\\gerbe\\OneDrive\\מסמכים\\looz916\\916David\\InputLooz.xls")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
Printovisch = sheet.cell_value(0, 0)

EightBasedOptions = list(permutations(range(8)))

def PrintScheduelByShips(SessionOfShips):
    for i in range(7):
        LineToPrint = "ship "+str(i)
        for Day in SessionOfShips[i]:
            LineToPrint += "  " + str(Day)
        print(LineToPrint)


def CreateScheduelByShips(Hisory):
    Ship0=[]
    Ship1=[]
    Ship2=[]
    Ship3=[]
    Ship4=[]
    Ship5=[]
    Ship6=[]
    Ship7=[]
    SessionOfShips=[Ship0,Ship1,Ship2,Ship3,Ship4,Ship5,Ship6,Ship7]
    for Tami,Roni,Gal,Orly,Miadi,Daniela,Hof1,Hof2 in History:
        SessionOfShips[Tami].append("תמי")
        SessionOfShips[Roni].append("רוני")
        SessionOfShips[Gal].append("גל")
        SessionOfShips[Orly].append("אורלי")
        SessionOfShips[Miadi].append("מיידי")
        SessionOfShips[Daniela].append("דניאלה")
        for i in range(8):
            if i != Tami and i != Roni and i != Gal and i != Orly and i != Miadi and i != Daniela:
                SessionOfShips[i].append("חוף")
    return SessionOfShips


def TurnNumbersIntoExcelCells(Day,Ship):
    Letters = ['B','C','D','E','F','G']
    OutPutDay = Letter[Day]
    OutPutShip = str(Ship + 1)
    FinalOutPut = OutPutDay + OutPutShip
    return FinalOutPut



def ExportToExcel(SessionOfShips,ShaotYamShips,Info):
    global Printovisch
    
    workbook = xlsxwriter.Workbook('Looz916.xlsx')
    worksheet = workbook.add_worksheet()
    format1 = workbook.add_format({'bg_color': 'FFCCCC',
                               'font_color': '#000000'})
    format2 = workbook.add_format({'bg_color': 'BBBBBB',
                               'font_color': '#000000'})
    format3 = workbook.add_format({'bg_color': '000000',
                               'font_color': '#000000'})
    worksheet.write(1, 0,sheet.cell_value(1, 3))
    worksheet.write(2, 0,sheet.cell_value(2, 3))
    worksheet.write(3, 0,sheet.cell_value(3, 3))
    worksheet.write(4, 0,sheet.cell_value(4, 3))
    worksheet.write(5, 0,sheet.cell_value(5, 3))
    worksheet.write(6, 0,sheet.cell_value(6, 3))
    worksheet.write(7, 0,sheet.cell_value(7, 3))
    worksheet.write(8, 0,sheet.cell_value(8, 3))
    worksheet.write(0, 0,"ספינה")
    worksheet.write(0, 1,"שני")
    worksheet.write(0, 2,"שלישי")
    worksheet.write(0, 3,"רביעי")
    worksheet.write(0, 4,"חמישי")
    worksheet.write(0, 5,"שישי")
    worksheet.write(0, 6,"שבת")
    worksheet.write(0, 7,"ראשון")

    #BrokenArray = Inf.Musts
    #format2 = workbook.add_format({'bg_color': '#C6EFCE',
    #                               'font_color': '#006100'})
    #for Case in BrokenArray:
    #    worksheet.conditional_format(TurnNumbersIntoExcelCells(Case[0],Case[1]), {'type':     'cell',
    #                                        'criteria': '>=',
    #                                        'value':    5,
    #                                        'format':   format2
    #                                        })

    row = 1
    col = 1

# Iterate over the data and write it out row by row.
    for a, b, c, d, e, f, g in (SessionOfShips):
        worksheet.write(row, col, a)
        worksheet.write(row, col + 1, b)
        worksheet.write(row, col + 2, c)
        worksheet.write(row, col + 3, d)
        worksheet.write(row, col + 4, e)
        worksheet.write(row, col + 5, f)
        worksheet.write(row, col + 6, g)
        row = row + 1


    worksheet.write(0, 8, "שעות ים השבוע")
    worksheet.write(1, 8, ShaotYamShips[0])
    worksheet.write(2, 8, ShaotYamShips[1])
    worksheet.write(3, 8, ShaotYamShips[2])
    worksheet.write(4, 8, ShaotYamShips[3])
    worksheet.write(5, 8, ShaotYamShips[4])
    worksheet.write(6, 8, ShaotYamShips[5])
    worksheet.write(7, 8, ShaotYamShips[6])
    worksheet.write(8, 8, ShaotYamShips[7])
    worksheet.write(15, 15, Printovisch)


    worksheet.conditional_format('A1:K12', {'type':     'cell',
                                        'criteria': '==',
                                        'value':  '"תמי"'  ,
                                        'format':   format1})
    worksheet.conditional_format('A1:K12', {'type':     'cell',
                                        'criteria': '==',
                                        'value':  '"רוני"'  ,
                                        'format':   format1})
    worksheet.conditional_format('A1:K12', {'type':     'cell',
                                        'criteria': '==',
                                        'value':  '"גל"'  ,
                                        'format':   format1})
    worksheet.conditional_format('A1:K12', {'type':     'cell',
                                        'criteria': '==',
                                        'value':  '"אורלי"'  ,
                                        'format':   format1})
    worksheet.conditional_format('A1:K12', {'type':     'cell',
                                        'criteria': '==',
                                        'value':  '"מיידי"'  ,
                                        'format':   format2})
    worksheet.conditional_format('A1:K12', {'type':     'cell',
                                        'criteria': '==',
                                        'value':  '"דניאלה"'  ,
                                        'format':   format2})
    worksheet.conditional_format('A1:K12', {'type':     'cell',
                                        'criteria': '==',
                                        'value':  '"חוף"'  ,
                                        'format':   format3})
    workbook.close()




def IsEqual(a,b):
    HowMany = 0
    for i in a:
        for ii in b:
            if i == ii:
                HowMany = HowMany + 1
    if HowMany == 4:
        return True
    else:
        return False

def ListContain(l1,l2):
    for i in l1:
        for ii in l2:
            if i == ii:
                return True
    return False

class Info:
    def __init__(self):
        self.BrokenArray = []
        self.ShaotYam = [0,0,0,0,0,0,0,0]
        self.Mababs =   [0,0,0,0,0,0,0,0]
        self.Tamistim = [0,0,0,0,0,0,0,0]
        self.Musts = []

    def IsBroken(self,Day,Ship):
        for case in self.BrokenArray:
            if case[0] == Day and case[1] == Ship:
                return True
        return False

    def InsertBrokenArray(self,Day,Ship):
        self.BrokenArray.append([Day,Ship])
        
    def DidntPass360(self,Ship):
        if self.ShaotYam[Ship]+24<360:
            return True
        return False

    def Insert360(self,Ship,Hours):
        self.ShaotYam[Ship] =  Hours

    def Update360(self,HowToAllocate):
        for Ship in HowToAllocate[:4]:
            self.ShaotYam[Ship] += 24
        #for Ship in HowToAllocate[-1:]:
        #    self.ShaotYam[Ship] += 16

    def InsertMust(self,DayMustBeIn,ShipSpecific,SioorMustBeIn):
        self.Musts.append([DayMustBeIn,ShipSpecific,SioorMustBeIn])


    def Delete24From360(self,HowToAllocate):
        for Ship in HowToAllocate:
            self.ShaotYam[Ship] -= 24
        #for Ship in HowToAllocate[-1:]:
        #    self.ShaotYam[Ship] -= 16

    def GetShaotYam(self,Ship):
        return self.ShaotYam[Ship]

    def IsMabab(self,Ship):
        if self.Mababs[Ship] == 1:
            return True
        else:
            return False

    def IsTami(self,Ship):
        if self.Tamistim[Ship] == 1:
            return True
        else:
            return False
    

        

  


ADAfter = []
EFAfter = []
ADOrders = []
EFOrders = []


def NotMoreThan3d(Day,HowToAllocate,Info,History):
    if len(History) < 3:
        return True
    else:
        for Ship in HowToAllocate:
            DayInARow = 0
            for HistoryDay in History[-3:]:
                if Ship in HistoryDay:
                    DayInARow += 1
                    if DayInARow > 2:
                        return False
    return True

def NotMoreThan3DaysDynamic(Day,HowToAllocate,Info,History):
    if len(History) < 2:
        return True
    elif len(History) > 5:
        return True
    else:
        for Ship in HowToAllocate[:4]:
            DayInARow = 0
            for HistoryDay in History[-2:]:
                if Ship in HistoryDay[:4]:
                    DayInARow += 1
                    if DayInARow > 1:
                        return False
    return True

def NotBroken(Day,HowToAllocate,Info,History):
    for Ship in HowToAllocate:
        if Info.IsBroken(Day,Ship):
            return False
    return True

    
def Not360(Day,HowToAllocate,Info,History):
    for Ship in HowToAllocate:
        if not Info.DidntPass360(Ship):
            return False
    return True

def MustBeIn(Day,HowToAllocate,Info,History):
    Counter = 0
    for Case in Info.Musts:
        if Case in Info.Musts:
            if Case[0] == Day:
                Counter = Counter + 1
    CorrectCaseCounter = 0
    if Counter > 0:
        for Case in Info.Musts:
            if Case[0] == Day:
                if HowToAllocate[Case[2]]==Case[1]:
                    CorrectCaseCounter = CorrectCaseCounter + 1
                else:
                    return False
    if CorrectCaseCounter == Counter:
        return True
    else:
        return False

def HasMabab(Day,HowToAllocate,Info,History):
    for Ship in HowToAllocate[:4]:
        if Info.IsMabab(Ship):
            return True
    return False

def HasTami(Day,HowToAllocate,Info,History):
    if Info.IsTami(HowToAllocate[0]):
        return True
    return False

def NotDoubled(Day,HowToAllocate,Info,History):
    if Day == 1 :
        return True
    for Pos in range(7):
        if HowToAllocate[Pos] == History[Day - 2][Pos]:
            return False
        else:
            return True
#def UnderstandHyuristic(Day,HowtoAllocate)

def Validate(Day,HowToAllocate,Info,History):
    
    if True: # NotMoreThan3d(Day,HowToAllocate,Info,History):
        if NotMoreThan3DaysDynamic(Day,HowToAllocate,Info,History):
            if True:# NotBroken(Day,HowToAllocate,Info,History):
                if Not360(Day,HowToAllocate,Info,History):
                    if MustBeIn(Day,HowToAllocate,Info,History):
                        if HasMabab(Day,HowToAllocate,Info,History):
                            if HasTami(Day,HowToAllocate,Info,History):
                                if NotDoubled(Day,HowToAllocate,Info,History):
                                    return True
    return False



# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    
    #Call in a loop to create terminal progress bar
    #@params:

        #iteration   - Required  : current iteration (Int)
        #total       - Required  : total iterations (Int)
        #prefix      - Optional  : prefix string (Str)
        #suffix      - Optional  : suffix string (Str)
        #decimals    - Optional  : positive number of decimals in percent complete (Int)
        #length      - Optional  : character length of bar (Int)
        #fill        - Optional  : bar fill character (Str)
        #printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    
    
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    
    if iteration == total: 
        print()
       


def CalculateShaotYam(History,Info):
    Ships = [0,0,0,0,0,0,0,0]
    for Day in History:
        for Ship in Day[:4]:
            Ships[Ship] = Ships[Ship] + 24
        for Ship in Day[-2:]:
            Ships[Ship] = Ships[Ship] + 16
    for Ship in range(7):
       Ships[Ship] = Ships[Ship] + Info.ShaotYam[Ship]

    return Ships

def Allocate (Day, HowToAllocate,Info,History):
    global Options
    global EightBasedOptions
    global FakeOptions
    global FreakyCounter
    # Update Progress Bar
    if Day > 7:
        for i in range(100):
            # Do stuff...
            time.sleep(0.001)
            # Update Progress Bar
            printProgressBar(i + 1, 100, prefix = 'Progress:', suffix = 'Complete', length = 50)
        ShaotYamShips = CalculateShaotYam(History,Info)
        print("Congrats!")
        print(History)
        ShipNum = 0
        for ship in ShaotYamShips:          
            print("Ship Number " + str(ShipNum) + "   " +str(ShaotYamShips[ShipNum]) )
            ShipNum += 1

        PrintScheduelByShips(CreateScheduelByShips(History))
        ExportToExcel(CreateScheduelByShips(History),ShaotYamShips,Info)
        input("finish")
        exit
     
    if Validate(Day,HowToAllocate,Info,History):
        History.append(HowToAllocate)
        #Info.Update360(HowToAllocate)  
        random.shuffle(EightBasedOptions)
        counterOption = 0
        for option in EightBasedOptions:
            if counterOption > 20:
                break
            Allocate(Day + 1, option,Info,History)
            

    else:
        return
    #Info.Delete24From360(HowToAllocate)
    History.pop(-1)    
    
def EasyYesNo(Question):
    Answer = input(Question + "?   (yes/no)\n")
    if Answer == 'yes' or Answer == 'y':
        return True
    else:
        return False

def DefineDay(DayInput):
    DayOutput = DayInput + 1
    if DayOutput == 8:
       DayOutput = 1
    return DayOutput

Inf = Info()
def ClientInfo():
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    global Inf
    print()
    FleetSize = 8
    if sheet.cell_value(8, 3) == 0:
        FleetSize = 7
        if sheet.cell_value(7, 3) == 0:
            FleetSize = 6
        
    if FleetSize == 7:
        for i in range(7):
            Inf.InsertBrokenArray(i+1,7)
    elif FleetSize == 6:
        for i in range(7):
            Inf.InsertBrokenArray(i+1,6)
        for i in range(7):
            Inf.InsertBrokenArray(i+1,7)

    for x in range(8):
        for y in range(7):
            if sheet.cell_value(x + 1, y + 4) == "חוף":
                Inf.InsertBrokenArray(y +1 , x )
            elif  sheet.cell_value(x + 1, y + 4) == "תמי":
                    Inf.InsertMust(y + 1, x , 0)

            elif  sheet.cell_value(x + 1, y + 4) == "רוני":
                    Inf.InsertMust(y + 1, x  , 1)

            elif  sheet.cell_value(x + 1, y + 4) == "גל":
                    Inf.InsertMust(y + 1, x ,2)

            elif  sheet.cell_value(x + 1, y + 4) == "אורלי":
                    Inf.InsertMust(y + 1, x ,3)

            elif  sheet.cell_value(x + 1, y + 4) == "מיידי" or sheet.cell_value(x + 1, y + 4) == "מידי":
                    Inf.InsertMust(y + 1, x ,4)

            elif  sheet.cell_value(x + 1, y + 4) == "דניאלה":
                    Inf.InsertMust(y + 1, x ,5)
    for x in range(1,8):
        Inf.Insert360(x-1,sheet.cell_value(x,2))
    for x in range(1,8):
        if sheet.cell_value(x,1) == 1:
            Inf.Mababs[x-1] = 1
    for x in range(1,8):
        if sheet.cell_value(x,0) == 1:
            Inf.Tamistim[x-1] = 1
            

  #  for x in range(8):
  #          for y in range(7):
  #              if sheet.cell_value(x + 1, y + 4) == "חוף":
  #                  Inf.InsertMust(x ,y + 1,0)      

    #if EasyYesNo("Is there a ship you want to be in a specific location"):
    #    HasMore = True
    #    while HasMore == True:
    #        ShipSpecific = int(input("Which Ship? (0-7)\n 0 - 825 \n 1 - 830\n 2 - 831 \n 3 - 832 \n 4 - 833 \n 5 - 834 \n 6 - 835 \n 7 - 836 \n"))
    #        DayMustBeIn = int(input("when? (1-7)\n 1 - Monday\n 2 - Tuesday\n 3 - Wedensday\n 4 - Thursday \n 5 - Friday \n 6 - saturday\n 7 - Sunday\n"))
    #        SioorMustBeIn = int(input("where do you want it to be? \n 0 - Tami \n 1 - Roni \n 2 - Gal \n 3 - Orly \n 4 - Miadi \n 5 - Daniela\n"))
    #        Inf.InsertMust(DayMustBeIn,ShipSpecific,SioorMustBeIn)
    #        HasMore = EasyYesNo("more")
    
    


ClientInfo()
History = []


random.shuffle(EightBasedOptions)


FakeOptions=[[6, 3, 2, 7, 0, 5], [3, 5, 6, 2, 0, 4], [1, 7, 4, 5, 0, 3], [6, 1, 4, 3, 2, 5], [3, 2, 0, 7, 6, 1], [2, 7, 0, 1, 5, 3], [0, 7, 5, 4, 3, 2]]
for Option in EightBasedOptions:
    Allocate(1,Option,Inf,History)

print("Faild to allocate ships")




             