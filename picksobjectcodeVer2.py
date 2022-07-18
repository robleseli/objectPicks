#!/usr/bin/env python3
import sys

pickpath='./syst_linux_py/radutils'
#print(sys.path)

#from pickutils.py import Picks
#Picks()

sys.path.insert(1,pickpath)

print(sys.path)

from pickutils import Picks
printpicks = Picks([1,1,1],[1,1,1],[1,1,1], "pst", "product",1,
"label",
"filepath") #setting the last one as None returns a typeError.
print(printpicks)

try:
    printpicks.load()
except TypeError as e:
    print(e)
    raise e

print("end")



add_pick = printpicks.add_pick(1,1,True)  #positional arg.

print(add_pick)
print("end2")
