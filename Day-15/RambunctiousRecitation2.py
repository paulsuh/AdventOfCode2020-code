#!/Users/plsuh/Projects/AdventOfCode2020-venv/bin/python

from sys import stdin

# read in input text
inputText = stdin.read().splitlines()

currentTurnNum = 1
spokenNums={}
prevNumStr = "0"
prevNumTurnNum = -1

# prime the dict
for n in inputText[0].split(","):
    spokenNums[n] = currentTurnNum
    prevNumStr = n
    prevNumTurnNum = -1
    print(currentTurnNum,n)
    currentTurnNum += 1

# next number is always "0"
# prevNumStr = "0"
# prevNumTurnNum = spokenNums.get(prevNumStr,-1)
# print(currentTurnNum,prevNumStr)
# currentTurnNum += 1

# print(spokenNums)
while currentTurnNum <= 30000000:
    if currentTurnNum % 1000000 == 0:
        print(currentTurnNum)
    prevTurnNum = spokenNums.get(prevNumStr,-1)
    #print(f"   prevNumStr={prevNumStr}  prevNumTurnNum={prevNumTurnNum}")
    if prevNumTurnNum == -1:
        # number has never been spoken
        currNumStr = "0"
    else:
        currNumStr = str(currentTurnNum - prevNumTurnNum - 1)
    
    #print(f"{currentTurnNum} prevNumStr={prevNumStr} prevNumTurnNum={prevNumTurnNum} currNumStr={currNumStr}")
    spokenNums[prevNumStr]=currentTurnNum - 1
    prevNumStr = currNumStr
    prevNumTurnNum = spokenNums.get(currNumStr,-1)
    currentTurnNum += 1

print(currNumStr)
