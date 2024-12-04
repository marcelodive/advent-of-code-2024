input = """3 4
4 3
2 5
1 3
3 9
3 32"""

lines = input.splitlines()

lefts = []
rights = []

for line in lines:
    left, right = map(int, line.split())
    lefts.append(left)
    rights.append(right)

rights.sort()
lefts.sort()

result = 0
j = 0

for i in range(len(lefts)):
    left = lefts[i]
    
    if i > 0:
        formerLeft = lefts[i - 1]
        if left == formerLeft:
            result += left * repeats
            continue
    
    repeats = 0
    while j < len(rights) and rights[j] <= left:
        right = rights[j]
        if left == right:
            repeats += 1
        j += 1
        
    result += left * repeats

print(result)
