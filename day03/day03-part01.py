import re


input = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""


pattern = r'mul\((\d+),(\d+)\)'
matches = re.findall(pattern, input)

result = 0
for x, y in matches:
    result += int(x) * int(y)

print(result)