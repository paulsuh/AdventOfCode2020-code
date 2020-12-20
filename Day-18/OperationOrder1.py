#!/Users/plsuh/Projects/AdventOfCode2020-venv/bin/python

from sys import stdin
import re
from functools import reduce

# read in input text
inputText = stdin.read().splitlines()

# use switch-ish statement

# could be +, *, (, ), multi-digit number
tokenRE = re.compile( '(\+|\*|\(|\)|\d)(.*)' )
def nextToken( exprString ):

    if len(exprString) == 0:
        return "", ""
    nextTokenMatch = tokenRE.match( exprString )
    #print( nextTokenMatch.group(1), " XXX ", nextTokenMatch.group(2).lstrip() )
    return nextTokenMatch.group(1), nextTokenMatch.group(2).lstrip()
    
   
def plusHandler( prevValue, exprString ):
    
    # get the next real char of the remainder
    nextVal, remainder = nextValue( exprString )
    return evalExpr( prevValue + nextVal, remainder )

def timesHandler( prevValue, exprString ):
    
    # get the next real char of the remainder
    nextVal, remainder = nextValue( exprString )
    return evalExpr( prevValue * nextVal, remainder )

def closeParensHandler( prevValue, exprString ):
    
    # chop off close paren, return prevValue
    #print( prevValue, " YYY ", exprString)
    return prevValue, exprString

def defaultHandler( prevValue, exprString ):

    # we're at the end
    return prevValue, ""
    
def nextValue( exprString ):

    token, remainder = nextToken( exprString )
    # if it's a digit, return the digit and the remainder
    if token.isnumeric():
        return int(token), remainder
    
    # if it's a parenthesis, recurse
    elif token == '(':
        return evalExprStart( remainder )

handlerDict = {

    '+': plusHandler,
    '*': timesHandler,
    ')': closeParensHandler,
}

def evalExpr( prevValue, exprString ):

    token, remainder = nextToken( exprString )
    return handlerDict.get(token, defaultHandler)( prevValue, remainder )

def evalExprStart( exprString ):
    
    # load value
    val, remainder = nextValue( exprString )
    #print( val, remainder )
    
    return evalExpr( val, remainder )


# x = inputText[0]
# while len(x) > 0:
#     token, remainder = nextToken( x )
#     print(token)
#     print( "    ", remainder )
#     x = remainder

#print( evalExprStart( inputText[3] ))

result = reduce(
    lambda r, e: r + evalExprStart( e )[0],
    inputText,
    0
)

print( result )




