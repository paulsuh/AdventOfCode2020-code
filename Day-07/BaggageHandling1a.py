#!/Users/plsuh/Projects/AdventOfCode2020-venv/bin/python

from sys import stdin
import re

# regexes
noContainedBagsRE = re.compile( "(^\w+ \w+) bags contain no other bags.$" )
initialBagnameRE = re.compile( "^(\w+ \w+) bags contain (.+)\.$" )
containedBagtypeRE = re.compile( "^(\d) (\w+ \w+) (bag|bags)$")

# read in bag containment text
bagtypesRulesText = stdin.readlines()

bagsDict = {}
for oneLine in bagtypesRulesText:
    # (identifier) bags contain (n) (identifier) bag(s),...
    if noCont := noContainedBagsRE.match(oneLine):
        bagsDict[noCont.group(1)] = []
    else:
        bagCont = initialBagnameRE.match(oneLine)
        containedBagsList = []
        for oneContainedBag in bagCont.group(2).split(", "):
            contBagMatch = containedBagtypeRE.match(oneContainedBag)
            containedBagsList.append(contBagMatch.group(2))
        bagsDict[bagCont.group(1)] = containedBagsList

# print( bagsDict )

def checkBagtype( bagColor ):
    tempList = []
    if  "shiny gold" in bagsDict[bagColor]: 
        tempList.append(bagColor)
    for oneColor in bagsDict[bagColor]:
        recursiveList = checkBagtype(oneColor)
        if len(recursiveList) > 0:
            tempList.append(bagColor)
    return tempList

# walk the keys of the dict
colorsList = []
for oneKey in bagsDict.keys():
    colorsList += checkBagtype(oneKey)

print(f"Number of bag types that could hold a shiny gold bag = {len(set(colorsList))}")
