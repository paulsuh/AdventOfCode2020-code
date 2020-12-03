#!/usr/bin/python

from sys import stdin
import re


# read in data from stdin
values = stdin.read().splitlines()

# Compile regular expression
# 12-14 x: xxxxxxxxxxxcxxxx
pwRegex = re.compile( "(\d+)-(\d+) ([A-Za-z]): ([A-Za-z]+)")

totalMatches = 0

# for each line, parse out minimum, maximum, letter, password string
for oneLine in values:
    
    result = pwRegex.search( oneLine )
    minCount = int(result.group(1))
    maxCount = int(result.group(2))
    testChar = result.group(3)
    pwString = result.group(4)
    
    sumOfChars = 0
    # see if testChar is in the minCount place the pwString
    if pwString[minCount - 1] == testChar:
        sumOfChars += 1
    if pwString[maxCount - 1] == testChar:
        sumOfChars += 1
    if sumOfChars == 1:
        totalMatches += 1

print( f"Number of valid passwords = {totalMatches}" )
