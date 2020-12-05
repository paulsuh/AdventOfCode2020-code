#!/Users/plsuh/Projects/AdventOfCode2020-venv/bin/python

from sys import stdin


seatCodeList = stdin.read().splitlines()
seatIdList = map( lambda seatCode: int( 
    seatCode.replace( "F", "0" ).replace( "B", "1" ). \
            replace( "L", "0" ).replace( "R", "1" ), 2 ), seatCodeList )

print( f"Maximum seat ID = {max(seatIdList)}" )
