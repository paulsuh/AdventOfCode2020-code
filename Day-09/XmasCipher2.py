#!/Users/plsuh/Projects/AdventOfCode2020-venv/bin/python

from sys import stdin
from itertools import combinations, accumulate


# read in asm code text
fullNumListInput = stdin.read().splitlines()

# transform into ints to avoid casting later
fullNumList = list(map( lambda x: int(x), fullNumListInput ))

window = 25

def checkNumber( num, numList ):
    # combinatorics
    comboList = list( combinations(numList,2))
    #print(num)
    #print( comboList )
    for oneCombo in comboList:
        sum = oneCombo[0] + oneCombo[1]
        if sum == num:        
            print(f"matched: {oneCombo[0]} + {oneCombo[1]} = {sum}")
            return False
    # none matched
    return True

weaknum = 0
for i in range(window,len(fullNumList)-1):
    r = fullNumList[i-window:i]
    #print(r)
    checkVal = checkNumber( fullNumList[i], r )
    if checkVal:
        print(f"Invalid value = {fullNumList[i]} index = {i}")
        print(f"Prev {window} numbers = {r}")
        weaknum = fullNumList[i]
        break

# part 2

# slice lengths run from 2 to len(fullNumList)

for sliceLen in range(2,len(fullNumList)):
    print(f"Trying sliceLen = {sliceLen}")
    # move the slice down the list and sum the elements 
    for j in range(len(fullNumList)-sliceLen+1):
        #print(fullNumList[j:j+sliceLen])
        if sum(fullNumList[j:j+sliceLen]) == weaknum:
            print(f"found range {fullNumList[j:j+sliceLen]}")
            minNum = min(fullNumList[j:j+sliceLen])
            maxNum = max(fullNumList[j:j+sliceLen])
            print( f"sum = {minNum} + {maxNum} = {minNum + maxNum}")
            raise RuntimeError("found match")

