import re


input = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""


# Create arrays without don't()s, where every element will start with invalid instructions until we find a do()
splitByDonts = input.split("don't()")

# The instructions start valid. I'm adding a pipe to avoid this case: mudon't()#!/usr/bin/python3mul(3,43)do()l(7,9)mul(6,9) (it should be 54)
validInstructions = splitByDonts[0] + '|'

for chunk in splitByDonts[1:]:
    # Here I remove the invalid instructions (before the do()s) and keep only the valid instructions after the do()
    validInstructions += '|'.join(chunk.split("do()")[1:]) if len(chunk.split("do()")) > 1 else ''
    validInstructions += '|'

pattern = r'mul\((\d+),(\d+)\)'
matches = re.findall(pattern, validInstructions)

result = 0
for x, y in matches:
    result += int(x) * int(y)

print(result)