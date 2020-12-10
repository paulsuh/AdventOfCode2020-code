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

print(joltList)

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

# traverse from lowest to highest and get interval
oneJoltGaps=0
threeJoltGaps=0
for onePair in pairwise(joltList):
    gap = onePair[1] - onePair[0]
    if gap == 1:
        oneJoltGaps += 1
    else:
        threeJoltGaps += 1
    print(onePair, gap)

print( f"one jolt gaps = {oneJoltGaps}")
print( f"three jolt gaps = {threeJoltGaps}")
print( f"product = {oneJoltGaps*threeJoltGaps}")
