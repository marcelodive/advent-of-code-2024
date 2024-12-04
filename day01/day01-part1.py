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
for i, _ in enumerate(lefts):
    left = lefts[i]
    right = rights[i]
    result = result + abs(left - right)
    
print(result)
