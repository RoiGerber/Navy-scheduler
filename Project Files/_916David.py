import numpy as np
import random
import xlwt

ADCounter = [0,0,0,0,0,0,0,0]
AFCounter = [0,0,0,0,0,0,0,0]
ShaotYam = [0,0,0,0,0,0,0,0]
BrokenShip = 88888888
NewWeek = input("is it a new week? (yes/no)")
#IsBrokenShip = input("is there a broken ship? (yes/no)")
#if IsBrokenShip == "yes":
#    BrokenShip = int(input("which ship is broken? (0-7)"))

if NewWeek == "no":
    OldWeekDay = input("I will need your history, How many days have passed? (1-7)")
    for i in range(int(OldWeekDay)):
        Tami = int(input("who was Tami on day "+ str(i)+"? (0-7)"))
        ADCounter[Tami] = ADCounter[Tami] +1
        Roni = int(input("who was Roni on day "+ str(i)+"? (0-7)"))
        ADCounter[Roni] = ADCounter[Roni] +1
        Gal = int(input("who was Gal on day "+ str(i)+"? (0-7)"))
        ADCounter[Gal] = ADCounter[Gal] +1
        Orly = int(input("who was Orly on day "+ str(i)+"? (0-7)"))
        ADCounter[Orly] = ADCounter[Orly] +1
        Miadi = int(input("who was Miadi on day "+ str(i)+"? (0-7)"))
        ADCounter[Tami] = ADCounter[Tami] +1
        Daniela = int(input("who was Daniela on day "+ str(i)+"? (0-7)"))
        ADCounter[Daniela] = ADCounter[Daniela] +1


DaysNum = 7


SchedueledTasksAtoD = np.zeros(shape=(DaysNum,4))
SchedueledTasksAtoF = np.zeros(shape=(DaysNum,2))

index = random.randint(0,7)


#print(SchedueledTasksAtoD)
#print(SchedueledTasksAtoF)


def GetAD():
    global index
    global ADCounter
    global AFCounter
    ADlist = []
    while len(ADlist) < 4:
        if ADCounter[index] < 3 and AFCounter[index] < 4:
            ADlist.append(index)
            ADCounter[index] = ADCounter[index] + 1
            AFCounter[index] = AFCounter[index] + 1
        index = index +1
        if index > 7:
            index = 0
        
    i = 0
    while i < len(ADCounter):
        if i not in ADlist:
            ADCounter[i] = 0
        i = i + 1
    return ADlist 


def GetEF(ADships):
    EFships = []
    global AFCounter
    global ADCounter
    global index

    while len(EFships)<2:
        if AFCounter[index] < 4:
            if index not in  ADships:
                EFships.append(index)
                AFCounter[index] = AFCounter[index] + 1
            index = index + 1
        if index > 7:
            index = 0
    i = 0
    while i < len(AFCounter):
        if i not in ADships:
            if i not in EFships:
                AFCounter[i] = 0
        i = i + 1
    return EFships

Day = 0
while Day<DaysNum:
    ADships = GetAD()
    EFships = GetEF(ADships)
    SchedueledTasksAtoD[Day,0] = ADships[0]
    SchedueledTasksAtoD[Day,1] = ADships[1]
    SchedueledTasksAtoD[Day,2] = ADships[2]
    SchedueledTasksAtoD[Day,3] = ADships[3]
    SchedueledTasksAtoF[Day,0] = EFships[0]
    SchedueledTasksAtoF[Day,1] = EFships[1]
    DayToPrint = Day + 2
    if DayToPrint > 7:
        DayToPrint = 1
    print("Day number " + str(DayToPrint)+ ")"+
          "   Tami " + str(SchedueledTasksAtoD[Day,0]) +
          "   Roni  "+ str(SchedueledTasksAtoD[Day,1]) +
          "   Gal " + str(SchedueledTasksAtoD[Day,2]) +
          "   Orly " + str(SchedueledTasksAtoD[Day,3]) +
          "   |   Miadi " + str(SchedueledTasksAtoF[Day,0]) +
          "   Daniela " + str(SchedueledTasksAtoF[Day,1]))


    for s in ADships:
        ShaotYam[s] = ShaotYam[s] + 24
    for s in EFships:
        ShaotYam[s] = ShaotYam[s] + 24
    Day = Day + 1
    

print(ShaotYam)

import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('Looz916.xlsx')
worksheet = workbook.add_worksheet()

# Some data we want to write to the worksheet.
###expenses = (
###    ['Rent', 1000],
###    ['Gas',   100],
###    ['Food',  300],
###    ['Gym',    50],
###)

# Start from the first cell. Rows and columns are zero indexed.






Ship0=[]
Ship1=[]
Ship2=[]
Ship3 =[]
Ship4 =[]
Ship5 =[]
Ship6 =[]
Ship7 =[]

FullSched = np.concatenate((SchedueledTasksAtoD,SchedueledTasksAtoF), axis = 1)

SessionOfShips =[Ship0, Ship1, Ship2, Ship3, Ship4, Ship5, Ship6, Ship7]
for Tami,Roni,Gal,Orly,Miadi,Daniela in FullSched:
    SessionOfShips[int(Tami)].append("Tami")
    SessionOfShips[int(Roni)].append("Roni")
    SessionOfShips[int(Gal)].append("Gal")
    SessionOfShips[int(Orly)].append("Orly")
    SessionOfShips[int(Miadi)].append("Miadi")
    SessionOfShips[int(Daniela)].append("Daniela")

    for i in range(8):
        if i != int(Tami) and i != int(Roni) and i != int(Gal) and i != int(Orly) and i != int(Miadi) and i != int(Daniela):
            SessionOfShips[i].append("Hof")

worksheet.write(1, 0,"825")
worksheet.write(2, 0,"830")
worksheet.write(3, 0,"831")
worksheet.write(4, 0,"832")
worksheet.write(5, 0,"833")
worksheet.write(6, 0,"834")
worksheet.write(7, 0,"835")
worksheet.write(8, 0,"836")
worksheet.write(0, 0,"ship")
worksheet.write(0, 1,"monday")
worksheet.write(0, 2,"tuesday")
worksheet.write(0, 3,"wedensday")
worksheet.write(0, 4,"thursday")
worksheet.write(0, 5,"friday")
worksheet.write(0, 6,"saturday")
worksheet.write(0, 7,"sunday")

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




for i in range (len(ShaotYam)):
    worksheet.write(i+1,8, ShaotYam[i])
worksheet.write(0,8, "Shaot Yam")
print("jaguar")
