#!/Users/plsuh/Projects/AdventOfCode2020-venv/bin/python

from sys import stdin
import copy

# read in asm code text
asmCodeBase = stdin.read().splitlines()


def acc( argVal, acc, pc, td ):
    acc += argVal
    td[pc]=1
    pc+=1
    return acc, pc, td

def jmp( argVal, acc, pc, td ):
    td[pc]=1
    pc += argVal
    return acc, pc, td

def nop( argVal, acc, pc, td ):
    td[pc]=1
    pc+=1
    return acc, pc, td

def asmToFunc( asm ):
    a = asm.split(" ")
    return a[0] + "(" + a[1] + ", accumulator, progCtr, trackingDict)"

def runProgram( asmCode ):
    accumulator = 0
    progCtr = 0
    trackingDict = {}
    while trackingDict.get(progCtr) is None:
        #print( f"acc={accumulator} pc={progCtr} instr={asmCode[progCtr]}" )
        accumulator, progCtr, td = eval( asmToFunc(asmCode[progCtr] ) )
        #print( progCtr, len(asmCode))
        if progCtr >= len(asmCode):
            return True, accumulator
    return False, accumulator

def changeInstruction( instrString ):
    print(f"Original = {instrString}")
    currInstr = instrString.split(" ")
    if currInstr[0] == "jmp":
        currInstr[0] = "nop"
    elif currInstr[0] == "nop":
        currInstr[0] = "jmp"
    result = currInstr[0]+" "+currInstr[1]
    print(f"Altered = {result}")
    return result

# check each instruction, change to opposite, run until progCtr goes
# off end or progCtr loops
for i in range(len(asmCodeBase)):
    
    print(f"Checking instruction {i}")
    currAsmCode=copy.deepcopy(asmCodeBase)
    currAsmCode[i] = changeInstruction(currAsmCode[i])
    didHalt, accumulator = runProgram( currAsmCode )
    if didHalt:
        print("Found instruction")
        break

print( f"Changed line #{i+1} {asmCodeBase[i]} acc={accumulator}" )

