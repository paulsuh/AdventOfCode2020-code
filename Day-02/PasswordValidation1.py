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

    # then see how many testChars are in the pwString
    charCount = pwString.count(testChar)
    
    # see if the number of characters is between min and max
    totalMatches += minCount <= charCount <= maxCount
     
print( f"Number of valid passwords = {totalMatches}" )
