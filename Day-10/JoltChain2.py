#!/Users/plsuh/Projects/AdventOfCode2020-venv/bin/python

from sys import stdin
from itertools import tee

# read in jolt adapters text
joltListStrings = stdin.read().splitlines()

# transform into ints to avoid casting later
joltList = sorted(list(map( lambda x: int(x), joltListStrings )))

# put a zero on the front of the list
joltList.insert(0, 0)

# append a +3 at the end of the list
joltList.append( joltList[-1] + 3)


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


# brute force number of combos
# based on runs of 1 jolt gaps
# max run is 4 (I checked this data set)
# run of 4 --> 7 possible combos
# run of 3 --> 4 possible combos
# run of 2 --> 2 possible combos
# both ends of 3 jolt gap must be used
# run of 1 means both ends must be used (3-1-3) since without the 
#   1 jolt gap the interval is 4
# traverse from lowest to highest and get interval
oneJoltGaps=0
threeJoltGaps=0
prevThreeJolt=0
numCombos=1
for onePair in pairwise(joltList):
    gap = onePair[1] - onePair[0]
    if gap == 1:
        oneJoltGaps += 1
    else:
        threeJoltGaps += 1
        print(prevThreeJolt, onePair, onePair[0]-prevThreeJolt)
        runLen = onePair[0]-prevThreeJolt
        if runLen == 4:
            numCombos *= 7
        elif runLen == 3:
            numCombos *= 4
        elif runLen == 2:
            numCombos *= 2
        prevThreeJolt = onePair[1]

print( f"one jolt gaps = {oneJoltGaps}")
print( f"three jolt gaps = {threeJoltGaps}")
print( f"product = {oneJoltGaps*threeJoltGaps}")
print( f"numCombos = {numCombos}")
