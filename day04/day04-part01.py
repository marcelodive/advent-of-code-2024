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
    
    if matrix[x][y] != 'X':
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

 
result = 0

for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        result += countXmas(int(x), int(y))
        
print(result)