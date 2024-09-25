
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
