#!/Users/plsuh/Projects/AdventOfCode2020-venv/bin/python

from sys import stdin
import re

# read in bag containment text
bagtypesList = stdin.readlines()

class Bagtype:
    
    # list of bags
    globalBagsDict = {}
        
    # for now assume that the list of rules is clean
    # each bag type is on the LHS just once
    def __init__(self, name, containedBagsString="" ):
        self.name = name
        
        self.containedBags = [] # list of bags that can go into this type
        if len(containedBagsString) > 0:
            for oneContainedBagString in containedBagsString.split(", "):
            
                containedBagsMatch = containedBagtypeRE.match(oneContainedBagString)
                self.containedBags.append( {
                        'numBags': containedBagsMatch.group(1),
                        'bagtype': containedBagsMatch.group(2)
                    } )
        self.containedByBags = set() # set of bags that can hold this type
        Bagtype.globalBagsDict[name] = self
    
    # raw add contained bag
    def _addContainedBag(self, containableBag, numBags):
        # create a containment node and add it to the list
        self.containedBags.add( {
                'numBags': numBags,
                'bagtype': containableBag
            } )

    # raw add containedBy bag
    def _addContainedByBag(self, containedByBag):
        self.containedByBags.add( containedByBag )
    
    # look up bag by name or instantiate it
    @classmethod
    def getBagByName(cls,bagName):
        try:
            return cls.globalBagsDict[bagName]
        except KeyError:
            # create and insert a new bag type
            a = Bagtype(bagName)
            cls.globalBagsDict[bagName] = a
            return a
    
    # put a bag type into this one
    # make sure the links work both ways
    def setContainedBag( self, containedBag, numBags ):
        self._addContainedBag( containedBag, numBags )
        containedBag._addContainedByBag( self )
    
#    @classmethod
#    def ruletextToBagtype( ruletext ):
    
    def __str__(self):
        return f"{self.name}: {self.containedBags}"
    
    def __repr__(self):
        return f"{self.name}: {self.containedBags}"

        
    
# regexes
noContainedBagsRE = re.compile( "(^\w+ \w+) bags contain no other bags.$" )
initialBagnameRE = re.compile( "^(\w+ \w+) bags contain (.+)\.$" )
containedBagtypeRE = re.compile( "^(\d) (\w+ \w+) (bag|bags)$")

def pairwise(iterable):
    a = iter(iterable)
    return zip( a, a )

for oneLine in bagtypesList:
    # (identifier) bags contain (n) (identifier) bag(s),...
    if noCont := noContainedBagsRE.match(oneLine):
        x = Bagtype( noCont.group(1) )
        print(x)
    # (identifier) bags contain no other bags
    else:
        bagtypeMatch = initialBagnameRE.match(oneLine)
        print( bagtypeMatch.group(1) )
#         for oneContainedBag in bagtypeMatch.group(2).split(", "):
#             contBagMatch = containedBagtypeRE.match(oneContainedBag)
#             print( f"     {contBagMatch.group(1)} - {contBagMatch.group(2)}" )
        x = Bagtype( bagtypeMatch.group(1), bagtypeMatch.group(2) )

    
print( Bagtype.globalBagsDict )

print( Bagtype.getBagByName("dark olive") )
    
    
