#!/Users/plsuh/Projects/AdventOfCode2020-venv/bin/python

from sys import stdin

slopes =    ( (1, 1), 
              (3, 1),
              (5, 1),
              (7, 1),
              (1, 2)
            )

# read in tree pattern from stdin
treeList = stdin.read().splitlines()

# get width from first line
patternCols = len(treeList[0])

# count lines to get number of rows
patternRows = len(treeList)

# merge the whole list into one string
treePattern = "".join(treeList)

maxPosition = len(treePattern)

def evalOneSlope( right, down ):
    
    # start at position 0
    position = 0
    collisions = 0

    for currRow in range(0, patternRows, down):
        if treePattern[currRow*patternCols + position] == "#":
            collisions += 1
        #print(treePattern)
        #for i in range( currRow*patternCols + position ):
        #    print( " ", end="" )
        #print("^")
        position = (position + right) % patternCols
    
    return collisions

productValue = 1
for oneSlope in slopes:
    collisions = evalOneSlope( oneSlope[0], oneSlope[1] )
    print( f"right = {oneSlope[0]} down = {oneSlope[1]} collisions = {collisions}" )
    productValue *= collisions

print( f"product = {productValue}" )







