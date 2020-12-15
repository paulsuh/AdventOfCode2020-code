#!/Users/plsuh/Projects/AdventOfCode2020-venv/bin/python

from sys import stdin
import time
import re

startTime=time.time()

# read in input text
inputText = stdin.read().splitlines()

# mask1 = mask with X converted to zero
# result1 = value | mask1       # all 1's in mask set to 1
#
# mask2 = mask with X converted to 1
# result2 = result1 & mask2     # all 0's in mask set to 0

def parseMask( origMaskString ):
    
    mask1String = origMaskString.replace( "X", "0" )
    # print(mask1String)
    mask1 = int(mask1String,2)
    #print(mask1)
    xLocations = [m.start() for m in re.finditer("X", origMaskString)]
    
    return mask1, xLocations


maskRE = re.compile("^mask = (.*)$")
memRE = re.compile("^mem\[(\d+)\] = (\d+)$")
#maskString = maskRE.match( inputText[0] ).group(1)
#print(maskString)

#mask1, mask2 = parseMask(maskString)

#print( mask1, int.from_bytes(mask1, byteorder='big') )
#print( mask2, int.from_bytes(mask2, byteorder='big') )

# recurse over the list of X locations
# tweak baseLoc each time
# baseLoc comes in as a string, since it's easier
def writeToPermutedLocs( memValue, baseLoc, xLocList ):

    #print( "write entry: ", memValue, "".join(baseLoc), xLocList )

    if len(xLocList) == 0:
        # got a location, write the memValue
        memDict[str(int("".join(baseLoc),2))]=memValue
        print("MEM WRITE ", "".join(baseLoc), str(int("".join(baseLoc),2)), memValue)
    else:
        # permute the first location in the list
        permuteLoc = xLocList[0]
        #print( "permuteLoc: ", permuteLoc)
        tempLoc = baseLoc
        
        tempLoc[permuteLoc]="0"
        writeToPermutedLocs( memValue, tempLoc, xLocList[1:])
        
        tempLoc[permuteLoc]="1"
        writeToPermutedLocs( memValue, tempLoc, xLocList[1:])
    

currOrMask=0
xLocs=[]
memDict={}

# loop over the input
# if it's a mask line, update the currMask1 and currMask2 vars
# otherwise, set the dict line to the masked value
for oneLine in inputText: 
    if maskMatch := maskRE.match(oneLine):
        print("maskmatch:    ", maskMatch.group(1), maskMatch.group(1).count("X") )
        baseMask = list(maskMatch.group(1))
        xLocs = [m.start() for m in re.finditer("X", maskMatch.group(1))]
        #currMaskOr, xLocs = parseMask(maskMatch.group(1))
        
        # set up a logical OR mask for the first pass
        maskString = maskMatch.group(1).replace( "X", "0" )
        currOrMask = int(maskString,2)
        print("currOrMask: ", bin(currOrMask), xLocs)

    else:
        memMatch = memRE.match(oneLine)
        memLoc = int(memMatch.group(1))
        memVal = int(memMatch.group(2))
        
        memLocWithOr = memLoc | currOrMask
        memLocBaseFormatted = format(memLocWithOr, "036b")
        memLocBase = list(memLocBaseFormatted)
        
        #print("memMatch", memMatch.group(1),memLocBaseFormatted, memMatch.group(2))
        #print("permute entry: ", memVal, memLocBase, xLocs)
        writeToPermutedLocs( memVal, memLocBase, xLocs )
        
        #print( (int(memMatch.group(2)) | currMaskOr) & currMaskAnd, bin((int(memMatch.group(2)) | currMaskOr) & currMaskAnd) )
        #memDict[memLoc]=memVal

print(memDict)
print(len(memDict))
print(sum(memDict.values()))
#print(max(xList))
