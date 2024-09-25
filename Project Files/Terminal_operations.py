def PrintScheduelByShips(SessionOfShips):
    for i in range(7):
        LineToPrint = "ship "+str(i)
        for Day in SessionOfShips[i]:
            LineToPrint += "  " + str(Day)
        print(LineToPrint)

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
        
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    
    if iteration == total: 
        print()


