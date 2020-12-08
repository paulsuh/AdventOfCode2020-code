#!/Users/plsuh/Projects/AdventOfCode2020-venv/bin/python

from sys import stdin
from functools import reduce

# read in passport pattern from stdin, split on double newline
customsStringList = stdin.read().split("\n\n")


print( "Sum of counts = %d" %
    reduce(
        lambda countSum, currSet: countSum + len(currSet),
        map(
            lambda oneListOfLines: 
                reduce(
                    lambda prevSet, currSet: prevSet.union(currSet),
                    list(map(
                        lambda oneLine: { oneChar for oneChar in oneLine },
                        oneListOfLines
                        ))
                    ),
            map(
                lambda stringWithNewlines: stringWithNewlines.split("\n"),
                customsStringList
                )
            ),
        0
        )
    )

