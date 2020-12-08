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
            containedBagsList.append( {
                'numBags': contBagMatch.group(1),
                'bagColor': contBagMatch.group(2),
                })
        bagsDict[bagCont.group(1)] = containedBagsList

#print( bagsDict )


def countHeldBags(bagColor):
    bagCount = 1
    for oneBagColor in bagsDict[bagColor]:
        bagColorCount = countHeldBags(oneBagColor['bagColor'])
        bagCount += int(oneBagColor['numBags']) * bagColorCount
    return bagCount

chosenColor = "shiny gold"
print( f"{chosenColor} bags hold {countHeldBags(chosenColor) - 1} other bags" )
    
    
