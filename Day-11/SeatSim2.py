#!/Users/plsuh/Projects/AdventOfCode2020-venv/bin/python

from sys import stdin
from copy import deepcopy

# read in input text
inputText = stdin.read().splitlines()

maxX = len(inputText[0])
maxY = len(inputText)

additionDict={
    'L': 0,
    '#': 1,
    '.': 0,
}

# Python is nice since a string can be treated just like a list

def seatValue( x, y, matrix ):
    if (0 <= x < maxX) and (0 <= y < maxY):
        return additionDict[ matrix[y][x] ]
    else:
        return 0

def seatVisibleValue( x, y, dx, dy, matrix ):
    # dx = -1, 0, 1
    # dy = -1, 0, 1
    # move along until get a 1 or break bounds
    # skip self
    if dx == 0 and dy == 0:
        return 0
    tx = x + dx
    ty = y + dy
    while   tx >= 0 and tx < maxX and ty >= 0 and ty < maxY:
        if matrix[ty][tx] == "#":
            return 1
        elif matrix[ty][tx] == "L":
            return 0
        tx += dx
        ty += dy
    return 0
            

def seatSurroundingValue( x, y, matrix ):
    result = 0
    for yy in range(-1,2):
        for xx in range(-1,2):
            # print(xx,yy,seatValue(xx,yy,matrix))
            result += seatVisibleValue(x,y,xx,yy,matrix)
    # skip self
    # result -= seatValue( x, y, matrix )
    return result

def seatRoundResult( x, y, matrix ):
    # if it's a floor space it stays a floor space
    if matrix[y][x] == ".":
        return ".", False, 0
    
    cVal = matrix[y][x]
    sNum = seatSurroundingValue(x, y, matrix)
    #print(sNum)
    if sNum == 0:
        # surrounding seats empty, person sits
        return "#", cVal != "#", 1
    elif sNum >= 5:
        # more than 5 surrounding, person leaves
        return "L", cVal != "L", 0
    else:
        # stays the same
        return matrix[y][x], False, 1 if cVal == "#" else 0
        
def oneRound( inputMatrix ):
    returnMatrix = []
    delta = False
    totalOccSeats = 0
    for y in range(0,maxY):
        lineBuilder = ""
        for x in range(0,maxY):
            newChar, currDelta, seatCountVal = seatRoundResult(x,y,inputMatrix)
            lineBuilder += newChar
            delta = delta or currDelta
            totalOccSeats += seatCountVal
            #print(f"{seatRoundResult(x,y,inputText)}", end="")
        returnMatrix.append(lineBuilder)
        #print()
    return returnMatrix, delta, totalOccSeats

#print(maxX, maxY)
#print(oneRound(inputText))
#print( seatRoundResult( 3, 3, inputText))
#print( seatVisibleValue( 5, 4, -1, 0, inputText))

currentState = inputText
seatsChanged = True
i = 0
while seatsChanged:
    # print( currentState )
    newState, seatsChanged, occSeats = oneRound( currentState )
    # print( newState, seatsChanged, occSeats)
    print( f"Round {i}, {seatsChanged}, occupied seats = {occSeats}")
    currentState = newState
    i += 1
    # print( currentState )
    #if i > 20:
    #    break

    

