import re


input = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""

# Create arrays without don't()s, where every element will start with invalid instructions until find a do()
splitByDonts = input.split("don't()")

validInstructions = splitByDonts[0]
for chunk in splitByDonts:
    # Here I remove the invalid instructions (before the do()s) and keep only the valid instructions after the do()
    validInstructions += ''.join(chunk.split("do()")[1:]) if len(chunk.split("do()")) > 1 else '' 

pattern = r'mul\((\d+),(\d+)\)'
matches = re.findall(pattern, validInstructions)

result = 0
for x, y in matches:
    result += int(x) * int(y)

print(result)