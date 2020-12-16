#!/Users/plsuh/Projects/AdventOfCode2020-venv/bin/python

from sys import stdin
import re

# read in input text
inputText = stdin.read().splitlines()

# parse first section
fieldRE = re.compile("^(.+): (\d+)-(\d+) or (\d+)-(\d+)$")
i = 0
allValidFieldValues = set()
validValuesByField = {}

for oneField in inputText:
    if len(oneField) == 0:
        break
    m = fieldRE.match(oneField)
    print(m.group(1),m.group(2),m.group(3),m.group(4),m.group(5))
    
    # add to sets of valid values
    tempSet = set()
    for validNum in range(int(m.group(2)), int(m.group(3))+1):
        allValidFieldValues.add(validNum)
        tempSet.add(validNum)
    for validNum in range(int(m.group(4)), int(m.group(5))+1):
        allValidFieldValues.add(validNum)
        tempSet.add(validNum)
    
    validValuesByField[m.group(1)] = tempSet
    
    # keep track of rows
    i += 1

# parse own ticket
ownTicket = inputText[i+2].split(",")
print(f"Own Ticket = {ownTicket}")

nearbyTickets = inputText[i+5:]

#print(sorted(list(validFieldValues)))
#print(nearbyTickets)
#print(validValuesByField)

validatedTickets=[]
# check each ticket for exclusion
for oneTicket in nearbyTickets:
    
    # check for validity
    ticketSplit=oneTicket.split(",")
    for oneFieldValue in ticketSplit:
        #print(oneFieldValue)
        if int(oneFieldValue) not in allValidFieldValues:
            break
    else:
        # all fields are valid
        validatedTickets.append(ticketSplit)

print(f"Validated Tickets count = {len(validatedTickets)}")


# prime the dict
columnsDict = {}
for i in range(len(validatedTickets[0])):
    columnsDict["col"+str(i)] = set()
    
# columnsDict = { 
#     "col0": set(),
#     "col1": set(),
#     "col2": set(),
# }

# load valid ticket values into dict
for oneValidTicket in validatedTickets:
    
    for i, oneValue in zip(range(len(oneValidTicket)), oneValidTicket):
        #print( i, oneValue )
        columnsDict["col"+str(i)].add(int(oneValue))

#print(columnsDict)

# compare set from dict element to valid values for each col
# prime the dict of potential valid columns
validFieldsDict = {}
for column, observedValues in columnsDict.items():
    
    tempSet = set()
    for oneField, validValuesForField in validValuesByField.items():
        
        if observedValues.issubset(validValuesForField):
            tempSet.add(oneField)
    
    validFieldsDict[column] = tempSet


# for colNum, fields in validFieldsDict.items():
#     print( colNum, ":", fields)
    
# work the logic down to figure out the actual mapping
searchComplete=False
finalMappingDict={}

while not searchComplete:

    searchComplete=True

#     for colNum, fields in validFieldsDict.items():
#         print( colNum, ":", fields)
    
    # go through each column in the dict, find one with only one field
    # use a list of keys, so that we can modify the dict and not get into trouble
    for oneCol in list(validFieldsDict):
        
        if len(validFieldsDict[oneCol]) == 1:
        
            # Record the value
            temp = validFieldsDict[oneCol].pop()
            
            # set final mapping
            finalMappingDict[oneCol]=temp
            
            # run through the dict and remove this value from the sets
            for s in validFieldsDict.values():
                s.discard(temp)
            
            # remove this column from the valid field dict
            del validFieldsDict[oneCol]
            
            # still need to keep looking
            searchComplete=False
            
            # exit the for loop
            break
    
    # if the if-statement never triggered, then searchComplete will be True
    # and the loop will exit


# for colNum, fields in finalMappingDict.items():
#     print( colNum, ":", fields)

# flip the keys and values around
reverseDict = {}
for k, v in finalMappingDict.items():
    reverseDict[v]=k

print( ownTicket )
result=1
for field, colNum in reverseDict.items():
    print( field, ":", colNum)
    if field.startswith("departure"):
        
        colIndex = int(colNum[3:])
        mulValue = int(ownTicket[colIndex])
        print( f"multiplying by column {colIndex} value {mulValue}")
        result *= mulValue

print( f"Final result = {result}")






   
    
    
    
    
    
    
