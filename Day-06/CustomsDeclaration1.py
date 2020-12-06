#!/Users/plsuh/Projects/AdventOfCode2020-venv/bin/python

from sys import stdin
from functools import reduce

# read in passport pattern from stdin, split on double newline
customsStringList = stdin.read().split("\n\n")


result = 0
for oneGroup in customsStringList:

    # split each line into sets of chars
    lineSets = map( lambda oneLine: {oneChar for oneChar in oneLine}, 
                        oneGroup.splitlines() )
    
    # union the sets for each group of lines
    groupSet = reduce( lambda prevSet, currSet: prevSet.union(currSet), 
                lineSets)
    result += len(groupSet)

print( f"Sum of counts = {result}")
        
