#!/Users/plsuh/Projects/AdventOfCode2020-venv/bin/python

from sys import stdin
import regex

# read in input text
inputText = stdin.read().splitlines()

r = regex.compile( "(ab(?:(?R)?)cd)")

m = r.match( inputText[0] )

print( m )
print( m.group(1) )
