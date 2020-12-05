#!/Users/plsuh/Projects/AdventOfCode2020-venv/bin/python

from sys import stdin
from functools import reduce


def seatIdCheck( prevSeatId, currSeatId ):
    if (currSeatId - prevSeatId) > 1:
        print( f"Seat before = {prevSeatId} Seat after = {currSeatId}")
    return currSeatId

seatCodeList = stdin.read().splitlines()
seatIdList = map( lambda seatCode: int( 
    seatCode.replace( "F", "0" ).replace( "B", "1" ). \
            replace( "L", "0" ).replace( "R", "1" ), 2 ), seatCodeList )

sortedSeatIdList = sorted(seatIdList) 

# function is too complex for a lambda
reduce( seatIdCheck, sortedSeatIdList )
