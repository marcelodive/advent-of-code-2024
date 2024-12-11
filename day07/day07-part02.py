input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""


def generateOperatorsCombination(length):
    if (length == 0):
        return [[]]
    
    previousCombinations = generateOperatorsCombination(length - 1)
    combinations = []
    
    for operator in ('+', '*', '||'):
        for previousCombination in previousCombinations:
            combination = previousCombination + [operator]
            combinations.append(combination)
            
    return combinations


combinationsByLength = {}
def isValidEquation (equation):
    testValue = equation['testValue']
    numbers = equation['numbers']
    combinations = combinationsByLength[len(numbers)]
    for combination in combinations:
        value = numbers[0]
        for i in range(len(combination)):
            operator = combination[i]
            if (operator == '+'):
                value += numbers[i + 1]
            elif (operator == '*'):
                value *= numbers[i + 1]
            elif (operator == '||'):
                value = int(f"{value}{numbers[i + 1]}")
        if value == testValue:
            return True
    return False


equationsRaw = input.splitlines()

equations = []
for equationRaw in equationsRaw:
    testValue, numbersRaw = equationRaw.split(': ')
    equation = {
        'testValue': int(testValue),
        'numbers': [int(number) for number in numbersRaw.split(' ')],
        'isValid': False
    }
    equations.append(equation)


for equation in equations:
    positionsLength = len(equation['numbers'])
    if positionsLength not in combinationsByLength:
        combinationsByLength[positionsLength] = generateOperatorsCombination(positionsLength - 1)
        
    equation['isValid'] = isValidEquation(equation)
    
    
result = sum([equation['testValue'] for equation in equations if equation['isValid'] == True])
print(result)