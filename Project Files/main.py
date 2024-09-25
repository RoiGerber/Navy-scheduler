import time
import random
import xlrd
from itertools import permutations
from Rules import NotMoreThan3DaysDynamic, Not360, MustBeIn, HasMabab, HasTami, NotDoubled
from excel_operations import ExportToExcel, load_excel_file
from Terminal_operations import printProgressBar, PrintScheduelByShips

# ... [Keep the existing Info class and other helper functions] ...

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

    def InsertMust(self,DayMustBeIn,ShipSpecific,SioorMustBeIn):
        self.Musts.append([DayMustBeIn,ShipSpecific,SioorMustBeIn])


    def Delete24From360(self,HowToAllocate):
        for Ship in HowToAllocate:
            self.ShaotYam[Ship] -= 24

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
          
def Validate(Day,HowToAllocate,Info,History,EightBasedOptions):    
    if NotMoreThan3DaysDynamic(Day,HowToAllocate,Info,History):
        if Not360(Day,HowToAllocate,Info,History):
            if MustBeIn(Day,HowToAllocate,Info,History):
                if HasMabab(Day,HowToAllocate,Info,History):
                    if HasTami(Day,HowToAllocate,Info,History):
                        if NotDoubled(Day,HowToAllocate,Info,History):
                            return True
    return False

def ClientInfo(Inf,loc):
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
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

def create_schedule_by_ships(history):
    # Initialize lists for each ship
    ships = [[] for _ in range(8)]  # Creates 8 empty lists, one for each ship
    
    # Loop through each record in the history
    for tami, roni, gal, orly, miadi, daniela, hof1, hof2 in history:
        # Assign crew members to the corresponding ship
        ships[tami].append("תמי")
        ships[roni].append("רוני")
        ships[gal].append("גל")
        ships[orly].append("אורלי")
        ships[miadi].append("מיידי")
        ships[daniela].append("דניאלה")
        
        # Assign the remaining ships to "חוף" (shore) if no crew members are assigned
        for i in range(8):
            if i not in [tami, roni, gal, orly, miadi, daniela]:
                ships[i].append("חוף")
    
    return ships

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

def dynamic_allocate(Info, Permutations, sheet):
    max_days = 7
    dp_table = {}

    def dp_helper(day, current_allocation, history):
        if day > max_days:
            return history

        state = (day, tuple(current_allocation), tuple(map(tuple, history)))
        if state in dp_table:
            return dp_table[state]

        if Validate(day, current_allocation, Info, history, Permutations):
            new_history = history + [current_allocation]
            best_solution = None
            
            for option in random.sample(Permutations, min(20, len(Permutations))):
                solution = dp_helper(day + 1, option, new_history)
                if solution and (not best_solution or len(solution) > len(best_solution)):
                    best_solution = solution

            dp_table[state] = best_solution
            return best_solution

        dp_table[state] = None
        return None

    best_solution = None
    for initial_option in random.sample(Permutations, min(100, len(Permutations))):
        solution = dp_helper(1, initial_option, [])
        if solution and (not best_solution or len(solution) > len(best_solution)):
            best_solution = solution

    return best_solution

def main():
    loc = "InputLooz.xls"
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    Permutations = list(permutations(range(8)))

    Inf = Info()    
    ClientInfo(Inf, loc)

    final_schedule = dynamic_allocate(Inf, Permutations, sheet)

    if final_schedule:
        ShaotYamShips = CalculateShaotYam(final_schedule, Inf)
        print("Congrats!")
        print(final_schedule)
        for ShipNum, ship in enumerate(ShaotYamShips):          
            print(f"Ship Number {ShipNum}: {ship}")

        PrintScheduelByShips(create_schedule_by_ships(final_schedule))
        ExportToExcel(create_schedule_by_ships(final_schedule), ShaotYamShips, Inf, sheet=sheet)
    else:
        main()
        

if __name__ == "__main__":
    main()