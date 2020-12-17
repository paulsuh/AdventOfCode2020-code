#!/Users/plsuh/Projects/AdventOfCode2020-venv/bin/python

from sys import stdin
import re
from functools import reduce
from itertools import product

# read in input text
inputText = stdin.read().splitlines()

# do this as dictionary of keys based on tuples
# could use numpy/scipy/pydata.sparse but it's simple enough
# to roll my own for this

class Sparse3D:

    # by convention
    # x values increase to the right starting from zero
    #   from the start of the initial layout
    # y values increase going down starting from zero
    #   from the start of the initial layout
    # z values start from zero in the initial layout
    #
    # this makes it easy to do the initial read
    
    def __init__(self):
        # dict to hold values
        self._values = {}
    
        # optimization to keep track of how big this space is
        # should really lazy init this from first setValue,
        # but good enough for now
        self._minCoords = (0,0,0)
        self._maxCoords = (0,0,0)
    
    # set a value
    def setValue( self, coords, val ):
        self._values[coords] = val
        if val != 0:
            self._updateMinMaxCoords( coords )
    
    # get a value
    def getValue( self, coords ):
        
        # take advantage of default value for dict.get
        return self._values.get(coords, 0)
    
    # update the minimum and maximum recorded dimensions
    def _updateMinMaxCoords( self, coords ):
    
        self._minCoords = (
            min( coords[0], self._minCoords[0]),
            min( coords[1], self._minCoords[1]),
            min( coords[2], self._minCoords[2]),
        )
        self._maxCoords = (
            max( coords[0], self._maxCoords[0]),
            max( coords[1], self._maxCoords[1]),
            max( coords[2], self._maxCoords[2]),
        )
    
    def dumpMinMaxCoords( self ):
        print(f"Min = {self._minCoords}")
        print(f"Max = {self._maxCoords}")
    
    def dumpSpaceValues( self ):
        for z in range(self._minCoords[2],self._maxCoords[2]+1):
            print( f"z={z}")
            for y in range(self._minCoords[1],self._maxCoords[1]+1):
                for x in range(self._minCoords[0],self._maxCoords[0]+1):
                    if self.getValue((x,y,z)) == 0 :
                        print(".",end="")
                    else:
                        print("#",end="")
                    # print(self.getValue((x,y,z)), end="")
                print()

    #value of surrounding cells
    def surroundingValue( self, coords ):
    
        result = reduce(
            lambda result, cellCoord: result+self.getValue(cellCoord),
            product( 
                range(coords[0]-1,coords[0]+2),
                range(coords[1]-1,coords[1]+2),
                range(coords[2]-1,coords[2]+2)
            ),
            0
        )
        return result-self.getValue(coords)
    
    # do this using a new Sparse3D instance for now
    # if we need to save memory we can optimize to doing it in place later
    def runOneCycle(self):
        
        result = Sparse3D()
        
        # walk all of the cells from min-1 to max+1
        # I guess I could do this with map() but it's too complicated
        for oneCoord in product(
                                range(self._minCoords[0]-1,self._maxCoords[0]+2),
                                range(self._minCoords[1]-1,self._maxCoords[1]+2),
                                range(self._minCoords[2]-1,self._maxCoords[2]+2),
                            ):
            sSum = self.surroundingValue(oneCoord)
            if sSum == 3:
                result.setValue(oneCoord,1)
            elif sSum == 2 and self.getValue(oneCoord) == 1:
                result.setValue(oneCoord,1)
#             else:
#                 # technically not necessary
#                 result.setValue(oneCoord,0)
        
        return result
    
    def totalCells( self ):
        return reduce(
            lambda r, coords: r + self.getValue( coords ),
            product( 
                range(self._minCoords[0],self._maxCoords[0]+1),
                range(self._minCoords[1],self._maxCoords[1]+1),
                range(self._minCoords[2],self._maxCoords[2]+1),
            ),
            0
        )

# Test out the class

space = Sparse3D()

# load data into space
for oneLine, y in zip(inputText,range(len(inputText))):
    
    for oneChar, x in zip( oneLine, range(len(oneLine))):
    
        if oneChar == "#":
            space.setValue( (x, y, 0), 1 )
        else:
            space.setValue( (x, y, 0), 0 )

# space.setValue( (0,1,2), 2 )
# space.setValue( (-1,1,3), 3 )
# space.setValue( (7,2,0), 4 )
# 
# 
# print( space.getValue((0,1,2)), space.getValue((0,0,0)) )
space.dumpMinMaxCoords()
space.dumpSpaceValues()

#print(space.totalCells())

# print(space.surroundingValue((0,0,-1)))

print( "\n*************  1  ****************\n")

space1 = space.runOneCycle()

space1.dumpSpaceValues()

print( "\n*************  2  ****************\n")

space2 = space1.runOneCycle()

space2.dumpSpaceValues()

print( "\n*************  3  ****************\n")

space3 = space2.runOneCycle()

space3.dumpSpaceValues()

print( "\n*************  4  ****************\n")

space4 = space3.runOneCycle()

space4.dumpSpaceValues()

print( "\n*************  5  ****************\n")

space5 = space4.runOneCycle()

space5.dumpSpaceValues()

print( "\n*************  6  ****************\n")

space6 = space5.runOneCycle()

space6.dumpSpaceValues()

print( "\n*************  7  ****************\n")

space6 = space5.runOneCycle()

space6.dumpSpaceValues()

print(space6.totalCells())
