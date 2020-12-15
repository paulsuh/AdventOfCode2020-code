#!/Users/plsuh/Projects/AdventOfCode2020-venv/bin/python

from sys import stdin

# read in input text
inputText = stdin.read().splitlines()

# first line is timestamp
timestamp = int(inputText[0])

# split second line into bus ids
busIds = list(map(
            lambda x: 0 if x=='x' else int(x),
            [i for i in inputText[1].split(',') if i != 'x']
            ))
        
#print( busIds )

# for each busId, do integer division with remainder
timesList = [ [i]+list(divmod(timestamp,i)) for i in busIds ]

#print(timesList)

# subtract the remainder from the busId to get the next time
# that busId arrives
busNextTimes = list(map(
                        lambda x: [x[0], x[0]-x[2]],
                        timesList
                        ))

print(busNextTimes)

# get the minimum element
result = min(busNextTimes, key=lambda busNextTime: busNextTime[1])

print(f"Bus id={result[0]}, wait minutes={result[1]}, product={result[0]*result[1]}")
