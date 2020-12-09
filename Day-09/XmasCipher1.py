#!/Users/plsuh/Projects/AdventOfCode2020-venv/bin/python

from sys import stdin
from itertools import combinations


# read in asm code text
fullNumList = stdin.read().splitlines()

window = 25

def checkNumber( num, numList ):
    # combinatorics
    comboList = list( combinations(numList,2))
    print(num)
    #print( comboList )
    for oneCombo in comboList:
        sum = int(oneCombo[0]) + int(oneCombo[1])
        if sum == num:        
            print(f"matched: {oneCombo[0]} + {oneCombo[1]} = {sum}")
            return False
    # none matched
    return True

for i in range(window,len(fullNumList)-1):
    r = fullNumList[i-window:i]
    print(r)
    checkVal = checkNumber( int(fullNumList[i]), r )
    if checkVal:
        print(f"Invalid value = {fullNumList[i]} index = {i}")
        print(f"Range = {r}")
        break
