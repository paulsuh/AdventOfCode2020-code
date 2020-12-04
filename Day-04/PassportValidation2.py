#!/Users/plsuh/Projects/AdventOfCode2020-venv/bin/python

from sys import stdin
import re



fieldSet =  {
             'byr', 
             'iyr', 
             'eyr', 
             'hgt', 
             'hcl', 
             'ecl', 
             'pid',
#            'cid',    # cid is not needed for North Pole
            }

hairColorRE = re.compile( "^#[A-Fa-f0-9]{6}$" )

eyeColorSet = {
                "amb", 
                "blu", 
                "brn", 
                "gry", 
                "grn", 
                "hzl", 
                "oth", 
              }

passportIdRE = re.compile( "^[0-9]{9}$")



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


def validatePassport( passportDict ):

    # check for all fields present except for cid
    # (part  1). Return false immediately if it fails
    passportKeySet = set(list(passportDict))
    if not fieldSet.issubset(passportKeySet):
        return False
    
    # part 2: rules for each of the other elements
    # rough and ready, not trying to modularize or anything
    
    # birth year
    if int(passportDict['byr']) < 1920 or int(passportDict['byr']) > 2002:
        #print( f"Failed byr = {passportDict['byr'] }")
        return False
    
    # issue year
    if int(passportDict['iyr']) < 2010 or int(passportDict['iyr']) > 2020:
        print( f"    Failed iyr = {passportDict['iyr'] }")
        return False
    
    # expiration year
    if int(passportDict['eyr']) < 2020 or int(passportDict['eyr']) > 2030:
        print( f"        Failed eyr = {passportDict['eyr'] }")
        return False
    
    # height
    if "cm" in passportDict['hgt']:
        strippedHeight = int(passportDict['hgt'][0:-2])
        if strippedHeight < 150 or strippedHeight > 193:
            print( f"            Failed hgt-cm = {passportDict['hgt'] }")
            return False
    elif "in" in passportDict['hgt']:
        strippedHeight = int(passportDict['hgt'][0:-2])
        if strippedHeight < 59 or strippedHeight > 76:
            print( f"            Failed hgt-in = {passportDict['hgt'] }")
            return False
    else:
        print( f"            Failed hgt-nounits = {passportDict['hgt'] }")
        return False
        
    # hair color
    if not hairColorRE.match( passportDict['hcl'] ):
        print( f"                Failed hcl = {passportDict['hcl'] }")
        return False
        
    # eye color
    if not passportDict['ecl'] in eyeColorSet:
        print( f"                    Failed ecl = {passportDict['ecl'] }")
        return False
    
    # passport ID
    if not passportIdRE.match( passportDict['pid'] ):
        print( f"                    Failed pid = {passportDict['pid'] }")
        return False

    # passed all tests
    return True
    

validPassportCount = 0

for onePassportString in passportStringList:

    #passportList.append(passportStringToDict( onePassportString ))
    passportDict = passportStringToDict( onePassportString )

    # this gets the keys of the passportDict and puts them into a set
    # for unordered comparison    
    if validatePassport( passportDict ):
        validPassportCount += 1

print( f"Number of valid passports = {validPassportCount}" )


