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
# rotation matrix
# [ cos -sin ] [x]
# [ sin  cos ] [y]

# left 90 = pi/2 = right 270
# [ 0   -1 ]
# [ 1    0 ]

# 180 = pi
# [ -1   0 ]
# [ 0   -1 ]

# left 270 = 3pi/2 = right 90
# [ 0    1 ]
# [ -1   0 ]

def left90( wx, wy ):
    return wx * 0 + wy * -1, wx * 1 + wy * 0

def left180( wx, wy ):
    return wx * -1 + wy * 0, wx * 0 + wy * -1

def left270( wx, wy ):
    return wx * 0 + wy * 1, wx * -1 + wy * 0

def right90( wx, wy ):
    return left270( wx, wy )

def right180( wx, wy ):
    return left180( wx, wy )
    
def right270( wx, wy ):
    return left90( wx, wy )


def moveN( x, y, wx, wy, heading, distance ):
    return x, y, wx, wy+distance, heading

def moveS( x, y, wx, wy, heading, distance ):
    return x, y, wx, wy-distance, heading
    
def moveE( x, y, wx, wy, heading, distance ):
    return x, y, wx+distance, wy, heading
    
def moveW( x, y, wx, wy, heading, distance ):
    return x, y, wx-distance, wy, heading

def moveF( x, y, wx, wy, heading, distance ):
    return x + wx*distance, y+wy*distance, wx, wy, heading

def moveL( x, y, wx, wy, heading, degrees ):
    newWx, newWy = eval(f"left{str(degrees)}( {wx}, {wy} )")
    return x, y, newWx, newWy, leftTurnLookup[str(degrees)][heading]

def moveR( x, y, wx, wy, heading, degrees ):
    newWx, newWy = eval(f"right{str(degrees)}( {wx}, {wy} )")
    return x, y, newWx, newWy, rightTurnLookup[str(degrees)][heading]

x=0
y=0
heading="E"
wx = 10
wy = 1
for oneMove in  movesList:
    print( oneMove )
    print(f"move{oneMove[0]}({x},{y},{wx},{wy},{heading},{oneMove[1]})")
    x, y, wx, wy, heading = eval( f"move{oneMove[0]}({x},{y},{wx},{wy},'{heading}',{oneMove[1]})")
    print( x, y, wx, wy, heading )
    
print( f"Manhattan distance = {abs(x)} + {abs(y)} = {abs(x)+abs(y)}")
    
    
    
