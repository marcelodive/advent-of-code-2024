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
                

def markGuardRoad():
    while(True):
        x, y, direction = guardInfo['x'], guardInfo['y'], guardInfo['direction']
        
        dirX, dirY = actionByDirection[direction]
        nextX = dirX + guardInfo['x']
        nextY = dirY + guardInfo['y']
        
        try:
            labMap[x][y] = 'X'

            # for line in labMap:
            #     print(' '.join(line))
            
            # print('\n\n')

            if nextX < 0 or nextY < 0:
                return None
            if labMap[nextX][nextY] == '#':
                guardInfo['direction'] = nextDirection[direction]
            elif labMap[nextX][nextY]:
                guardInfo['x'] = nextX
                guardInfo['y'] = nextY
        except Exception as e:
            return None
                

guardInfo = buildGuardInfo()

markGuardRoad()
    
count = 0
for i in range(len(labMap)):
    for j in range(len(labMap[i])):
        if labMap[i][j] == 'X':
            count += 1

print(count)
    
        

