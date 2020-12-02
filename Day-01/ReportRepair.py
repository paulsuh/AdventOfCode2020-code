#!/usr/bin/python

from sys import stdin
from itertools import product

# read in data from stdin
values = list(map(int, stdin.readlines()))

# there really isn't a faster way than O(n^2); any speed gain
# from a faster algorithm would be lost to the initial sort

# filter generated tuples of values that add up to 2020
foundTuples = filter( 
        lambda t : (t[0] + t[1]) == 2020, 
        product( values, values ) 
    )

# There will be two, since the pairs are found (A,B) and (B,A)
# so we only need one
print ( "tuple is " + str( foundTuples[0] ) )
print ( foundTuples[0][0] *  foundTuples[0][1] )


