input="""7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""


def isReportSafe(levels):    
    isIncreasing = all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))
    isDecreasing = all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))
    isSafedAdjacent = all(abs(levels[i] - levels[i + 1]) <= 3 for i in range(len(levels) - 1))
    
    return (isIncreasing or isDecreasing) and isSafedAdjacent


reports = input.splitlines()

safeReportsCount = 0
for report in reports:
    levels = [int(level) for level in report.split()]
    safeReportsCount += 1 if isReportSafe(levels) else 0
    
print(safeReportsCount)
    

    
    
    