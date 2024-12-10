import copy
import time

input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""


labMap = [list(row) for row in input.split()]
labMapClean = copy.deepcopy(labMap)

guardDirections = ('^', '>', '<', 'v')
actionByDirection = {
    '^': (-1, 0),
    '>': (0, 1),
    '<': (0, -1),
    'v': (1, 0),
}
nextDirection = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^',
}


def buildGuardInfo():
    for x in range(len(labMap)):
        for y in range(len(labMap[x])):
            if (labMap[x][y] in guardDirections):
                return {
                    'x': x,
                    'y': y,
                    'direction': labMap[x][y]
                }
                

def markGuardRoad(shouldPrint = False):
    countX = 0
    while(True):
        x, y, direction = guardInfo['x'], guardInfo['y'], guardInfo['direction']
        
        dirX, dirY = actionByDirection[direction]
        nextX = dirX + guardInfo['x']
        nextY = dirY + guardInfo['y']
        
        try:
            if labMap[x][y] == 'X':
                countX += 1
                
            if countX > ((4 * len(labMap)) + (4 * len(labMap[x]))):
                return True
            
            if labMap[x][y] != '#' and labMap[x][y] != 'O':
                labMap[x][y] = 'X'
            
            if shouldPrint == True:
                for m in range(len(labMap)):
                    print(labMap[m])
                print('\n')
                time.sleep(0.3)
                
            if nextX < 0 or nextY < 0:
                return None
            if labMap[nextX][nextY] == '#' or labMap[nextX][nextY] == 'O':
                guardInfo['direction'] = nextDirection[direction]
            elif labMap[nextX][nextY]:
                guardInfo['x'] = nextX
                guardInfo['y'] = nextY
        except Exception as e:
            return None
             

guardInfo = buildGuardInfo()
guardInfoClean = copy.deepcopy(guardInfo)

markGuardRoad()
    
possibleCombinations = {}
for i in range(len(labMap)):
    for j in range(len(labMap[i])):
        if labMap[i][j] == 'X':
            if i in possibleCombinations:
                possibleCombinations[i].append(j)
            else:
                possibleCombinations[i] = [j]
                
countLoop = 0
for i in possibleCombinations:
    for j in possibleCombinations[i]:
        guardInfo = copy.deepcopy(guardInfoClean)
        labMap = copy.deepcopy(labMapClean)
        labMap[i][j] = 'O'
        isLooped = markGuardRoad(False)
        if isLooped == True:
            countLoop += 1
               

print(countLoop)
    
        

