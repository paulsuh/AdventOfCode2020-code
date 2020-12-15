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
    mask2String = origMaskString.replace( "X", "1" )
    #print(mask2String)
    mask2 = int(mask2String,2)
    #print(mask2)
    
    return mask1, mask2


maskRE = re.compile("^mask = (.*)$")
memRE = re.compile("^mem\[(\d+)\] = (\d+)$")
#maskString = maskRE.match( inputText[0] ).group(1)
#print(maskString)

#mask1, mask2 = parseMask(maskString)

#print( mask1, int.from_bytes(mask1, byteorder='big') )
#print( mask2, int.from_bytes(mask2, byteorder='big') )

currMaskOr=0
currMaskAnd=-1
memDict={}

# loop over the input
# if it's a mask line, update the currMask1 and currMask2 vars
# otherwise, set the dict line to the masked value
for oneLine in inputText: 
    if maskMatch := maskRE.match(oneLine):
        print(maskMatch.group(1))
        currMaskOr, currMaskAnd = parseMask(maskMatch.group(1))
        #print(currMaskOr, currMaskAnd)
        #print(bin(currMaskOr), bin(currMaskAnd))
    else:
        memMatch = memRE.match(oneLine)
        memLoc = memMatch.group(1)
        memVal = (int(memMatch.group(2)) | currMaskOr) & currMaskAnd
        print(memMatch.group(1), memMatch.group(2),bin(int(memMatch.group(2))))
        #print( (int(memMatch.group(2)) | currMaskOr) & currMaskAnd, bin((int(memMatch.group(2)) | currMaskOr) & currMaskAnd) )
        memDict[memLoc]=memVal

print(memDict)
print(sum(memDict.values()))
    
