from pprint import pprint
import re


input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""


orderRules, updateRules = input.split("\n\n")

ruleByPage = {}


def isValidRule (update, before, after):    
    for beforeNum in ruleByPage[update]["before"]:
        pattern = r'((?:^|,){}(?=,|$))'.format(beforeNum)
        if re.search(pattern, after):
            return False
        
    for afterNum in ruleByPage[update]["after"]:
        pattern = r'((?:^|,){}(?=,|$))'.format(afterNum)
        if re.search(pattern, before):
            return False
        
    return True


for rule in orderRules.split("\n"):
    first, second = rule.split("|")
    
    if first in ruleByPage:
        ruleByPage[first]["after"].append(second)
    else:
        ruleByPage[first] = { "after": [second], "before": [] }
    
    if second in ruleByPage:
        ruleByPage[second]["before"].append(first)
    else:
        ruleByPage[second] = { "after": [], "before": [first] }

valids = []
for updatesRaw in updateRules.split("\n"):
    updates = updatesRaw.split(",")
    isValid = True
    for update in updates:
        pattern = r'((?:^|,){}(?=,|$))'.format(update)
        before, _, after = re.split(pattern, updatesRaw)
        
        isValid = isValid and isValidRule(update, before, after)
    if isValid:
        valids.append(updates)
            
middlePageNumberSum = 0
for valid in valids:
    middleIndex = len(valid) // 2
    middlePageNumberSum += int(valid[middleIndex])
    
print(middlePageNumberSum)