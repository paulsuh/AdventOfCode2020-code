#!/Users/plsuh/Projects/AdventOfCode2020-venv/bin/python

from sys import stdin
from itertools import count
import time

startTime=time.time()

# read in input text
inputText = stdin.read().splitlines()

# first line is timestamp
timestamp = int(inputText[0])

# split second line into bus ids
busIds = inputText[1].split(',')

#print(busIds)
        
# transform into pairs of [busId, position], discarding X's

filteredIds=[ [x[0],int(x[1])] for x in zip(count(0),busIds) if x[1] != 'x' ]

# print(filteredIds)

# optimization
# sort so that the highest busId is first, that way the jumps
# are as large as possible
sortedIds=sorted(filteredIds,key=lambda x: x[1], reverse=True)

# now need to adjust the positions so that they work for the
# new series of jumps
adjustment=sortedIds[0][0]
adjustedIds=list(map(
    lambda oneJump: [oneJump[0]-adjustment, oneJump[1]],
    sortedIds
))

print(adjustedIds)

# jump by first interval
# test each subsequent busId
# break if found
found=False
i=adjustedIds[0][1]
testIds=adjustedIds[1:]
# optimization: start at first jump past 100000000000000 as suggested/hinted
#t=i
# t=(100000000000000//i+1)*i
# #t=(2000//i+1)*i
# print(t)
# while not found:
#     
#     isFound=True
#     for j in testIds:
#         
#         jump=j[0]
#         busId=j[1]
#         if jump < 0:
#             testVal=(t//busId)*busId-t
#         else:
#             testVal=(t//busId+1)*busId-t
#         #print(t,busId,jump,testVal)
#         if testVal != jump:
#             isFound=False
#             break
#     
#     found=isFound
#     t+=i

# jump by first busId until find a match for second busId
# new jump is first * second, find match for third
# etc.
for busID in sortedIDs:
    
    

print(t-i-adjustment)

print(f"run time={time.time()-startTime}")
