#!/Users/plsuh/Projects/AdventOfCode2020-venv/bin/python

from sys import stdin

right = 3
# patternCols = 11
# patternRows = 11

# read in tree pattern from stdin
treeList = stdin.read().splitlines()

# get width from first line
patternCols = len(treeList[0])

# count lines to get number of rows
patternRows = len(treeList)

# merge the whole list into one string
treePattern = "".join(treeList)

# treePattern =   "..##......." + \
#                 "#...#...#.." + \
#                 ".#....#..#." + \
#                 "..#.#...#.#" + \
#                 ".#...##..#." + \
#                 "..#.##....." + \
#                 ".#.#.#....#" + \
#                 ".#........#" + \
#                 "#.##...#..." + \
#                 "#...##....#" + \
#                 ".#..#...#.#"
    
maxPosition = len(treePattern)

# start at position 0
position = 0
collisions = 0

for currRow in range(patternRows):
    if treePattern[currRow*patternCols + position] == "#":
        collisions += 1
    position = (position + right) % patternCols

print( f"Slope = {right} collisions = {collisions}" )
