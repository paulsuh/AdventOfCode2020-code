#!/Users/plsuh/Projects/AdventOfCode2020-venv/bin/python

from sys import stdin
import re
import regex

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
k=0
n=0
while len(rulesDict) > 1 and k < 1000:
    for ruleNum, ruleList in rulesDict.items():
    
#         if ruleNum == "42" or ruleNum == "31":
#             print( ruleNum, ruleList )

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
    if len(rulesDict) > 3:
        n += 1
    k += 1

print(n)
print( rulesDict )

# special case 8, 11 and 0
# 8 is a + match
rule8List = rulesDict["8"]
# pull out only the last element (rule 42 substitution)
rule8List = rule8List[0:1]
rule8List.append("+")
rule8Text = "".join(rule8List)

print()
print( rule8List )

# 11 is a recursive match
rule11List = rulesDict["11"]
rule11List = rule11List[3:]
# swap out "(?R)" for "11"
rule11List[1]="(?:(?126)?)"
rule11Text = "("+"".join(rule11List)+")"

print()
print( rule11List )

# set up rule 0 based on the texts for 8 and 11
finalREText = "^"+rule8Text+rule11Text+"$"


# finalREText = "^"+"".join(rulesDict["0"])+"$"

print()
print(finalREText)
finalRE = regex.compile(finalREText)

# now run through the rest of the lines
# skip 1 line
numValidMessages = 0
for oneString in inputText[i+1:]:
    #print( oneString, finalRE.search(oneString) )
    if finalRE.search(oneString):
        print(oneString)
        numValidMessages += 1

print( f"Number of valid messages = {numValidMessages}" )





