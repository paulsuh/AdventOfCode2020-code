#!/Users/plsuh/Projects/AdventOfCode2020-venv/bin/python

from sys import stdin

# read in input text
inputText = stdin.read().splitlines()

# split each line into a first letter and a number
movesList = list(
    map(
        lambda s: [s[0], int(s[1:])],
        inputText
        )
    )

leftTurnLookup = {
    '90': {
        'E': 'N',
        'N': 'W',
        'W': 'S',
        'S': 'E',
        },
    '180': {
        'E': 'W',
        'N': 'S',
        'W': 'E',
        'S': 'N',
        },
    '270': {
        'E': 'S',
        'N': 'E',
        'W': 'N',
        'S': 'W',
        },
    }
rightTurnLookup = {
    '90': {
        'E': 'S',
        'N': 'E',
        'W': 'N',
        'S': 'W',
        },
    '180': {
        'E': 'W',
        'N': 'S',
        'W': 'E',
        'S': 'N',
        },
    '270': {
        'E': 'N',
        'N': 'W',
        'W': 'S',
        'S': 'E',
        },
    }



def moveN( x, y, heading, distance ):
    return x, y+distance, heading

def moveS( x, y, heading, distance ):
    return x, y-distance, heading
    
def moveE( x, y, heading, distance ):
    return x+distance, y, heading
    
def moveW( x, y, heading, distance ):
    return x-distance, y, heading

def moveF( x, y, heading, distance ):
    return eval( f"move{heading}( {x}, {y}, '{heading}', {distance})" )

def moveL( x, y, heading, degrees ):
    return x, y, leftTurnLookup[str(degrees)][heading]

def moveR( x, y, heading, degrees ):
    return x, y, rightTurnLookup[str(degrees)][heading]

x=0
y=0
heading="E"
for oneMove in  movesList:
    print( oneMove )
    # print(f"move{oneMove[0]}({x},{y},{heading},{oneMove[1]})")
    x, y, heading = eval( f"move{oneMove[0]}({x},{y},'{heading}',{oneMove[1]})")
    print( x, y, heading )
    
print( f"Manhattan distance = {abs(x)} + {abs(y)} = {abs(x)+abs(y)}")
    
    
    
