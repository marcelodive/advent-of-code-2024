input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""


matrix = [list(row) for row in input.split()]


def isXMas(x, y):
    
    if matrix[x][y] != 'A':
        return 0
    
    directions=[[-1,-1],[1,-1],[1,1],[-1,1]]
    
    xChars = []
    for dx, dy in directions:
       if (x+dx) < 0 or (y+dy) < 0:
           return False
       try: 
           xChars.append(matrix[x+dx][y+dy])
       except:
           return False
       
    xWord = ''.join(xChars)
    if xWord in ('SSMM', 'MMSS', 'SMMS', 'MSSM'):
       return True

 
result = 0

for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        result += 1 if isXMas(int(x), int(y)) else 0
        
print(result)