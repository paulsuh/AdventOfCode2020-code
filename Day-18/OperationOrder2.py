#!/Users/plsuh/Projects/AdventOfCode2020-venv/bin/python

from sys import stdin
import re
from functools import reduce

# read in input text
inputText = stdin.read().splitlines()

hwTotal = 0
for oneLine in inputText:
    # build total using stack

    stack = []
    postfixList = []
    expr = oneLine.replace(" ", "")

    print(expr)

    # Original method
    # 
    # for t in expr:
    #     
    #     print(postfixList,stack)
    #     
    #     if t.isdigit():
    #         postfixList.append( t )
    #     elif t == "(":
    #         stack.append(t)
    #     elif t == ")":
    #         while (p := stack.pop()) != "(":
    #             postfixList.append(p)
    #     # not a number or parens, must be an operator
    #     elif len(stack) == 0:
    #         stack.append(t)
    #     # stack has something on top, 
    #     elif t == "+":
    #         while len(stack) > 0 and stack[-1] != "(":
    #             postfixList.append(stack.pop())
    #         stack.append(t)
    #     else:   # t == "*":
    #         while len(stack) > 0 and stack[-1]=="*":
    #             postfixList.append(stack.pop())
    #         stack.append(t)
    
    # precedence of + and * reversed
    for t in expr:
    
        # print(postfixList,stack)
    
        if t.isdigit():
            postfixList.append( t )
        elif t == "(":
            stack.append(t)
        elif t == ")":
            while (p := stack.pop()) != "(":
                postfixList.append(p)
        # not a number or parens, must be an operator
        elif len(stack) == 0:
            stack.append(t)
        # stack has something on top, 
        elif t == "*":
            while len(stack) > 0 and stack[-1] != "(":
                postfixList.append(stack.pop())
            stack.append(t)
        else:   # t == "+":
            while len(stack) > 0 and stack[-1]=="+":
                postfixList.append(stack.pop())
            stack.append(t)

    # print( postfixList, list(reversed(stack)) )
    # now pop everything off the stack
    result = postfixList + list(reversed(stack))

    print( result )

    # now evaluate the postfix expression
    total = 0
    buffer = []
    for x in result:
    
        if x.isdigit():
            buffer.append(x)
            # print(buffer)
        elif x == "+":
            y = int(buffer[-2]) + int(buffer[-1])
            buffer = buffer[:-2]
            # print("+", str(y), buffer)
            buffer.append(str(y))
            # print(buffer)
        elif x == "*":
            y = int(buffer[-2]) * int(buffer[-1])
            # print("*", str(y), buffer)
            buffer = buffer[:-2]
            buffer.append(str(y))
            # print(buffer)

    print(buffer)
    hwTotal += int(buffer[0])

print(hwTotal)

