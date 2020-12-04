#!/Users/plsuh/Projects/AdventOfCode2020-venv/bin/python

from sys import stdin

# read in passport pattern from stdin, split on double newline
passportStringList = stdin.read().split("\n\n")

# Take each line and transform it into a dict
def passportStringToDict( passportString ):
    
    resultDict = {}
    # split the passport into individual fields
    for oneField in passportString.split():
        fieldParts = oneField.split( ":" )
        resultDict[ fieldParts[0] ] = fieldParts[1]
    
    return resultDict

passportList = []
comparisonSet = {'byr', 
                 'iyr', 
                 'eyr', 
                 'hgt', 
                 'hcl', 
                 'ecl', 
                 'pid', }
#                 'cid' }   # cid is not needed for North Pole
validPassportCount = 0

for onePassportString in passportStringList:

    #passportList.append(passportStringToDict( onePassportString ))
    passportDict = passportStringToDict( onePassportString )

    # this gets the keys of the passportDict and puts them into a set
    # for unordered comparison    
    passportSet = set(list(passportDict))
    if comparisonSet.issubset(passportSet):
        validPassportCount += 1
    print( passportSet )
    print( comparisonSet.issubset(passportSet) )

print( f"Number of valid passports = {validPassportCount}" )

#print( passportList )

