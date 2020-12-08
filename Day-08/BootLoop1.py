#!/Users/plsuh/Projects/AdventOfCode2020-venv/bin/python

from sys import stdin


# read in asm code text
asmCode = stdin.read().splitlines()

accumulator = 0
progCtr = 0
trackingDict = {}


def acc( argVal ):
    global accumulator, progCtr, trackingDict
    accumulator += argVal
    trackingDict[progCtr]=1
    progCtr+=1

def jmp( argVal ):
    global accumulator, progCtr, trackingDict
    trackingDict[progCtr]=1
    progCtr += argVal

def nop( argVal ):
    global accumulator, progCtr, trackingDict
    trackingDict[progCtr]=1
    progCtr+=1

def asmToFunc( asm ):
    a = asm.split(" ")
    return a[0] + "(" + a[1] + ")"

while trackingDict.get(progCtr) is None:
    print( f"acc={accumulator} pc={progCtr} instr={asmCode[progCtr]}" )
    eval( asmToFunc(asmCode[progCtr]) )

print( f"Final (not executed): acc={accumulator} pc={progCtr} instr={asmCode[progCtr]}" )

