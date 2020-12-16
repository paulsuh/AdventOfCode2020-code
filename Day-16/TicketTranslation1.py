#!/Users/plsuh/Projects/AdventOfCode2020-venv/bin/python

from sys import stdin
import re

# read in input text
inputText = stdin.read().splitlines()

# parse first section
fieldRE = re.compile("^.+: (\d+)-(\d+) or (\d+)-(\d+)")
i = 0
validFieldValues = set()
for oneField in inputText:
    if len(oneField) == 0:
        break
    m = fieldRE.match(oneField)
    print(m.group(1),m.group(2),m.group(3),m.group(4))
    for validNum in range(int(m.group(1)), int(m.group(2))+1):
        validFieldValues.add(validNum)
    for validNum in range(int(m.group(3)), int(m.group(4))+1):
        validFieldValues.add(validNum)
    i += 1

# skip own ticket for now
nearbyTickets = inputText[i+5:]

#print(sorted(list(validFieldValues)))
#print(nearbyTickets)

errorRateSum=0
# check each ticket for exclusion
for oneTicket in nearbyTickets:
    for oneFieldValue in oneTicket.split(","):
        #print(oneFieldValue)
        if int(oneFieldValue) not in validFieldValues:
            errorRateSum += int(oneFieldValue)

print( f"Ticket scanning error rate = {errorRateSum}")
