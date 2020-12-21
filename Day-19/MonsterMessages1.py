#!/Users/plsuh/Projects/AdventOfCode2020-venv/bin/python

from sys import stdin
import re

# read in input text
inputText = stdin.read().splitlines()

# first step is to read in just the rules
i = 0
rulesStringList = []
while len(oneLine := inputText[i]) > 0:
    rulesStringList.append(oneLine)
    print( oneLine )
    i += 1

# parse each rule into number and list of elements
rulesDict = {}
ruleParsingRE = re.compile("^(\d+): (.+)$")
for oneRuleString in rulesStringList:
    m = ruleParsingRE.match(oneRuleString)
    if m.group(2) == "\"a\"":
        r = ["a"]
    elif m.group(2) == "\"b\"":
        r = ["b"]
    else:
        r = m.group(2).split(" ")
    rulesDict[m.group(1)] = r
    #print(m.group(1), r)

# run through the dict substituting rules
while len(rulesDict) > 1:
    for ruleNum, ruleList in rulesDict.items():
    
        digitsMatch = re.search("\d", "".join(ruleList))
        if digitsMatch:
            # this rule still has sub-rules
            continue
    
        # this rule is ready to be swapped in
        # if it has a native "|" (not from a subrule), put parens around it
        if "|" in ruleList:
            ruleList.append(")")
            ruleList.insert(0, "(")
        # first remove any spaces
        squashedRuleText = "".join(ruleList)
    
        # run through each ruleText looking for the current rule
        for xRNum, xRList in rulesDict.items():
        
            if ruleNum in xRList:
                for j in range(len(xRList)):
                    if xRList[j] == ruleNum:
                        xRList[j] = squashedRuleText
    
        # remove the current rule from the dict
        del rulesDict[ruleNum]
        break

    #print( rulesDict )

finalREText = "^"+"".join(rulesDict["0"])+"$"

print(finalREText)
finalRE = re.compile(finalREText)

# now run through the rest of the lines
# skip 1 line
numValidMessages = 0
for oneString in inputText[i+1:]:
    #print( oneString, finalRE.search(oneString) )
    if finalRE.search(oneString):
        numValidMessages += 1

print( f"Number of valid messages = {numValidMessages}" )





