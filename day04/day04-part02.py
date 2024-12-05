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


def countXmas(x, y):
    directions = [[1,0], [0,1], [-1,0], [0,-1], [1,1], [-1,-1], [1,-1], [-1,1]]
    
    if matrix[x][y] != 'A':
        return 0
    
    xmasCount = 0
    mas = ['M', 'A', 'S']
    for dx, dy in directions:
        for i in range(len(mas)):
            try:
                if (x+(dx*(i+1)) < 0 or y+(dy*(i+1)) < 0):
                    break
                if (matrix[x+(dx*(i+1))][y+(dy*(i+1))] != mas[i]):
                    break
            except:
                break
            if i == (len(mas) - 1):
                xmasCount += 1
    
    return xmasCount


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
    if xWord == 'SSMM' or xWord == 'MMSS' or xWord == 'SMMS' or xWord == 'MSSM':
       return True

 
result = 0

for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        result += 1 if isXMas(int(x), int(y)) else 0
        
print(result)